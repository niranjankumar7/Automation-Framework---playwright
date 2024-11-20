from playwright.sync_api import sync_playwright

def before_all(context):
    # Start Playwright and launch the browser before all scenarios
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)

def after_all(context):
    # Stop Playwright and close the browser after all scenarios
    context.browser.close()
    context.playwright.stop()

# Dismiss the consent dialog before clicking the radio button
def handle_consent(context):
    try:
        # Wait for the consent button to be visible and click it
        context.page.wait_for_selector('//button[@aria-label="Consent"]', state='visible')
        context.page.click('//button[@aria-label="Consent"]')
        # You can also wait for the button to disappear if necessary
        context.page.wait_for_selector('//button[@aria-label="Consent"]', state='hidden')
    except Exception:
        # If no consent button is present, continue without error
        pass

