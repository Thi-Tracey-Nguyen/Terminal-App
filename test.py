import random
import string
import itertools
from numpy.random import choice

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "#": 0}

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2}


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

# player_rack = ['E', 'P', 'I', 'H', 'G', 'N', 'D']
# # group_number = random.randint(2, 6)
# group_number = 5
# print(group_number)

# def shuffle_letters():
#     words_to_test= []
#     # group_number = random.randint(2, 6)
#     # print(group_number)
#     t = list(itertools.permutations(player_rack, group_number))
#     for i in range(len(t)):
#         words_to_test.append(''.join(t[i]))
#     return words_to_test

# x = shuffle_letters()
# print(x)

# def is_english_word(player_word):
#     if player_word in english_words:
#         return True

# def computer_play(): 
#     for word in x: 
#       if is_english_word(word): 
#         return word

# print(computer_play())

# def calculate_points(word):
#     """This function calculates points based on the word played

#     Args:
#         word (_str_): word played by the player
#     Returns:
#         _int_: points
#     """   
#     points = 0
#     for i in range(len(word)): 
#         points += letter_values[word[i]] 
#     return points

# print(calculate_points(SANE))

tile_bag = ['A', 'G', 'A', 'R', 'H', 'I', 'M']
rack = ['A', 'G', 'A', 'R']

def is_english_word(player_word):
    if player_word.upper() in english_words:
        return player_word.upper()

def verify_word(word, rack):
    word_split = list(word)
    # rack_letter_count = {word[i] : rack.count(word[i]) for i in range(len(word)-1)}
    # print(rack_tile_count)
    for letter in word_split:
        if letter not in rack: 
            print(f'{letter} is not in your rack. Try again. ')
            break
    if is_english_word(word):
      print(f'Well play! {word} is an excellent choice. ') 
      return True
    else: 
      print(f'{word}??? It isn\'t a valid English word. Try again. ')

# verify_word('AGAR', rack)

rack = ['B', 'A', 'N', 'A']

word = 'BANANA' 

verify_word(word, rack)



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
    if check_within_rack(word, rack):
        if is_english_word(word):
            print(f'Well play! {word} is an excellent choice.') 
            return word
        else: 
            print(f'{word}??? It isn\'t a valid English word. Try again.')
            return False
    else: 
        print('Try again.')
        return False

x = verify_word(word, rack)