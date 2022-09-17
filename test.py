import numbers
import random
import string
import itertools
from numpy.random import choice

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "#": 0}

tile_bag = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "#": 2}


with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

def tile_probability():
    """This function calculates probabilities of each tile in the bag 

    Returns:
        _dict_: name of tile and its associated probability
    """  
    total_number_of_tiles = sum(tile_bag.values())
    return {letter : tile_bag[letter] / total_number_of_tiles for letter in tile_bag.keys()}

letter_probabilities = tile_probability()

# def deal_tiles(number_of_tiles): 
#     """This function randomly deals 5 tiles for each player propotionally to the tile's probalibily

#     Args: 
#         number_of_tiles(_int_): how many tiles to deal

#     Returns:
#         __str__: name of tiles
#     """    
#     letters = [key for key in letter_probabilities.keys()]
#     probabilities = [value for value in letter_probabilities.values()]
#     rack = choice(letters, number_of_tiles,p=probabilities, replace=False)
#     return list(rack)

# def replenish(rack): 
#     """This function replishes a player's rack after each round

#     Args:
#         rack (_list_): partially used player's rack 

#     Returns:
#         rack (_list_): fully-stocked player's rack
#     """    
#     number_of_tiles = 7 - len(rack)
#     new_tiles = deal_tiles(number_of_tiles)
#     new_rack = rack + new_tiles
#     return new_rack

# player_rack = ['B', 'U', 'S', 'H']

# player_rack = player_rack + replenish(player_rack)

# print(player_rack)

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

human_rack = ['A', 'M']
computer_rack = []

x = deal_tiles(human_rack)
print(deal_tiles(computer_rack))
print(x)

human_rack += x
print(human_rack)