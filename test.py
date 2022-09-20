import itertools
import os
import random
from types import NoneType
 
path = os.path.abspath("dic.txt")

with open(path, 'r', encoding='utf-8') as word_file:
    english_words = set(word.strip() for word in word_file)

# def play(rack, word_length):
#     group_number = word_length
#     for i in range(len(group_number) - 1):
#         random_number = group_number.pop(random.randint(0, group_number))
#         words_to_test= []
#         letter_combinations = list(itertools.permutations(rack, random_number))
#         for combination in letter_combinations:
#             words_to_test.append(''.join(combination))
#         for word in words_to_test: 
#             if word in english_words:
#                 print(f'Computer played {word}')
#                 return word
#     return None

rack = ['B', 'A', 'T', 'T', 'L', 'E', '#']

def pop_random_number(word_length):
    word_length = [5, 6, 7]
    group_numbers = random.sample(word_length, 2)
    return group_numbers

def play_word(rack):
    words_to_test = []
    for number in pop_random_number(word_length):
        letter_combinations = list(itertools.permutations(rack, number))
        for combination in letter_combinations:
            words_to_test.append(''.join(combination))
        for word in words_to_test: 
            if word in english_words:
                print(f'Computer played {word}')
                return word
        

word_length = [5, 6, 7]
print(play_word(rack))

