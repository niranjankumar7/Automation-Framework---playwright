import time
from datetime import datetime, timedelta

from playwright.sync_api import Page

from features.environment import handle_consent


class DatepickerPage:
    def __init__(self,page:Page):
        self.page = page

    def date_picker(self):
        handle_consent(self)
        today = datetime.today().strftime('%m/%d/%Y')
        # write code to verify the disabled datepicker
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%m/%d/%Y')
        #self.page.wait_for_selector('//input[@id="datepicker1"]',state='visible')
        #self.page.click('//input[@id="datepicker1"]')
        #self.page.fill('//input[@id="datepicker1"]', today)
        #time.sleep(1)
        self.page.click('//input[@id="datepicker2"]')
        self.page.fill('//input[@id="datepicker2"]', yesterday)
        time.sleep(1)
        assert self.page.is_visible('//input[@id="datepicker2"]')== True