from PIL import Image
import pyautogui
from pytesseract import pytesseract

debug_screenshot_latest_file_name = 'latest_screenshot.png'
debug_screenshots_folder = 'debug-screenshots/'
screenshot_latest_start_game_file_name = 'latest_start_game_screenshot_file_name.png'


class Image_Reader:
    def __init__(self):
        self._natural_language = 'eng'

        tesseract_windows_path_folder = 'D:\\Program Files\\Tesseract-OCR\\'
        tesseract_windows_path_file = 'tesseract.exe'
        self._tesseract_windows_path = '{}{}'.format(
            tesseract_windows_path_folder,
            tesseract_windows_path_file
        )

    def extract_text(self, image_path):
        opened_image_file = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(
            opened_image_file,
            lang=self._natural_language
        )
        return extracted_text


class Game_Instance(object):
    def __init__(self):
        self._full_screen_height = 1080
        self._full_screen_width = 1920
        self._game_title = 'One Step From Eden'
        self._keyboard_action_confirm_press = 'q'
        self._time_seconds_delay_to_take_control = 2

    def get_delay_to_take_control(self):
        return self._time_seconds_delay_to_take_control

    def get_game_title(self):
        return self._game_title

    def get_keyboard_action_confirm_press(self):
        return self._keyboard_action_confirm_press

    def get_prompt_is_game_open(self):
        return 'Is {} open? y/n'.format(self._game_title)

    def get_retry_message_when_game_is_closed(self):
        return 'Open the game {}, then try again.'.format(self._game_title)

    def get_start_message_when_game_is_open(self):
        return 'Watch me play {}.'.format(self._game_title)

    def wait_for_user_to_focus_on_the_game(self):
        pyautogui.sleep(self.get_delay_to_take_control())

    def play_game(self, image_reader):
        '''
        Choose the current option by pressing the confirm button.
        '''
        print('Begin playing')

        # Look at the current state of the game.
        screenshot_path = '{}/{}'.format(
            debug_screenshots_folder,
            screenshot_latest_start_game_file_name
        )
        pyautogui.screenshot(screenshot_path)

        extracted_text = image_reader.extract_text(screenshot_path)
        print('Words on screen: {}'.format(extracted_text))

        # Assume game is in focus and option 'Single Player' is highlighted.
        pyautogui.press(self.get_keyboard_action_confirm_press())

        print('Finish playing')

    def is_response_yes(self, response):
        return response.lower() != 'y'


def main():
    # Copy over values from game properties.
    game_instance = Game_Instance()

    prompt_message = game_instance.get_prompt_is_game_open()
    response = input(prompt_message)

    if game_instance.is_response_yes(response):
        response_message = game_instance.get_retry_message_when_game_is_closed()
        print(response_message)
        return

    response_message = game_instance.get_start_message_when_game_is_open()
    print(response_message)

    image_reader = Image_Reader()

    game_instance.wait_for_user_to_focus_on_the_game()

    game_instance.play_game(image_reader)


if __name__ == '__main__':
    main()

    # Take a screenshot of right before where the application ended.
    # Then pause before closing the script for debugging purposes.
    image = pyautogui.screenshot(
        '{}/{}'.format(
            debug_screenshots_folder,
            debug_screenshot_latest_file_name
        )
    )
    input()
