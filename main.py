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

negative = ['You think I am silly, don\'t you?', 'You just made that up, didn\'t you?', 'Is that all you got?', 'Lame effort. Hahaha', 'I thought you were better than that.']

positive = ['That\'s brilliant!', 'You\'re very clever!', 'No wonder the people of Fancy Town think so highly of you', 'Well played!', 'A worthy opponent!']

trick_bags = ['shuffle', 'double_score', 'triple_score', 'confundo']

def tile_probability():
    """This function calculates probabilities of each tile in the bag 

    Returns:
        _dict_: name of tile and its associated probability
    """  
    total_number_of_tiles = sum(tile_bag.values())
    return {letter : tile_bag[letter] / total_number_of_tiles for letter in tile_bag.keys()}

letter_probabilities = tile_probability()

group_number = 4

def deal_tiles(rack): 
    """This function randomly deals 5 tiles for each player propotionally to the tile's probalibily

    Args: 
        rack(_list_): whose rack to deal tiles to 
        
    Returns:
        __list__: player's rack 
    """    
    letters = [key for key in letter_probabilities.keys()]
    probabilities = [value for value in letter_probabilities.values()]
    number_of_tiles = 7 - len(rack) 
    rack = choice(letters, number_of_tiles,p=probabilities, replace=False)
    return list(rack)

def shuffle_letters(player_rack):
    words_to_test= []
    # group_number = random.randint(2, 6)
    # print(group_number)
    t = list(itertools.permutations(player_rack, group_number))
    for i in range(len(t)):
        words_to_test.append(''.join(t[i]))
    return words_to_test


def is_english_word(player_word):
    if player_word.upper() in english_words:
        return player_word.upper()


# print(is_english_word(x))

def calculate_points(player, word):
    """This function calculates points based on the word played

    Args:
        word (_str_): word played by the player
    Returns:
        _int_: points
    """   
    points = 0
    for i in range(len(word)): 
        points += letter_values[word[i]]
    # print(f'{player} earned {points} points.') 
    return points

def greetings(): 
    print('''Hello! Welcome to Word Play! here are some rules: 
    - you can skip
    - you can get a hint
    - play a valid english word
    ''')

def response(type):
    """This function picks a random response from a list

    Args:
        type (_list_): collection of phrases

    Returns:
        _int_: a phrase chosen at random
    """    
    print(random.choice(type))
 

def check_within_rack(word, rack):
    """This function checks if all letters in a word are in the player's rack taking into account how many of each letter there is in the rack

    Args:
        word (_type_): player's word
        rack (_type_): player's rack

    Returns:
        _bool_: True if the word used only letters in the rack and do not exceed the available number of each letter
    """    
    false_letters_invalid = set()
    false_letters_too_many = set()
    rack_letter_count = {word[i] : rack.count(word[i]) for i in range(len(word))}
    for i in range(len(word)):
        if word[i] not in rack:
            false_letters_invalid.add(word[i])
        elif rack_letter_count[word[i]] > 0: 
            rack_letter_count[word[i]] -= 1
        else: 
            false_letters_too_many.add(word[i])
    if not false_letters_too_many and not false_letters_invalid: 
        return True
    else: 
        if false_letters_invalid: 
            print(f'{false_letters_invalid} {"is" if len(false_letters_invalid) == 1 else "are"} not in your rack!') 
        if false_letters_too_many: 
            print(f'{false_letters_too_many} {"is" if len(false_letters_invalid) == 1 else "are"} used too many times!') 
        return False

def verify_word(word, rack):
    """This function checks if a word only contains letters from the rack AND if it is a valid English word

    Args:
        word (_str_): the word to be checked
        rack (_list_): the rack where tiles are used from
    
    Returns: 
        _bool_: true if the word uses only words from the rack AND it is a valid English word. false if any of the conditions is false.
    """    
    if check_within_rack(word, rack):
        if is_english_word(word):
            response(positive)
            print(f'{word} is an excellent choice.') 
            return word
        else: 
            response(negative)
            print(f'{word} isn\'t a valid English word. Try again.')
            return False
    else:
        response(negative) 
        print('Try again.')
        return False

def replenish(rack): 
    """This function replishes a player's rack after each round

    Args:
        rack (_list_): partially used player's rack 

    Returns:
        rack (_list_): fully-stocked player's rack
    """    
    number_of_tiles = 7 - len(rack)
    new_tiles = deal_tiles(rack)
    return new_tiles

def human_player_turn():
    human_word = input('>>>').upper()
    return human_word

def human_player(human_rack):
    print("""It's your turn. Goodluck!\nPlay a valid English word.""")
    while True: 
        human_word = human_player_turn()
        verified = verify_word(human_word, human_rack) 
        if verified: 
            return human_word
# Computer play: 
def computer_play(player_rack): 
    for word in shuffle_letters(player_rack): 
      if is_english_word(word):
        print(f'Computer plays {word}.')
        return word

# Removing tiles
def remove_tiles(small_collection, large_collection): 
    if type(small_collection) == str: 
        small_collection = list(small_collection)
    for tile in small_collection: 
        large_collection.remove(tile)
    return large_collection

class Player():
    def __init__(self, name):
        self.name = name
        self.rack = rack
        self.score = score


    def __str__(self):
        return f'Player is {self.name}.'

    def play(self):
        pass




# def game_play(): 
#     greetings()
#     human_rack = []
#     human_points = 0
#     computer_rack = []
#     computer_points = 0

#     for i in range(1,8):
#         print(f'Round {i} ')
#         print(f'Your current points are: {human_points}')
#         print(f'Computer\'s current points are: {computer_points}')
#         human_rack += deal_tiles(human_rack)
#         computer_rack += deal_tiles(computer_rack)
#         print(f'Your rack is: {human_rack}')
#         print(f'Computer rack is: {computer_rack}')
#         human_word = human_player(human_rack)
#         earned_points = calculate_points(human, human_word)
#         print(f'You earned {earned_points} points.')
#         remove_tiles(human_word, human_rack)
#         human_points += earned_points
#         computer_word = computer_play(computer_rack)
#         earned_points = calculate_points(computer, computer_word)
#         print(f'Computer earned {earned_points} points.')
#         remove_tiles(computer_word, computer_rack)
#         computer_points += earned_points
#         print('------------------------------')

# game_play()
print(letter_probabilities)