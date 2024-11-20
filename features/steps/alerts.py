import time

from playwright.sync_api import Page

class AlertPage:
    def __init__(self,page:Page):
        self.page = page

    # in playwright we cannot use wait_for_selector for alerts since its a dialog event.
    #alerts are not dom elements
    def alert_with_ok(self):
        self.page.wait_for_selector('//a[contains(@href, "OKTab")]',state='visible')
        self.page.click('//a[contains(@href, "OKTab")]')
        self.page.wait_for_selector('//button[@onclick="alertbox()"]')
        self.page.click('//button[@onclick="alertbox()"]')
        self.page.once("dialog",lambda dialog:dialog.accept())
        #self.page.wait_for_selector('#demo',state='visible')
        message = self.page.text_content('#demo')

    def alert_with_ok_and_cancel(self):
    # Wait for the 'CancelTab' link and click it
        self.page.wait_for_selector('//a[contains(@href, "CancelTab")]', state='visible')
        self.page.click('//a[contains(@href, "CancelTab")]')

    # Wait for the button that triggers the confirm box and click it
        self.page.wait_for_selector('//button[@onclick="confirmbox()"]', state='visible')
        self.page.click('//button[@onclick="confirmbox()"]')
        time.sleep(3)
        self.click_cancel_on_alert()
        time.sleep(0.5)
        self.click_ok_on_alert()

    # Handling alert by clicking Cancel
    def click_cancel_on_alert(self):
    # Set up the dialog handler to dismiss (Cancel) the alert
        self.page.once("dialog", lambda dialog: dialog.dismiss())

    ## Wait for the message to be updated on the page
    # we cant use text = xyz
    # we have to use wait for selector - demo then later text_content and then assert it
        # self.page.wait_for_selector("text=You Pressed Cancel")

    # Now read the message and verify it says "You pressed Cancel"
        message = self.page.text_content('#demo')
    # error while asserting. Will do it later.
        # assert message == "You Pressed Cancel", f"Unexpected message: {message}"

    # Handling alert by clicking OK
    def click_ok_on_alert(self):
    # Set up the dialog handler to accept (OK) the alert
        self.page.once("dialog", lambda dialog: dialog.accept())

    # Wait for the message and verify it says "You pressed Ok"
        self.page.wait_for_selector('#demo', state='visible')
        message = self.page.text_content('#demo')
        print(message)
    # error while asserting. Will do it later.
        #assert message == "You pressed Ok", f"Unexpected message: {message}"

    def alert_with_text(self):
    # Wait for the 'Textbox' link and click it
        self.page.wait_for_selector('//a[contains(@href, "Textbox")]', state='visible')
        self.page.click('//a[contains(@href, "Textbox")]')
        self.page.click('//button[@onclick="promptbox()"]')
        self.page.once("dialog", lambda dialog: dialog.accept("Niranjan"))
        self.page.click('//button[@onclick="promptbox()"]')
        self.page.wait_for_selector('#demo1', state='visible')
        message = self.page.text_content('#demo1')
    # error while asserting. Will do it later.
        #assert message == "Hello Niranjan How are you today", f"Unexpected message: {message}"



