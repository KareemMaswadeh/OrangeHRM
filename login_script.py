from playwright.sync_api import sync_playwright
from config import URL, USERNAME, PASSWORD
from selectors import USERNAME_SELECTOR, PASSWORD_SELECTOR, LOGIN_BUTTON_SELECTOR
from utils import wait_and_type

def login_to_site():
    with sync_playwright() as playwright:

        # Launch a Chromium browser
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the URL from config
        page.goto(URL)

        # Fill in the username and password
        wait_and_type(page, USERNAME_SELECTOR, USERNAME)
        wait_and_type(page, PASSWORD_SELECTOR, PASSWORD)

        # Click the login button
        login_button = page.wait_for_selector(LOGIN_BUTTON_SELECTOR)
        login_button.click()

        # Wait for 3 seconds after login
        page.wait_for_timeout(3000)

        # Close the browser
        browser.close()