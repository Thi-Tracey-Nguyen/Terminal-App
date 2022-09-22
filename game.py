import random
from numpy import random as nur
import data as d
import word as w
import exceptions as ex
import character as ch
        
class Game: 
    def __init__(self): 
        pass

    def get_input(self, prompt): 
        input_value = input(prompt).lower()
        if input_value == '\quit': 
            raise ex.KeyboardInterrupt
        elif input_value == '\help':
            self.get_help()
            raise ex.HelpRequired
        elif input_value == '\skip':
            raise ex.SkipTurn
        else: 
            return input_value

    def announce_blocks(self, message):
        sleep(0.5)
        print(message)
        sleep(0.5)

    def get_help(self): 
        print("""Valid keyboard inputs are:
        * \Help to see this message again
        * \Quit to quit at any point of the game
        * \Skip to skip your turn
        """)

    def announce_player(self, player):
        if player.name == 'The Kid':
            d.typewriter('The Kid just run in from outside. He will play with you!\n')
        else: 
            d.typewriter('The Word Master just roused from a siesta. He will take you on.\n')

    def announce_rack(self, player):
        if player.name == 'Human':
            d.typewriter(f'Your rack is: {player.rack}\n')
        else: 
            d.typewriter(f"{player.name}' rack is: {player.rack}\n")

    def announce_turn(self):
        print("It's your turn. Goodluck!\nPlay an English word.")
        print("""***Type \help to get help at any time***""")

    def announce_scores(self, list_of_players):
        s = "'s"
        for player in list_of_players:
            print(f"{player.name + s if player.name != 'Human' else 'Your'} {'point is' if player.points <= 0 else 'points are'}: {player.points}.", end = ' ')
        if list_of_players[0].points == list_of_players[1].points == 0: 
            print('Let\'s begin.')
        elif list_of_players[0].points == list_of_players[1].points: 
            print('It\'s a tie.')
        elif list_of_players[0].points > list_of_players[1].points: 
            print('You are in front.')
        else: 
            print(f'{list_of_players[1]} is in front.')

    def announce_end(self, list_of_players):
        s = "'s"
        for player in list_of_players:
            print(f"{player.name + s if player.name != 'Human' else 'Your'} {'point is' if player.points <= 0 else 'points are'}: {player.points}.", end = ' ')
        print('\n')
        if list_of_players[0].points == list_of_players[1].points: 
            print('It\'s a tie. Well done! With a little more training, you will be ready to take on the Dark Lord.')
        elif list_of_players[0].points > list_of_players[1].points: 
            print('You won! I have never met such a competent player. You are ready to battle the Dark Lord.')
        else: 
            print('Solid effort. But you are not ready yet. Go back and train some more.')

    def choose_character(self): 
        kid_name_options = ['kid', 'the kid']
        master_name_options = ['master', 'the master', 'word master', 'the word master'] 
        player_choice = str(self.get_input('>>>>  ')).strip().lower()
        choices = ['The Kid', 'The Word Master']
        if player_choice in kid_name_options: 
            return 'The Kid'
        elif player_choice in master_name_options:
            return 'The Word Master'
        elif player_choice == 'random':
            return random.choice(choices)
        else: 
            raise ex.InvalidInput

    def get_word(self):
        human_input = self.get_input('>>>  ')
        if human_input == '\skip': 
            raise SkipTurn
        else: 
            human_word = human_input
            return human_word.upper()

    def tile_probability(self):
        """This function calculates probabilities of each tile in the bag 

        Returns:
            _dict_: name of tile and its associated probability
        """  
        total_number_of_tiles = sum(d.letter_collection.values())
        return {letter : d.letter_collection[letter] / total_number_of_tiles for letter in d.letter_collection.keys()}

    def deal_letters(self, player): 
        """This function randomly deals tiles for each player propotionally to the tile's probalibily. Number of tiles is 7 for first play and after each play, it is the difference between 7 and what's left in the rack

        Args: 
            rack(_list_): whose rack to deal tiles to 
            
        Returns:
            __list__: player's rack 
        """   
        letters = list(self.tile_probability().keys())
        probabilities = list(self.tile_probability().values())
        # number_of_tiles = 7 - len(player.rack)
        player.rack = nur.choice(letters, 7,p=probabilities, replace = True)
        return list(player.rack)

    def calculate_points(self, word):
        """This function calculates points based on the word played

        Args:
            word (_str_): word played by the player
        Returns:
            _int_: points
        """   
        points = 0
        word = word.strip().upper()
        for letter in word:
            points += d.letter_values[letter]
        return points

    def main(self):
        # self.typewriter(d.greetings)
        # self.announce_blocks(d.greetings_block_1)
        # self.announce_blocks(d.greetings_block_2)
        # self.typewriter(d.available_characters)
        human_player = ch.Character('Human')
        players = [human_player]
        try:
            while True:
                try:  
                    player_choice = self.choose_character()
                except ex.InvalidInput: 
                    print('Please choose a valid opponent ("Kid", "Master" or "Random"):')
                else:
                    if player_choice: 
                        computer_player = ch.Computer(player_choice)
                        players.append(computer_player)
                        break
            self.announce_player(computer_player)
            for i in range(1, 8):
                print('------------------------------------------------------------')
                print('Round ', i)
                self.announce_scores(players)
                for player in players:
                    player.rack = self.deal_letters(player)
                    self.announce_rack(player)
                self.announce_turn()
                while True:
                    try:
                        human_word = self.get_word()
                    except ex.HelpRequired:
                        continue
                    except ex.SkipTurn: 
                        human_word = '####' 
                        print('You chose to skip.')
                        break
                    else: 
                        word = w.Word(human_word)
                        is_verified = word.verify(human_player.rack)
                        if is_verified:
                            human_player.points += self.calculate_points(human_word)
                            computer_player.response('positive')
                            break
                        else:
                            computer_player.response('negative')
                computer_word = computer_player.play()
                if not computer_word: 
                    computer_player.response('skip')
                else: 
                    print(computer_word)
                    computer_player.points += self.calculate_points(computer_word)

            print('------------------------------------------------------------')    
            self.announce_end(players)
        except KeyboardInterrupt:
            print('\nOkay! Come back when you are ready!')

game = Game()
game.main()

if __name__ == '__main__':
    game.main()