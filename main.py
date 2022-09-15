# from spellchecker import SpellChecker
import random
import itertools
import string

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
rack = []

for i in range(8): 
    random_letter = random.choice(string.ascii_uppercase)
    rack.append(random_letter)

print(rack)


# group_number = len(rack)
# t = list(itertools.permutations(rack, group_number))
# for i in range(len(t)):
#     list_words_to_test.append(''.join(t[i]))

# Test using words in a set


def shuffle_letters():
    list_words_to_test = []
    group_number = len(rack)
    t = list(itertools.permutations(rack, group_number))
    for i in range(len(t)):
        list_words_to_test.append(''.join(t[i]))
    return list_words_to_test


def is_english_word():
    for word in shuffle_letters():
        if word.upper() in english_words: 
            return word.upper()




shuffle_letters()
print(is_english_word())
