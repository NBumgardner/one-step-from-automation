import pyautogui

debug_screenshot_latest_file_name = 'latest_screenshot.png'
debug_screenshots_folder = 'debug-screenshots/'


class Game_Instance(object):
    def __init__(self):
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

    def play_game(self):
        '''
        Choose the current option by pressing the confirm button.
        '''
        print('Begin playing')

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

    game_instance.wait_for_user_to_focus_on_the_game()

    game_instance.play_game()


if __name__ == '__main__':
    main()

    # Take a screenshot of right before where the application ended.
    # Then pause before closing the script for debugging purposes.
    image = pyautogui.screenshot(
        '{}/{}'.format(debug_screenshots_folder, debug_screenshot_latest_file_name))
    input()
