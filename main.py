import sys
from time import sleep
import itertools
from numpy.random import choice
import os
 
path = os.path.abspath("dic.txt")

with open(path, 'r', encoding='utf-8') as word_file:
    english_words = set(word.strip() for word in word_file)

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 9, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 3, "Z": 1}

tile_probability = {'A': 0.09, 'B': 0.02, 'C': 0.02, 'D': 0.04, 'E': 0.12, 'F': 0.02, 'G': 0.03, 'H': 0.02, 'I': 0.09, 'J': 0.01, 'K': 0.01, 'L': 0.04, 'M': 0.02, 'N': 0.06, 'O': 0.09, 'P': 0.02, 'Q': 0.01, 'R': 0.06, 'S': 0.04, 'T': 0.06, 'U': 0.04, 'V': 0.02, 'W': 0.02, 'X': 0.01, 'Y': 0.03, 'Z': 0.01}

greetings = 'Hello! Welcome to Word Play!\n'
greetings_block_1 = "\nYou are a word enthusiast from Fancy Town and it is your life goal to take on the Dark Lord who has been terrorizing your village for quite some times. The Dark Lord is powerful and evil, however, his ego is his weakness. You plan to challenge him to a Guess the Word game and beat him in public." 

greetings_block_2 = "\nTo prepare yourself for the big battle, you come to the town's Word Master to ask for his opinion. His grandson, The Kid, is cheeky and smart, he sometimes interupts people who come to see his grandfather." 

available_characters = """
Choose your opponent: 
    - The Kid is fast but he plays mostly short words
    - The Word Master is wise but slow, he sometimes falls asleep and has to skip a turn, but his words are intricate.
    - Random to let the computer choose for you.\n
    """

negative = ['You think I am silly, don\'t you?', 'You just made that up, didn\'t you?', 'Is that all you got?', 'Lame effort. Hahaha', 'I thought you were better than that.']

positive = ['That\'s brilliant!', 'You\'re very clever!', 'No wonder the people of Fancy Town think so highly of you', 'Well played!', 'A worthy opponent!']

encourge = ['Now give it another go', 'Your are better than that', 'Don\'t give up!']

skip = ['I don\'t know, this is too much for me!', 'Hmmmm... I have no answers', 'I must have fallen asleep. I\'ll have to skip']

trick_bag = ['Skip']

class Character():
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rack = []

    def __repr__(self): 
        return self.name

    def __str__(self):
        return self.name

class Computer(Character):
    def __init__(self, name):
        super().__init__(name)
        if self.name == 'The Kid': 
            self.word_length = [3, 4]
        else: 
            self.word_length = [5, 6, 7]

    def play(self):
        for num in sorted(self.word_length, reverse = True):
            words_to_test= []
            group_number = num
            letter_combinations = list(itertools.permutations(self.rack, group_number))
            for combination in letter_combinations:
                words_to_test.append(''.join(combination))
            for word in words_to_test: 
                if word in english_words:
                    print(f'{self.name} played {word}')
                    return word
        return None

    def response(self, tone):
        """This function picks a random response to the opponent's word from a list of positive responses

        Returns:
            _int_: a phrase chosen at random
        """    
        if tone == 'positive':
            message = choice(positive) + '\n'
        elif tone == 'negative': 
            message = choice(negative) + '\n' + 'Try again\n'
        else: 
            message = choice(skip) + '\n'
        Game.typewriter(self, message)
        
class Word: 
    def __init__(self, word):
        self.word = word
    
    def verify(self, rack):
        """This function checks if a word only contains letters from the rack AND if it is a valid English word

        Args:
            word (_str_): the word to be checked
            rack (_list_): the rack where tiles are used from
        
        Returns: 
            _bool_: true if the word uses only words from the rack AND it is a valid English word. false if any of the conditions is false.
        """    
        false_letters_invalid = set()
        false_letters_too_many = set()
        rack_letter_count = {self.word[i] : rack.count(self.word[i]) for i in range(len(self.word))}
        for letter in self.word:
            if letter not in rack:
                false_letters_invalid.add(letter)
            elif rack_letter_count[letter] > 0: 
                rack_letter_count[letter] -= 1
            else: 
                false_letters_too_many.add(letter)
        if not false_letters_too_many and not false_letters_invalid: 
            if self.word.upper() in english_words:
                print(f'{self.word} is an excellent choice.') 
                return self.word
            else: 
                print(f'{self.word} isn\'t a valid English word.')
                return False
        else: 
            if false_letters_invalid: 
                print(f'{false_letters_invalid} {"is" if len(false_letters_invalid) == 1 else "are"} not in your rack!') 
            if false_letters_too_many: 
                print(f'{false_letters_too_many} {"is" if len(false_letters_invalid) == 1 else "are"} used too many times!')
            return False

class InvalidInput(Exception):
    def __init__(self):
        super().__init__(self)

class KeyboardInterupt(Exception):
    def __init__(self):
        super().__init__(self)
        
class SkipTurn(Exception):
    def __init__(self):
        super().__init__(self)

class HelpRequired(Exception):
    def __init__(self):
        super().__init__(self)
        
class Game: 
    def __init__(self): 
        pass

    def get_input(self, prompt): 
        input_value = input(prompt).lower()
        if input_value == '\quit': 
            raise KeyboardInterrupt
        elif input_value == '\help':
            self.get_help()
            raise HelpRequired
        elif input_value == '\skip':
            raise SkipTurn
        else: 
            return input_value

    def typewriter(self, message):
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.01) if letter != '\n' else sleep(0.1)

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
            self.typewriter('The Kid just run in from outside. He will play with you!\n')
        else: 
            self.typewriter('The Word Master just roused from a siesta. He will take you on.\n')

    def announce_rack(self, player):
        if player.name == 'Human':
            self.typewriter(f'Your rack is: {player.rack}\n')
        else: 
            self.typewriter(f"{player.name}' rack is: {player.rack}\n")

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
        player_choice = str(self.get_input('>>>>')).strip().lower()
        choices = ['The Kid', 'The Word Master']
        if player_choice in kid_name_options: 
            return 'The Kid'
        elif player_choice in master_name_options:
            return 'The Word Master'
        elif player_choice == 'random':
            return choice(choices)
        else: 
            raise InvalidInput

    def get_word(self):
        human_input = self.get_input('>>>')
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
        total_number_of_tiles = sum(tile_bag.values())
        return {letter : tile_bag[letter] / total_number_of_tiles for letter in tile_bag.keys()}

    def deal_tiles(self, player): 
        """This function randomly deals tiles for each player propotionally to the tile's probalibily. Number of tiles is 7 for first play and after each play, it is the difference between 7 and what's left in the rack

        Args: 
            rack(_list_): whose rack to deal tiles to 
            
        Returns:
            __list__: player's rack 
        """   
        letters = list(self.tile_probability().keys())
        probabilities = list(self.tile_probability().values())
        # number_of_tiles = 7 - len(player.rack)
        player.rack = choice(letters, 7,p=probabilities, replace = True)
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
            points += letter_values[letter]
        return points

    def play(self):
        self.typewriter(greetings)
        self.announce_blocks(greetings_block_1)
        self.announce_blocks(greetings_block_2)
        self.typewriter(available_characters)
        human_player = Character('Human')
        players = [human_player]
        try:
            while True:
                try:  
                    player_choice = self.choose_character()
                except InvalidInput: 
                    print('Please choose a valid opponent ("Kid", "Master" or "Random"):')
                else:
                    if player_choice: 
                        computer_player = Computer(player_choice)
                        players.append(computer_player)
                        break
            self.announce_player(computer_player)
            for i in range(1, 8):
                print('------------------------------------------------------------')
                print('Round ', i)
                self.announce_scores(players)
                for player in players:
                    player.rack = self.deal_tiles(player)
                    self.announce_rack(player)
                self.announce_turn()
                while True:
                    try:
                        human_word = self.get_word()
                    except HelpRequired:
                        continue
                    except SkipTurn: 
                        human_word = '####' 
                        print('You chose to skip.')
                        break
                    else: 
                        word = Word(human_word)
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
            print('Okay! Come back when you are ready!')

game = Game()
game.play()

