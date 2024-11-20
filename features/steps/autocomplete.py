import time

from playwright.sync_api import Page

from features.environment import handle_consent


class AutoCompletePage:
    def __init__(self,page:Page):
        self.page = page

    def auto_complete(self):
        handle_consent(self)
        self.page.wait_for_selector('//input[@id="searchbox"]',state='visible')
        time.sleep(1)
        self.page.fill('//input[@id="searchbox"]','ind')
        time.sleep(1)
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        time.sleep(1)
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        time.sleep(1)
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        self.page.press('//input[@id="searchbox"]','Enter')
        time.sleep(1)
        india_selected = self.page.is_visible('.ui-autocomplete-multiselect-item:has-text("India")')
        assert india_selected, "India was not selected"

        self.page.wait_for_selector('//input[@id="searchbox"]',state='visible')
        time.sleep(1)
        self.page.fill('//input[@id="searchbox"]','united')
        time.sleep(1)
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        self.page.press('//input[@id="searchbox"]','ArrowDown')
        time.sleep(1)
        self.page.press('//input[@id="searchbox"]','Enter')
        time.sleep(1)
        usa_selected = self.page.is_visible('.ui-autocomplete-multiselect-item:has-text("United States")')
        assert usa_selected, "USA was not selected"
        time.sleep(1)
        self.page.click('.ui-icon.ui-icon-close')