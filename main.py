import random
import itertools
from numpy import random as npr

# dictionary = open("dic.txt").read().splitlines()


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "#": 0}

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2}


def tile_probability():
    """This function calculates probabilities of each tile in the bag 

    Returns:
        _dict_: name of tile and its associated probability
    """  
    return {letter : tile_bag[letter] / 100 for letter in tile_bag.keys()}

letter_probabilities = tile_probability()

group_number = 4
print(group_number)

def deal_tiles(): 
    """This function randomly deals 5 tiles for each player propotionally to the tile's probalibily

    Returns:
        __str__: name of tiles
    """    
    letters = [key for key in letter_probabilities.keys()]
    probabilities = [value for value in letter_probabilities.values()]
    rack = npr.choice(letters, 7,p=probabilities, replace=False)
    return list(rack)

player_rack = deal_tiles()
# print(player_rack)


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

def calculate_points(word):
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
            print(f'Well played! {human_player_word} is an excellent choice.\nYou earned {calculate_points(human_player_word)} points.')
            break
        else: 
            print(f'{human_player_word}?? It\'s not a valid word. Try again. ')
    return human_player_word

# Computer play: 
def computer_play(player_rack): 
    for word in shuffle_letters(player_rack): 
      if is_english_word(word): 
        return word


def game_play(): 
    greetings()
    human_player_rack = deal_tiles()
    computer_rack = deal_tiles()
    print(f'Your rack is: {human_player_rack}')
    print(f'Computer rack: {computer_rack}')
    for i in range(1,8):
        print(f'Round {i} ') 
        human_player()
        computer_word = computer_play(computer_rack)
        print(f'Computer\'s word is: {computer_word}')
        computer_points = calculate_points(computer_word)
        print(f'Computer earned {computer_points} points')

game_play()
