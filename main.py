class Game_Instance(object):
    def __init__(self):
        self._game_title = 'One Step From Eden'
    
    def get_game_title(self):
        return self._game_title
    
    def get_prompt_is_game_open(self):
        return 'Is {} open? y/n'.format(self._game_title)
    
    def get_retry_message_when_game_is_closed(self):
        return 'Open the game {}, then try again.'.format(self._game_title)
    
    def get_start_message_when_game_is_open(self):
        return 'Watch me play {}.'.format(self._game_title)
    
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

if __name__ == '__main__':
    main()

    # Pause before closing the script for debugging purposes.
    input()
