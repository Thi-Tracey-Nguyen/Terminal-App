import random
import itertools
from numpy.random import choice

# dictionary = open("dic.txt").read().splitlines()
human = 'You'
computer = 'Computer'


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 9, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 3, "Z": 1}

tile_probability = {'A': 0.09, 'B': 0.02, 'C': 0.02, 'D': 0.04, 'E': 0.12, 'F': 0.02, 'G': 0.03, 'H': 0.02, 'I': 0.09, 'J': 0.01, 'K': 0.01, 'L': 0.04, 'M': 0.02, 'N': 0.06, 'O': 0.09, 'P': 0.02, 'Q': 0.01, 'R': 0.06, 'S': 0.04, 'T': 0.06, 'U': 0.04, 'V': 0.02, 'W': 0.02, 'X': 0.01, 'Y': 0.03, 'Z': 0.01}

negative = ['You think I am silly, don\'t you?', 'You just made that up, didn\'t you?', 'Is that all you got?', 'Lame effort. Hahaha', 'I thought you were better than that.']

positive = ['That\'s brilliant!', 'You\'re very clever!', 'No wonder the people of Fancy Town think so highly of you', 'Well played!', 'A worthy opponent!']

trick_bag = ['Skip', 'DP', 'TP', 'Hint', 'Confundo']

class Character():
    __available_characters = ['Human', 'The Kid', 'The Word Master']
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rack = []

    def __repr__(self): 
        return self.name


    def __str__(self):
        return self.name

    @classmethod
    def is_valid_character(cls, character): 
        return character in cls.__available_characters

class Human(Character):
    def __init__(self, name):
        super().__init__(name)
        self.trick_bag = ['Skip', 'DP', 'TP', 'Hint', 'Confundo']


    def play(self):
        human_word = input('>>>').upper()
        return human_word

class Computer(Character):
    
    def __init__(self, name):
        super().__init__(name)
        if self.name == 'The Kid': 
            self.word_length = [2, 3, 4]
        else: 
            self.word_length = [5, 6, 7]

    def shuffle_letters(self):
        words_to_test= []
        group_number = random.choice(self.word_length)
        t = list(itertools.permutations(self.rack, group_number))
        for i in range(len(t)):
            words_to_test.append(''.join(t[i]))
        return words_to_test
    
    def play(self):
        word_options = self.shuffle_letters()
        for word in word_options: 
            if word in english_words:
                return f'{self.name} played {word}'

    def response_positive(self):
        """This function picks a random response to the opponent's word from a list of positive responses

        Returns:
            _int_: a phrase chosen at random
        """    
        print(random.choice(positive))
    
    def response_negative(self):
        """This function picks a random response to the opponent's word from a list of negative responses

        Returns:
            _int_: a phrase chosen at random
        """    
        print(random.choice(negative))
    

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
        for i in range(len(self.word)):
            if self.word[i] not in rack:
                false_letters_invalid.add(self.word[i])
            elif rack_letter_count[self.word[i]] > 0: 
                rack_letter_count[self.word[i]] -= 1
            else: 
                false_letters_too_many.add(self.word[i])
        if not false_letters_too_many and not false_letters_invalid: 
            if self.word.upper() in english_words:
                print(f'{self.word} is an excellent choice.') 
                return self.word
            else: 
                print(f'{self.word} isn\'t a valid English word. Try again.')
                return False
        else: 
            if false_letters_invalid: 
                print(f'{false_letters_invalid} {"is" if len(false_letters_invalid) == 1 else "are"} not in your rack!') 
            if false_letters_too_many: 
                print(f'{false_letters_too_many} {"is" if len(false_letters_invalid) == 1 else "are"} used too many times!')
            print('Try again.') 
            return False

        
class Game: 
    def __init__(self): 
        pass

    def greetings(self): 
        print('''Hello! Welcome to Word Play! here are some rules: 
        - you can skip
        - you can get a hint
        - play a valid english word
        ''')

    def announce_rack(self, player):
        if player.name == 'Human':
            print(f'Your rack is: {player.rack}')
        else: 
            print(f'{player.name} rack is: {player.rack}')

    def announce_turn(self):
        print("It's your turn. Goodluck!\nPlay a valid English word.")

    def choose_character(self):
        kid_name_options = ['kid', 'the kid']
        master_name_options = ['master', 'the master', 'word master', 'the word master'] 
        player_choice = input('Choose your opponet: ').title()
        if player_choice in kid_name_options: 
            return 'The Kid'
        elif player_choice in master_name_options:
            return 'The Word Master'
        else: 
            return None

    def get_word(self):
        human_input_word = input('>>>').upper()
        return human_input_word

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
        number_of_tiles = 7 - len(player.rack) 
        player.rack = choice(letters, number_of_tiles,p=probabilities, replace=False)
        return list(player.rack)

    def remove_tiles(self, small_collection, large_collection): 
        # if not isinstance(small_collection, str): 
        #     small_collection = list(small_collection)
        for tile in small_collection: 
            large_collection.remove(tile)
        return large_collection

    def calculate_points(self, word):
        """This function calculates points based on the word played

        Args:
            word (_str_): word played by the player
        Returns:
            _int_: points
        """   
        points = 0
        for i in range(len(word)): 
            points += letter_values[word[i]]
        return points

    def play(self):
        self.greetings()
        human_player = Human('Human')
        players = [human_player]
        while True: 
            player_choice = self.choose_character()
            if Computer(player_choice):
                computer_player = Computer(player_choice)
                players.append(computer_player)
                break
        
        # for player in player_choice:
        #     if player == 'Human': 
        #         human_player = Human(player)
        #         characters.append(human_player)
        #     else: 
        #         while True:
        #         computer_player = Computer(player)
        #         characters.append(computer_player)
        # print(characters)
        # print(computer_player)
        # for i in range(1, 8):
        #     print('Round ', i)
        #     for player in characters:
        #         player.rack += self.deal_tiles(player)
        #         self.announce_rack(player)
        #     self.announce_turn()
        #     while True:
        #         human_word = self.get_word()
        #         word = Word(human_word)
        #         is_verified = word.verify(human_player.rack)
        #         if is_verified:
        #             self.remove_tiles(word.word, human_player.rack)
        #             print(human_player.rack)
        #             break
        #     if is_verified:
        #         computer_player.response_positive()
        #     else: 
        #         computer_player.response_negative()
        #     print(computer_player.play())


game = Game()
game.play()

