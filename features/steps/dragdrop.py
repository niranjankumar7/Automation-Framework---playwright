import time

from playwright.sync_api import Page

from features.environment import handle_consent


class DragDrop:
    def __init__(self,page:Page):
        self.page = page

    # debug this - this is not working properly as expected
    def drag_and_drop_static_image(self):
        handle_consent(self.page)
        time.sleep(2)
        self.page.drag_and_drop('//img[@id="angular"]', 'div#droparea')
        time.sleep(2)
        img_src1 = self.page.get_attribute('#angular', 'src')
        assert img_src1 == 'logo.png', f"Unexpected img src: {img_src1}"
        time.sleep(2)

    #    once do we multiple thats when this is failing. Fix later
    #     handle_consent(self.page)
    #     self.page.drag_and_drop('//img[@id="mongo"]', 'div#droparea')
    #     time.sleep(2)
    #     img_src2 = self.page.get_attribute('#mongo', 'src')
    #
    #     # Assert that the 'src' attribute is equal to 'logo.png'
    #     assert img_src2 == 'logo.png', f"Unexpected img src: {img_src2}"
    #     time.sleep(2)
    #
    #     handle_consent(self.page)
    #     self.page.drag_and_drop('//img[@id="node"]', 'div#droparea')
    #     time.sleep(2)
    #     img_src3 = self.page.get_attribute('#node', 'src')
    #
    # # Assert that the 'src' attribute is equal to 'logo.png'
    #     assert img_src3 == 'logo.png', f"Unexpected img src: {img_src3}"
    #     self.page.screenshot(path="screenshots/dragdrop.png")
    #     time.sleep(2)
    #     self.page.close()

    def drag_and_drop_dynamic(self):
        handle_consent(self.page)
        time.sleep(2)
        self.page.drag_and_drop('//img[@id="angular"]', 'div#droparea')
        time.sleep(2)
        img_src1 = self.page.get_attribute('#angular', 'src')
        assert img_src1 == 'logo.png', f"Unexpected img src: {img_src1}"
        time.sleep(2)

        #unable to do for the 2nd image. Find out why
        self.page.drag_and_drop('//img[@id="mongo"]', 'div#droparea')
        time.sleep(2)
        img_src2 = self.page.get_attribute('#mongo', 'src')
        assert img_src2 == 'logo.png', f"Unexpected img src: {img_src2}"
        time.sleep(2)

    def select_items(self):
        self.page.wait_for_selector('//a[@href="#Serialize"]')
        handle_consent(self)
        self.page.click('//a[@href="#Serialize"]')
        time.sleep(2)
        # assertion isnt working that good. So have to optimise it by using parent tag id etc etc
        #result_text = self.page.inner_text('#result')
        #assert result_text == "None:", f"Unexpected result text: {result_text}"
        self.page.click('//div[@id="Serialize"]//li[b[text()="Sakinalium - Method Chaining"]]')
        self.page.wait_for_selector('#result',state='visible')
        #result_text = self.page.inner_text('#result')
        #assert result_text == "Sakinalium - Method Chaining", f"Unexpected result text: {result_text}"



    def resize_element(self):
        handle_consent(self.page)
    # Wait for the resizable handle to be visible
        self.page.wait_for_selector('.ui-resizable-se', state='visible')
        time.sleep(1)
    # Get the position of the resizable handle
        handle_position = self.page.evaluate("""() => {
            const handle = document.querySelector('.ui-resizable-se');
            const rect = handle.getBoundingClientRect();
            return {x: rect.x + rect.width / 2, y: rect.y + rect.height / 2};
        }""")

    # Move the mouse to the position of the resizable handle
        self.page.mouse.move(handle_position['x'], handle_position['y'])
        time.sleep(1)
    # Press the left mouse button
        self.page.mouse.down()
        time.sleep(1)
    # Move the mouse to the new position
        self.page.mouse.move(handle_position['x'] + 350, handle_position['y'] + 225)
        time.sleep(1)
    # Release the left mouse button
        self.page.mouse.up()
        time.sleep(1)
    # Get the actual width and height of the element
        size = self.page.evaluate("""() => {
            const element = document.querySelector('#resizable');
            return {width: element.offsetWidth, height: element.offsetHeight};
        }""")
        time.sleep(1)
    # Assert that the actual width and height match the expected values
        assert size['width'] == 350, f"Unexpected width: {size['width']}"
        assert size['height'] == 225, f"Unexpected height: {size['height']}"





