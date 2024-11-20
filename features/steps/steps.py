from features.steps.accordion import AccordionPage
from features.steps.alerts import AlertPage
from features.steps.autocomplete import AutoCompletePage
from features.steps.datepicker import DatepickerPage
from features.steps.dragdrop import DragDrop
from features.steps.slider import SliderPage
from features.steps.video import VideoPage
from login import LoginPage
from register import RegistrationForm
from behave import given, when, then

@given('the user is on the login page')
def user_on_login_page(context):
    # Use the globally initialized browser and Playwright
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Index.html")


@when('the user enters valid email and clicks login')
def user_enters_email_and_clicks_login(context):
    login_page = LoginPage(context.page)
    login_page.login("xyz0020@gmail.com")

@when('the user clicks on the skip sign in button')
def user_clicks_skip_sign_in(context):
    login_page = LoginPage(context.page)
    login_page.skip_sign_in()

@then('the user should be redirected to the registration page')
def user_redirected_to_registration(context):
    context.page.wait_for_url("https://demo.automationtesting.in/Register.html")
    assert context.page.url == "https://demo.automationtesting.in/Register.html"


@given('The user is on registration page')
def user_on_registration_page(context):
    # Use the globally initialized browser and Playwright
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Register.html")


@when("Fill the basic details")
def fill_registration_form(context):
    registration_form = RegistrationForm(context.page)
    registration_form.fill_first_name("Niranjan")
    context.page.wait_for_timeout(1000)
    registration_form.fill_last_name("Kumar")
    context.page.wait_for_timeout(1000)
    registration_form.fill_email("xyz@gmail.com")
    context.page.wait_for_timeout(1000)
    registration_form.fill_address("India")
    context.page.wait_for_timeout(1000)
    registration_form.fill_phone("81919191919")
    registration_form.select_gender()
    context.page.wait_for_timeout(1000)
    registration_form.select_skills()
    context.page.wait_for_timeout(5000)
    registration_form.select_hobbies()
    context.page.wait_for_timeout(5000)
    registration_form.select_country()
    context.page.wait_for_timeout(4000)
    registration_form.select_DOB()
    context.page.wait_for_timeout(4000)
    registration_form.fill_password("first-password","first-password")

@given('The user is on alerts page')
def user_on_alerts(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Alerts.html")

@when('The user handles the alerts')
def user_handling_alerts(context):
    alert_page = AlertPage(context.page)
    alert_page.alert_with_ok()
    alert_page.alert_with_ok_and_cancel()
    alert_page.alert_with_text()

@given('The user is on widgets page acoordion section')
def user_on_widgets(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Accordion.html")

@when('The user handles the widgets accordion')
def user_handling_accordion(context):
    accordion_page = AccordionPage(context.page)
    accordion_page.click_accordion()

@when('The user tries to close the accordion')
def user_closing_accordion(context):
    accordion_page = AccordionPage(context.page)
    accordion_page.close_accordion()

@given('The user is on widgets page autocomplete section')
def user_on_widgets_autocomplete(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/AutoComplete.html")

@when('The user handles the widgets autocomplete')
def user_handling_automcomplete(context):
    autocomplete_page = AutoCompletePage(context.page)
    autocomplete_page.auto_complete()

@given('The user is on widgets page datepicker section')
def user_on_widgets_datepicker(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Datepicker.html")

@when('The user handles the widgets datepicker')
def user_handling_datepicker(context):
    datepicker_page = DatepickerPage(context.page)
    datepicker_page.date_picker()

@given('The user is on widgets page slider section')
def user_on_widgets_slider(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Slider.html")

@when('The user handles the widgets slider')
def user_handling_slider(context):
    slider_page = SliderPage(context.page)
    slider_page.handle_slider()

@given('I am on the drag and drop page static')
def drag_and_drop_page(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Static.html")

@when('I drag and drop the element static')
def drag_and_drop_static(context):
    drag_and_drop_static = DragDrop(context.page)
    drag_and_drop_static.drag_and_drop_static_image()

@given('I am on the drag and drop page dynamic')
def drag_and_drop_page(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Dynamic.html")

@when('I drag and drop the element dynamic')
def drag_and_drop_dynamic(context):
    drag_and_drop_dynamic = DragDrop(context.page)
    drag_and_drop_dynamic.drag_and_drop_dynamic()

@given('I am on the selectable page')
def selectable_page(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Selectable.html")

@when('I select the elements')
def select_items(context):
    select_items = DragDrop(context.page)
    select_items.select_items()

@given('I am on the resizable page')
def resizable_page(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Resizable.html")

@when('I resize the element')
def resize_element(context):
    resize_element = DragDrop(context.page)
    resize_element.resize_element()



@given('The user is on the YouTube video page')
def user_on_youtube_page(context):
    context.page = context.browser.new_page()
    context.page.goto("https://demo.automationtesting.in/Youtube.html")  # Replace with the URL of your YouTube video
    context.video_page = VideoPage(context.page)

@when('The user clicks the play button')
def user_clicks_play(context):
    context.video_page.click_play()

@then('The video should start playing')
def video_starts_playing(context):
    assert context.video_page.is_playing() == True

@when('The user clicks the pause button')
def user_clicks_pause(context):
    context.video_page.click_pause()

@then('The video should pause')
def video_pauses(context):
    assert context.video_page.is_playing() == False

@when('The user clicks the fullscreen button')
def user_clicks_fullscreen(context):
    context.video_page.click_fullscreen()

@then('The video should enter fullscreen mode')
def video_enters_fullscreen(context):
    assert context.video_page.is_fullscreen() == True

@when('The user exits fullscreen mode')
def user_exits_fullscreen(context):
    context.video_page.exit_fullscreen()

@then('The video should exit fullscreen mode')
def video_exits_fullscreen(context):
    assert context.video_page.is_fullscreen() == False


@then('close the browser')
def close_browser(context):
    # No need to close the browser here; it's handled globally in after_all
    pass
