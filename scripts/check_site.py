#!/usr/bin/env python3
"""Read-only checks for content parity, downloads and subpath-safe links."""
from hashlib import sha256
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

from bs4 import BeautifulSoup, Tag
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
texts = json.loads((ROOT / 'content/prompt-texts.json').read_text())['prompts']
slides = json.loads((ROOT / 'content/slides.json').read_text())
slide_numbers = [slide['number'] for slide in slides]
assert slide_numbers == list(range(1, len(slides) + 1)), 'Slide numbers must be continuous.'
slide_count = len(slides)
prompt_count = len(texts)
prompt_index_number = next(slide['number'] for slide in slides if slide['kind'] == 'prompt-index')
pages = list(SITE.rglob('index.html'))
assert len(pages) == slide_count + prompt_count + 1, len(pages)


def required(soup: BeautifulSoup, selector: str) -> Tag:
    element = soup.select_one(selector)
    assert isinstance(element, Tag), selector
    return element


def normal(text: str) -> str:
    return ' '.join(text.split())


def slide_page(number: int) -> Path:
    return SITE / ('index.html' if number == 1 else f'pages/{number:02d}/index.html')


def local_target(path: Path, raw: str) -> Path:
    parts = urlsplit(raw)
    assert not parts.scheme and not raw.startswith('/'), (path, raw)
    target = (path.parent / unquote(parts.path)).resolve()
    assert target.is_relative_to(SITE.resolve()), (path, raw)
    return target / 'index.html' if target.is_dir() else target


def soup_for_slide_kind(kind: str) -> BeautifulSoup:
    slide = next(slide for slide in slides if slide['kind'] == kind)
    return BeautifulSoup(slide_page(slide['number']).read_text(), 'html.parser')


for path in pages:
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    assert required(soup, 'html').get('lang') == 'en'
    assert soup.find('meta', attrs={'name': 'viewport'})
    assert len(soup.find_all('h1')) == 1
    required(soup, 'main#main')
    ids = [str(element['id']) for element in soup.select('[id]')]
    assert len(ids) == len(set(ids)), f'Duplicate IDs: {path}'
    for image in soup.find_all('img'):
        assert image.has_attr('alt'), f'Missing image alt: {path}'
    for element in soup.select('[href], [src]'):
        raw = str(element.get('href') or element.get('src') or '')
        if raw.startswith('#'):
            assert soup.find(id=raw[1:]), (path, raw)
            continue
        parts = urlsplit(raw)
        if parts.scheme:
            assert parts.scheme == 'https', (path, raw)
            assert not any(host in parts.netloc for host in ('localhost', '127.0.0.1', 'manus.computer'))
            continue
        target = local_target(path, raw)
        assert target.is_file(), f'Broken link: {path}: {raw}'
    for copy in soup.select('[data-copy]'):
        assert soup.find(id=str(copy['data-copy'])), f'Invalid clipboard target: {path}'
    footer_text = required(soup, 'footer.site-footer').get_text(' ', strip=True)
    assert 'Downloads & links' not in footer_text, path
    assert 'Print this page' not in footer_text, path
    assert soup.select_one('[data-print]') is None, path
    previous = required(soup, 'a[data-page-previous]')
    if path.is_relative_to(SITE / 'prompts'):
        assert local_target(path, str(previous['href'])) == slide_page(prompt_index_number).resolve()
        assert soup.select_one('a[data-page-next]') is None
        choices = soup.select('.prompt-switcher-menu li a')
        assert len(choices) == prompt_count
        for number, choice in enumerate(choices, 1):
            assert local_target(path, str(choice['href'])) == (SITE / f'prompts/{number:02d}/index.html').resolve()
        assert len(soup.select('.prompt-switcher-menu a[aria-current=page]')) == 1
    else:
        required(soup, 'a[data-page-next]')
        assert soup.select_one('.prompt-switcher') is None

for index, slide in enumerate(slides):
    path = slide_page(slide['number'])
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    main_text = normal(required(soup, 'main').get_text(' ', strip=True))
    for point in slide.get('points', []):
        assert normal(point) in main_text, (slide['number'], point)
    for note in slide.get('notes', []):
        assert normal(note) in main_text, (slide['number'], note)
    previous = required(soup, 'a[data-page-previous]')
    expected_previous = SITE / 'resources/index.html' if index == 0 else slide_page(slides[index - 1]['number'])
    assert local_target(path, str(previous['href'])) == expected_previous.resolve(), (slide['number'], 'previous')
    following = required(soup, 'a[data-page-next]')
    expected_following = slide_page(slides[index + 1]['number']) if index + 1 < slide_count else slide_page(prompt_index_number)
    assert local_target(path, str(following['href'])) == expected_following.resolve(), (slide['number'], 'next')
    assert f'Slide {slide["number"]:02d} / {slide_count}' in main_text, slide['number']

for number, text in enumerate(texts, 1):
    soup = BeautifulSoup((SITE / f'prompts/{number:02d}/index.html').read_text(), 'html.parser')
    for key, suffix in [('example_en', 'en'), ('example_zh', 'zh-Hant'), ('template_en', 'en-template'), ('template_zh', 'zh-Hant-template')]:
        assert required(soup, '#prompt-' + suffix).get_text() == text[key], (number, key)
        assert not re.search(r'\b20\d{2}\b', text[key]), (number, key, 'fixed year')
    assert text['example_en'].endswith('Write in English.')
    assert text['example_zh'].endswith('請以繁體中文回答。')
    all_text = required(soup, 'main').get_text(' ', strip=True)
    assert f'Prompt {number:02d} / {prompt_count}' in all_text
    assert 'Situation' in all_text and 'Sources to add to Notebook' in all_text

for filename in ['DigitalEducationBlueprint(Chinese).pdf', 'DigitalEducationBlueprint(English).pdf']:
    uploaded = Path('/home/ubuntu/upload') / filename
    assert sha256(uploaded.read_bytes()).digest() == sha256((SITE / 'downloads' / filename).read_bytes()).digest()

with ZipFile(SITE / 'downloads/Gemini-Notebook-Workshop.pptx') as archive:
    assert archive.testzip() is None
    presentation_slide_count = len([name for name in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)])
assert presentation_slide_count == slide_count

studio_source = Path('/home/ubuntu/workshop/studio-examples')
original_downloads = {
    'studio-infographic-default-original.png': studio_source / 'Infographics/01. Infographic (Default).png',
    'studio-infographic-custom-original.png': studio_source / 'Infographics/03. Infographic (Custom).png',
    'studio-deck-default-original.pdf': studio_source / 'Slides/01. Slides (Default).pdf',
    'studio-deck-custom-original.pdf': studio_source / 'Slides/03. Slides (Custom).pdf',
}
for filename, source in original_downloads.items():
    assert sha256(source.read_bytes()).digest() == sha256((SITE / 'downloads' / filename).read_bytes()).digest(), filename

studio_slides = {slide['id']: slide for slide in slides if slide['kind'] == 'studio-example'}
assert list(studio_slides) == [
    'info_default', 'info_prompt', 'info_custom', 'info_detail',
    'deck_default', 'deck_prompt', 'deck_custom', 'deck_detail',
]
for studio_id, slide in studio_slides.items():
    path = slide_page(slide['number'])
    source = path.read_text()
    soup = BeautifulSoup(source, 'html.parser')
    main_text = normal(required(soup, 'main').get_text(' ', strip=True))
    assert normal(slide['summary']) in main_text, studio_id
    for paragraph in slide.get('paragraphs', []):
        assert normal(paragraph) in main_text, (studio_id, paragraph)
    if slide.get('callout'):
        assert normal(slide['callout']) in main_text, (studio_id, slide['callout'])
    if slide.get('badge'):
        assert normal(slide['badge']) in main_text, (studio_id, slide['badge'])
    caution = slide.get('draft_note') or 'Supplied AI-generated draft — not independently verified policy. Verify any figures, dates, mandates, strategies, funding or curriculum claims shown in the output against the original sources before using them.'
    assert normal(caution) in main_text, studio_id
    for image in slide.get('images', []):
        assert image['file'] in source, (studio_id, image['file'])
        assert (SITE / 'assets' / image['file']).is_file(), image['file']
        image_link = next(link for link in soup.select('a.shot') if image['file'] in str(link.get('href')))
        assert image_link.get('target') == '_blank', studio_id
    for download in slide.get('downloads', []):
        assert any(download['file'] in str(link.get('href')) and link.has_attr('download') for link in soup.select('a')), download['file']

info_prompt = studio_slides['info_prompt']
info_prompt_soup = BeautifulSoup(slide_page(info_prompt['number']).read_text(), 'html.parser')
assert required(info_prompt_soup, '#prompt-en').get_text() == 'Focus on information that is relevant to students'
assert 'Portrait (9:16)' in info_prompt_soup.get_text(' ', strip=True)
assert 'Low' in info_prompt_soup.get_text(' ', strip=True)
assert 'Anime' in info_prompt_soup.get_text(' ', strip=True)
deck_prompt = studio_slides['deck_prompt']
deck_prompt_soup = BeautifulSoup(slide_page(deck_prompt['number']).read_text(), 'html.parser')
assert required(deck_prompt_soup, '#prompt-en').get_text() == 'Only focus on information that is relevant to English teachers.'
assert 'Write in English.' not in required(info_prompt_soup, '#prompt-en').get_text()
assert 'Write in English.' not in required(deck_prompt_soup, '#prompt-en').get_text()

manifest = json.loads((SITE / 'manus-routes.json').read_text())
assert len(manifest['routes']) == slide_count + prompt_count + 1
for route in manifest['routes']:
    assert (SITE / (route['path'].lstrip('/') + 'index.html')).is_file(), route

prompt_index_soup = soup_for_slide_kind('prompt-index')
assert len(prompt_index_soup.select('#prompt-index li a')) == prompt_count
format_soup = soup_for_slide_kind('format')
assert len(format_soup.select('table th')) == 4
assert 'Write in English' not in required(format_soup, 'main').get_text()
explore_soup = soup_for_slide_kind('explore-activity')
assert required(explore_soup, 'h1').get_text(' ', strip=True).startswith('Try Explore. Find more relevant sources.')
assert '探索' not in required(explore_soup, 'h1').get_text()
practice_soup = soup_for_slide_kind('practice')
assert 'Check one important claim' not in required(practice_soup, 'main').get_text()
resources = BeautifulSoup((SITE / 'resources/index.html').read_text(), 'html.parser')
resources_text = required(resources, 'main').get_text(' ', strip=True)
for removed_link in ['EDB Blueprint & supplement resource page', 'HKDSE assessment framework index', 'EDB English curriculum documents', 'Desmond EdTech teacher playlist']:
    assert removed_link not in resources_text, removed_link
assert len(resources.select('.resource-group:last-of-type .button-row a')) == 2
assert f'current supplied file: {presentation_slide_count} slides' in resources_text

home = BeautifulSoup((SITE / 'index.html').read_text(), 'html.parser')
assert required(home, '.page-heading .eyebrow').get_text(' ', strip=True) == 'HKMA K S LO COLLEGE'
assert required(home, '.presenter-credit').get_text(' ', strip=True) == 'Presented by Ken Kum'
crest = required(home, '.brand img')
assert crest.get('src') == 'assets/school-logo.png'
assert crest.get('alt') == 'HKMA K S Lo College school crest'
assert required(home, 'link[rel=icon]').get('href') == 'assets/school-logo.png'
social_url = 'https://hkmakslo.github.io/tie-261013/assets/workshop-social-school-20261012.jpg'
for property_name, expected in [
    ('og:image', social_url),
    ('og:image:secure_url', social_url),
    ('og:image:type', 'image/jpeg'),
    ('og:image:width', '1200'),
    ('og:image:height', '630'),
]:
    tag = home.find('meta', attrs={'property': property_name})
    assert tag and tag.get('content') == expected, property_name
for name, expected in [('twitter:card', 'summary_large_image'), ('twitter:image', social_url)]:
    tag = home.find('meta', attrs={'name': name})
    assert tag and tag.get('content') == expected, name
with Image.open(SITE / 'assets/workshop-social-school-20261012.jpg') as social_card:
    assert social_card.size == (1200, 630)
print(f'PASS: {slide_count} faithful slide pages, {prompt_count} bilingual prompt pages, resources, data-driven navigation, Studio examples, original downloads, and social metadata verified. Supplied PowerPoint currently contains {presentation_slide_count} slides.')
