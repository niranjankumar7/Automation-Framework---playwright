from playwright.sync_api import Page
import time

from features.environment import handle_consent


class RegistrationForm:
    def __init__(self, page: Page):
        self.page = page

    def fill_first_name(self, first_name: str):
        handle_consent(self)
        self.page.wait_for_selector('//input[@placeholder="First Name"]', state='visible')
        self.page.fill('//input[@placeholder="First Name"]', first_name)

    def fill_last_name(self, last_name: str):
        handle_consent(self)
        self.page.fill('//input[@placeholder="Last Name"]', last_name)

    def fill_address(self, address: str):
        handle_consent(self)
        self.page.fill('//textarea[@ng-model="Adress"]', address)

    def fill_email(self, email: str):
        handle_consent(self)
        self.page.fill('//input[@type="email"]', email)

    def fill_phone(self, phone: str):
        handle_consent(self)
        self.page.fill('//input[@type="tel"]', phone)

    def select_gender(self):
        handle_consent(self)
        self.page.click('//input[@value="Male"]')

    def select_hobbies(self):
        handle_consent(self)
        self.page.click('//input[@id="checkbox1"]')

    def select_languages_dropdown(self):
        handle_consent(self)
        self.page.click('//div[@id="msdd"]')
        self.page.click('//a[text()="English"]')
        self.page.click('//a[text()="Hindi"]')
        self.page.click('//a[text()="Japanese"]')
        # can use dynamic xpath by {} to the language

    def select_skills(self):
        handle_consent(self)
    # Wait for the Skills dropdown to be visible and click to open it
        self.page.wait_for_selector('//select[@id="Skills"]', state='visible')

    # Select the option "XML" directly using select_option
        self.page.select_option('//select[@id="Skills"]', 'XML')


    def select_country(self):
    # Handle consent button if it appears
        handle_consent(self)

    # Wait for the 'country' dropdown to be visible
        self.page.wait_for_selector('//select[@id="country"]', state='visible')

    # Select 'India' directly from the dropdown using its value
        self.page.select_option('//select[@id="country"]', 'India')


    def select_DOB(self):
        handle_consent(self)
        self.page.wait_for_selector('//select[@id="yearbox"]',state='visible')
        self.page.select_option('//option[@value="2000"]',state='visible')
        self.page.wait_for_selector('//select[@placeholder="Month"]',state='visible')
        self.page.select_option('//option[@value="November"]', state='visible')
        self.page.wait_for_selector('//select[@id="daybox"]',state='visible')
        self.page.select_option('//option[@value="15"]',state='visible')

    def fill_password(self, first_password : str, second_password:str):
        self.page.fill('//input[@id="firstpassword"]',first_password)
        self.page.fill('//input[@id="secondpassword"]',second_password)

    def submit(self):
        self.page.click('//button[@id="submitbtn"]')

    #def complete_registration(self):
        # Add any additional form filling steps here if necessary
        # time.sleep(3)
