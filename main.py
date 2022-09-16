import random
import itertools
from numpy import random as npr

# dictionary = open("dic.txt").read().splitlines()


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)


tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2}


def tile_probability():
    """This function calculates probabilities of each tile in the bag 

    Returns:
        _dict_: name of tile and its associated probability
    """  
    return {letter : tile_bag[letter] / 100 for letter in tile_bag.keys()}

letter_probabilities = tile_probability()

group_number = 5
print(group_number)

def deal_tiles(): 
    """This function randomly deals 5 tiles for each player propotionally to the tile's probalibily

    Returns:
        __str__: name of tiles
    """    
    letters = [key for key in letter_probabilities.keys()]
    probabilities = [value for value in letter_probabilities.values()]
    # print(letters)
    # print(probabilities)
    rack = npr.choice(letters, 7,p=probabilities, replace=False)
    return list(rack)

player_rack = list(deal_tiles())
print(player_rack)


def shuffle_letters():
    words_to_test= []
    # group_number = random.randint(2, 6)
    # print(group_number)
    t = list(itertools.permutations(player_rack, group_number))
    for i in range(len(t)):
        words_to_test.append(''.join(t[i]))
    return words_to_test

x = shuffle_letters()

def is_english_word(player_word):
    if player_word.upper() in english_words:
        return player_word.upper()


# print(is_english_word(x))

def greetings(): 
    print('''Hello! Welcome to Word Play! here are some rules: 
    - you can skip
    - you can get a hint
    - play a valid english word
    ''')

def human_player():
    while True: 
        human_player_word = input('It\'s your turn. Play a valid English word. ').upper()
        human_player_word_valid = is_english_word(human_player_word)
        if human_player_word_valid: 
            print(f'Well played! {human_player_word} is an excellent choice.')
            break
        else: 
            print(f'{human_player_word}?? It\'s not a valid word. Try again. ')
    return human_player_word

# Computer play: 
def computer_play(): 
    for word in x: 
      if is_english_word(word): 
        return word

def game_play(): 
    greetings()
    print(f'Your rack: {deal_tiles()}')
    print(f'Computer rack: {deal_tiles()}')
    human_player()
    print(f'Computer\'s word is: {computer_play()}')
    

game_play()
