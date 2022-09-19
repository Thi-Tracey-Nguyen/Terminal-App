class SkipTurn(Exception): 
    def __init__(self):
        pass

def game_play():
    while True: 
        try: 
            human_word = input('Play an English word: ')
            if human_word.lower() == '\skip':
                raise SkipTurn
        except SkipTurn:
            human_word = '###'
            print('You chose to skip.')
            break
        else: 
            print('Word validation runs')
            break
    print(human_word)
    print('Computer plays')

game_play()