import time
from datetime import datetime, timedelta

from playwright.sync_api import Page

from features.environment import handle_consent


class SliderPage:
    def __init__(self, page: Page):
        self.page = page

    def handle_slider(self):
        handle_consent(self)
        # Wait for the slider handle to be visible
        self.page.wait_for_selector('.ui-slider-handle', state='visible')

        # Set the left style property of the slider handle to 50%
        self.page.evaluate("document.querySelector('.ui-slider-handle').style.left = '50%';")
        time.sleep(1)
        assert self.page.evaluate("document.querySelector('.ui-slider-handle').style.left") == '50%', "Slider handle not set to 50%"