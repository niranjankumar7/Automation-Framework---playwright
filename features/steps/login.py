import time

from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_email(self, email: str):
        self.page.fill('//input[@id="email"]', email)

    def click_login(self):
        self.page.click('//img[@id="enterimg"]')

    def login(self, email: str):
        self.enter_email(email)
        self.click_login()

    def skip_sign_in(self):
        time.sleep(2)
        self.page.click('//button[@id="btn2"]')