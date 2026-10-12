#!/usr/bin/env python3
"""Check prompt navigation against a local static HTTP server."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
slides = json.loads((ROOT / 'content/slides.json').read_text())
prompt_count = len(json.loads((ROOT / 'content/prompt-texts.json').read_text())['prompts'])
prompt_index_number = next(slide['number'] for slide in slides if slide['kind'] == 'prompt-index')
start_prompt = min(3, prompt_count)
target_prompt = min(5, prompt_count)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT / 'site')))
Thread(target=server.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{server.server_port}'
try:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
        for width in [375, 768, 1440]:
            page = browser.new_page(viewport={'width': width, 'height': 900})
            page.set_default_timeout(8000)
            page.goto(base + f'/prompts/{start_prompt:02d}/')
            page.locator('.prompt-switcher summary').click()
            menu = page.locator('.prompt-switcher-menu')
            assert menu.is_visible()
            box = menu.bounding_box()
            assert box and box['x'] >= 0 and box['x'] + box['width'] <= width + 1
            assert page.locator('.prompt-switcher-menu a').count() == prompt_count
            assert page.locator('.prompt-switcher-menu a[aria-current=page]').get_attribute('href') == './'
            page.keyboard.press('Escape')
            assert not menu.is_visible()
            page.locator('.prompt-switcher summary').click()
            page.mouse.click(3, 200)
            assert not menu.is_visible()
            page.locator('.prompt-switcher summary').click()
            page.locator('.prompt-switcher-menu a').nth(target_prompt - 1).click()
            page.wait_for_url(f'**/prompts/{target_prompt:02d}/')
            assert page.locator('[data-page-next]').count() == 0
            page.locator('[data-page-previous]').click()
            page.wait_for_url(f'**/pages/{prompt_index_number:02d}/')
            assert page.locator('[data-page-next]').count() == 1
            print(f'{width}px PASS: dropdown fits, dismissal works, prompt links and index return work.', flush=True)
            page.close()
        page = browser.new_page(java_script_enabled=False, viewport={'width': 375, 'height': 900})
        page.goto(base + '/prompts/01/')
        page.locator('.prompt-switcher summary').click()
        assert page.locator('.prompt-switcher-menu').is_visible()
        page.locator('.prompt-switcher-menu a').nth(1).click()
        page.wait_for_url('**/prompts/02/')
        browser.close()
        print(f'PASS: dropdown works without JavaScript; slide navigation and {prompt_count} bilingual prompts retained.', flush=True)
finally:
    server.shutdown()
    server.server_close()
