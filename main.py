from enum import Enum
from PIL import Image
import pyautogui
from pytesseract import pytesseract

debug_screenshot_latest_file_name = 'latest_screenshot.png'
debug_screenshots_folder = 'debug-screenshots/'
screenshot_current_file_name = 'current.png'


class Game_Scene_One_Step_From_Eden(Enum):
    '''
    Enum to represent each scene within the game One Step From Eden.

    ## Layering Scenes

    - Pressing the `Esc` key usually opens or closes an options scene on top of the current scene.
    - Pressing the `I` key may open or close a deck scene on top of the current scene, outside of combat.
    - Pressing the `Tab` key may open or close a map scene on top of the current scene, outside of combat or after a boss fight.

    Each layered scene combination should have its own enum value.
    '''
    # Scene reached by selecting title option CO-OP.
    cooperative_controls = 'cooperative_controls'

    # Scenes reachable after starting a cooperative game.
    # Copied and tweaked from single player enum values.
    cooperative_gameplay = 'cooperative_gameplay'
    cooperative_gameplay_shop_open = 'cooperative_gameplay_shop_open'
    cooperative_gameplay_training = 'cooperative_gameplay_training'
    cooperative_gameplay_training_map_open = 'cooperative_gameplay_training_map_open'
    cooperative_gameplay_training_options = 'cooperative_gameplay_training_options'
    cooperative_gameplay_training_options_controls = 'cooperative_gameplay_training_options_controls'
    cooperative_gameplay_training_options_settings = 'cooperative_gameplay_training_options_settings'
    cooperative_gameplay_training_options_streaming = 'cooperative_gameplay_training_options_streaming'
    cooperative_gameplay_victory = 'cooperative_gameplay_victory'
    cooperative_gameplay_victory_experience_points = 'cooperative_gameplay_victory_experience_points'
    cooperative_gameplay_victory_take_artifact = 'cooperative_gameplay_victory_take_artifact'
    cooperative_gameplay_victory_take_spell = 'cooperative_gameplay_victory_take_spell'
    cooperative_gameplay_victory_take_spell_deck_open = 'cooperative_gameplay_victory_take_spell_deck_open'

    # Scene reached by selecting title option Library.
    library_spells = 'library_spells'
    library_artifacts = 'library_artifacts'

    # Scenes reached while loading the game that automatically change over time.
    loading_title_1_developer = 'loading_title_developer'
    loading_title_2_publisher = 'loading_title_publisher'
    loading_title_empty = 'loading_title_empty'

    # Scene reached by selecting title option MODS.
    mods = 'mods'

    # Scene reached by selecting title option PATCH NOTES.
    patch_notes = 'patch_notes'

    # Scenes reachable by selecting title option PvP.
    player_versus_player_controls = 'player_versus_player_controls'
    player_versus_player_controls_select_characters = 'player_versus_player_controls_select_characters'

    # Scene reached by selecting title option PROFILE ().
    profile = 'profile'

    # Scenes reachable after starting a single player game.
    single_player_gameplay = 'single_player_gameplay'
    single_player_gameplay_shop_open = 'single_player_gameplay_shop_open'
    single_player_gameplay_training = 'single_player_gameplay_training'
    single_player_gameplay_training_map_open = 'single_player_gameplay_training_map_open'
    single_player_gameplay_training_options = 'single_player_gameplay_training_options'
    single_player_gameplay_training_options_controls = 'single_player_gameplay_training_options_controls'
    single_player_gameplay_training_options_settings = 'single_player_gameplay_training_options_settings'
    single_player_gameplay_training_options_streaming = 'single_player_gameplay_training_options_streaming'
    single_player_gameplay_victory = 'single_player_gameplay_victory'
    single_player_gameplay_victory_experience_points = 'single_player_gameplay_victory_experience_points'
    single_player_gameplay_victory_take_artifact = 'single_player_gameplay_victory_take_artifact'
    single_player_gameplay_victory_take_spell = 'single_player_gameplay_victory_take_spell'
    single_player_gameplay_victory_take_spell_deck_open = 'single_player_gameplay_victory_take_spell_deck_open'

    # Scenes reachable while setting up a single player game.
    single_player_select_character = 'single_player_select_character'
    single_player_select_character_loadout = 'single_player_select_character_loadout'
    single_player_select_character_loadout_difficulty = 'single_player_select_character_loadout_difficulty'
    single_player_select_character_loadout_difficulty_play = 'single_player_select_character_loadout_difficulty_play'
    single_player_start_prompt = 'single_player_start_prompt'

    # Scenes reachable by selecting title option STATS.
    statistics_achievements = 'statistics_achievements'
    statistics_character_1_saffron = 'statistics_character_1_saffron'
    statistics_character_2_reva = 'statistics_character_2_reva'
    statistics_character_3_gunner = 'statistics_character_3_gunner'
    statistics_character_4_selicy = 'statistics_character_4_selicy'
    statistics_character_5_hazel = 'statistics_character_5_hazel'
    statistics_character_6_terra = 'statistics_character_6_terra'
    statistics_character_7_shiso = 'statistics_character_7_shiso'
    statistics_character_8_violette = 'statistics_character_8_violette'
    statistics_character_9_shopkeeper = 'statistics_character_9_shopkeeper'
    statistics_statistics = 'statistics_statistics'

    # Scene reached after fully loading the game.
    title = 'title'
    title_options = 'title_options'

    # Empty value for when a scene is not recognized yet.
    unknown = 'unknown'


class Image_Reader:
    '''
    Reads text from a screenshot input.
    '''

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
    '''
    Stores information about the game to play and how to run the gameplay tool.
    '''

    def __init__(self):
        self._full_screen_height = 1080
        self._full_screen_width = 1920
        self._game_title = 'One Step From Eden'
        self._keyboard_action_confirm_press = 'q'
        self._time_seconds_delay_to_take_control = 2
        self._time_seconds_delay_to_menu_transition = 0.88

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

    def wait_for_menu_navigation(self):
        pyautogui.sleep(self._time_seconds_delay_to_menu_transition)

    def play_game(self, image_reader, game_instance_navigator, game_instance_scene_locator):
        '''
        Choose the current option by pressing the confirm button.
        '''
        print('Begin playing')

        # Look at the current state of the game.
        screenshot_path = '{}/{}'.format(
            debug_screenshots_folder,
            screenshot_current_file_name
        )
        pyautogui.screenshot(screenshot_path)

        is_located_on_title_scene = game_instance_scene_locator.is_scene(
            Game_Scene_One_Step_From_Eden.title,
            screenshot_path
        )

        if is_located_on_title_scene:
            print('Starting on scene {}'.format(
                Game_Scene_One_Step_From_Eden.title)
            )

        extracted_text = image_reader.extract_text(screenshot_path)
        print('Words on screen: {}'.format(extracted_text))

        # Assume game is in focus and option 'Single Player' is highlighted.
        game_instance_navigator.confirm_option(self)

        self.wait_for_menu_navigation()

        pyautogui.screenshot(screenshot_path)

        is_located_on_single_player_select_character_scene = game_instance_scene_locator.is_scene(
            Game_Scene_One_Step_From_Eden.single_player_select_character,
            screenshot_path
        )

        if is_located_on_single_player_select_character_scene:
            print('Ending on scene {}'.format(
                Game_Scene_One_Step_From_Eden.single_player_select_character
            ))

        print('Finish playing')

    def is_response_yes(self, response):
        return response.lower() == 'y'


class Game_Instance_Scene_Locator():
    '''
    Detects which screen of the game is displayed.
    '''

    def __init__(self, game_scene_one_step_from_eden, image_reader):
        self._game_scene_one_step_from_eden = game_scene_one_step_from_eden
        self._image_reader = image_reader
        self._working_scenes = {
            Game_Scene_One_Step_From_Eden.title,
            Game_Scene_One_Step_From_Eden.single_player_select_character,
            Game_Scene_One_Step_From_Eden.single_player_select_character_loadout,
            Game_Scene_One_Step_From_Eden.single_player_select_character_loadout_difficulty
        }

    def _get_expected_text_list(self, scene):
        '''
        Returns a list of strings expected to be read from the chosen scene.

        To Do:
        - Refactor lists into sets for faster performance.
        - Check for visual cues when text detection is too similar.
        '''
        if scene == Game_Scene_One_Step_From_Eden.title:
            return [
                'MODS',
                'PATCH NOTES'
            ]

        if scene == Game_Scene_One_Step_From_Eden.single_player_select_character:
            return [
                'Saffron',
                'Reva',
                'Gunner',
                'Selicy',
                'Hazel',
                'Terra',
                'Shiso',
                'Violette',
                'Shopkeeper',
                'Spells',
                'Artifacts',
                'Weapon',
                # Intentional typo of OUTFIT to match measured value.
                'out FIT'
            ]

        if scene == Game_Scene_One_Step_From_Eden.single_player_select_character_loadout:
            return [
                'Saffron',
                'Reva',
                'Gunner',
                'Selic',
                'Hazel',
                'Terra',
                'Shiso',
                'START',
                'Violette',
                'Shopkeeper',
                'DETAILS',
                'ourent'  # Intentional typo of OUTFIT to match measured value.
            ]

        if scene == Game_Scene_One_Step_From_Eden.single_player_select_character_loadout_difficulty:
            return [
                'Saffron',
                'Reva',
                'Gunner',
                'Selic',
                'Hazel',
                'Terra',
                'START',
                'Shiso',
                'Violette',
                'Shopkeeper'
            ]

        print('Warning, tried to detect expected text in unhandled scene {}.'.format(scene))
        return []

    def _is_scene_handler_defined(self, scene):
        '''
        Returns true if the given scene enum has working code associated to it.
        '''
        if scene in self._working_scenes:
            return True

        return False

    def is_scene(self, scene, screenshot_path):
        '''
        Returns true if the given scene enum is recognized as the
         current screen, based on a screenshot in the given
         screenshot path.
        '''
        # Guardian check if the scene being looked for is coded yet.
        if not self._is_scene_handler_defined(scene):
            print('Warning, tried to detect unhandled scene {}.'.format(scene))
            False

        expected_text_list = self._get_expected_text_list(scene)

        extracted_text = self._image_reader.extract_text(screenshot_path)

        # Zip each fragment of expected text with the text found in the screenshot.
        matches_list = map(
            lambda expected_text: expected_text in extracted_text, expected_text_list)

        found_all_matches = all(matches_list)

        return found_all_matches


class Game_Instance_Navigator():
    '''
    Navigates to another gameplay scene through keypresses and clicks.
    '''

    def confirm_option(self, game_instance):
        '''
        Choose the current option by pressing the confirm button.

        Assume game is in focus and option is highlighted.
        '''
        pyautogui.press(game_instance.get_keyboard_action_confirm_press())


def main():
    '''
    Example function to play the game One Step From Eden on a Windows PC.

    ## Steps Implemented

    1. Prompt the user before starting to play the PC game One Step From Eden.
    2. If yes, wait for a bit so the user can focus on the game, then start playing.
    3. Play by pressing the 'Q' button once.
    '''
    # Copy over values from game properties.
    game_instance = Game_Instance()

    # Guardian check if game is open by asking the user.
    prompt_message = game_instance.get_prompt_is_game_open()
    response = input(prompt_message)

    if not game_instance.is_response_yes(response):
        response_message = game_instance.get_retry_message_when_game_is_closed()
        print(response_message)
        return

    response_message = game_instance.get_start_message_when_game_is_open()
    print(response_message)

    # game_scene = Game_Scene_One_Step_From_Eden()
    game_instance_navigator = Game_Instance_Navigator()
    image_reader = Image_Reader()

    game_instance_scene_locator = Game_Instance_Scene_Locator(
        Game_Scene_One_Step_From_Eden,
        image_reader
    )

    # Wait a short amount of time for the user to focus on the game
    #  application window.
    game_instance.wait_for_user_to_focus_on_the_game()

    game_instance.play_game(
        image_reader,
        game_instance_navigator,
        game_instance_scene_locator
    )


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
