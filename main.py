def main():
    game_title = 'One Step From Eden'

    response = input('Is {} open? y/n'.format(game_title))

    if response.lower() != 'y':
        print('Open the game {}, then try again.'.format(game_title))
        return

    print('Watch me play {}.'.format(game_title))

if __name__ == '__main__':
    main()

    # Pause before closing the script for debugging purposes.
    input()
