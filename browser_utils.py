# browser_utils.py
from playwright.sync_api import sync_playwright

def launch_browser(p):
    browser = p.chromium.launch(headless=False)
    return browser

def navigate_to_page(browser, link):
    page = browser.new_page()
    page.goto(link)
    page.wait_for_load_state()
    return page