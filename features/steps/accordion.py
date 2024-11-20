import time

from playwright.sync_api import Page

from features.environment import handle_consent


class AccordionPage:
    def __init__(self,page:Page):
        self.page = page

    def click_accordion(self):
        handle_consent(self)
        self.page.wait_for_selector('//a[contains(@href, "collapse1")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse1"]')== True
        time.sleep(1)
        self.validate_content('//div[@id="collapse1"]', 'Automation Testing API is very simple to read and understand')

        self.page.wait_for_selector('//a[contains(@href, "collapse2")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse2"]')== False
        self.page.click('//a[contains(@href, "collapse2")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse2"]',state='visible')
        assert self.page.is_visible('//div[@id="collapse2"]')== True
        self.validate_content('//div[@id="collapse2"]', 'In this Automation tool')

        self.page.wait_for_selector('//a[contains(@href, "collapse3")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse3"]')== False
        self.page.click('//a[contains(@href, "collapse3")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse3"]',state='visible')
        assert self.page.is_visible('//div[@id="collapse3"]')== True
        self.validate_content('//div[@id="collapse3"]', 'you can write the code')

        self.page.wait_for_selector('//a[contains(@href, "collapse4")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse4"]')== False
        self.page.click('//a[contains(@href, "collapse4")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse4"]',state='visible')
        assert self.page.is_visible('//div[@id="collapse4"]')== True
        self.validate_content('//div[@id="collapse4"]', ' the most popular browsers including ')

    def close_accordion(self):
        # write code to check if collapse2,3,4 are open and close them
        self.page.wait_for_selector('//a[contains(@href, "collapse1")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse1"]')== True
        self.page.click('//a[contains(@href, "collapse1")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse1"]',state='hidden')
        assert self.page.is_visible('//div[@id="collapse1"]')== False

        self.page.wait_for_selector('//a[contains(@href, "collapse2")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse2"]')== True
        self.page.click('//a[contains(@href, "collapse2")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse2"]',state='hidden')
        assert self.page.is_visible('//div[@id="collapse2"]')== False

        self.page.wait_for_selector('//a[contains(@href, "collapse3")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse3"]')== True
        self.page.click('//a[contains(@href, "collapse3")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse3"]',state='hidden')
        assert self.page.is_visible('//div[@id="collapse3"]')== False

        self.page.wait_for_selector('//a[contains(@href, "collapse4")]',state='visible')
        assert self.page.is_visible('//div[@id="collapse4"]')== True
        self.page.click('//a[contains(@href, "collapse4")]')
        time.sleep(1)
        self.page.wait_for_selector('//div[@id="collapse4"]',state='hidden')
        assert self.page.is_visible('//div[@id="collapse4"]')== False

    def validate_content(self, xpath, expected_text):
        handle_consent(self)
        self.page.wait_for_selector(xpath, state='visible')
        # inner text will handle finding the element and getting the text
        actual_text = self.page.inner_text(xpath)
        assert expected_text.strip() in actual_text.strip(), f"Expected text is not in the actual text. Actual text is {actual_text}"