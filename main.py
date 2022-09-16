import random
import itertools
import string
from numpy import random as npr

# dictionary = open("dic.txt").read().splitlines()


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)


# print(list_words_to_test)

# Iterate through words in the words_to_check list and check them against the dictionary


# def is_english_word_non_set():
#     meaningful_words = []
#     for word in list_words_to_test:
#         if word.upper() in dictionary: 
#             meaningful_words.append(word)
#     return meaningful_words

# print(is_english_word_non_set())

# Testing spellchecker 

# spell = SpellChecker()
# # spell.word_frequency.load_text_file('dic_fake.txt')
# x = spell.known(['hat', 'water', 'mouse', 'chair', 'hanger', 'dsfsd', 'asdfas', 'asdfasd'])
# print(x)

# char = ['c', 'a', 't', 's']

# # random_number = random.randint(2, len(s))

# # print(random_number)




# print(string.ascii_uppercase)
rack = ['o', 'd', 's', 'a', 'g', 'e']

# for i in range(7): 
#     random_letter = random.choice(string.ascii_uppercase)
#     rack.append(random_letter)

# print(rack)


# group_number = len(rack)
# t = list(itertools.permutations(rack, group_number))
# for i in range(len(t)):
#     list_words_to_test.append(''.join(t[i]))

# Test using words in a set



def shuffle_letters():
    list_words_to_test = []
    group_number = random.randint(2, 6)
    t = list(itertools.permutations(rack, group_number))
    for i in range(len(t)):
        list_words_to_test.append(''.join(t[i]))
    return list_words_to_test



def is_english_word():
    for word in shuffle_letters():
        if word.upper() in english_words:
            return word.upper()

# print(is_english_word())

# Drawing random but based on frequency

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2}

def total_number_of_tiles():
    """This function calcutes the total number of tiles in the tile bag

    Returns:
        _int_: total number of tiles
    """
    total_number_of_tiles = 0
    for letter in tile_bag: 
        frequency = tile_bag[letter]
        total_number_of_tiles += frequency
    return total_number_of_tiles 

# print(total_number_of_tiles())

def tile_probability():
    """This function calculates probabilities of each tile in the bag 

    Returns:
        _dict_: name of tile and its associated probability
    """  
    return {letter : tile_bag[letter] / 100 for letter in tile_bag.keys()}

letter_probabilities = tile_probability()

def deal_tiles(): 
    """This function randomly deals 5 tiles for each player propotionally to the tile's probalibily

    Returns:
        __str__: name of tiles
    """    
    pass


letters = [key for key in letter_probabilities.keys()]
probabilities = [value for value in letter_probabilities.values()]
# print(letters)
# print(probabilities)

draw = npr.choice(letters, 5,p=probabilities, replace=False)
print(draw)