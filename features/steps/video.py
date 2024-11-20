import time

from features.environment import handle_consent


class VideoPage:
    def __init__(self, page):
        self.page = page

    # have to fix the xpath and the selector properly
    def click_play(self):
        handle_consent(self)
        self.page.click('//video[@tabindex="-1"]')  # Replace with the actual selector of the play button
        time.sleep(4)

    def click_pause(self):
        time.sleep(1)
        self.page.click('#pause-button-selector')
        self.page.wait_for_selector('button.ytp-play-button')

    # Find the play/pause button and click it
        play_button = self.page.locator('button.ytp-play-button')
        play_button.click()# Replace with the actual selector of the pause button

    def is_playing(self):
        # Replace with the actual logic to check if the video is playing
        pass

    def click_fullscreen(self):
        self.page.click('#ytp-fullscreen-button[1]')  # Replace with the actual selector of the fullscreen button

    def exit_fullscreen(self):
        # Replace with the actual logic to exit fullscreen mode
        self.click_fullscreen()
        pass
