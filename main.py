# from spellchecker import SpellChecker
import random
import itertools
dictionary = open("dic.txt").read().splitlines()

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


char = ['p', 'r', 'o', 'u', 'd', 'e']
# char = ['c', 'a', 't', 's']
list_words_to_test = []

# # random_number = random.randint(2, len(s))

# # print(random_number)
t = list(itertools.permutations(char,len(char)))
# print(t)
for i in range(len(t)):
    list_words_to_test.append(''.join(t[i]))

# Test using words in a set
with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

def is_english_word():
    meaningful_words = []
    for word in list_words_to_test:
        if word.upper() in english_words: 
            meaningful_words.append(word)
    return meaningful_words

print(is_english_word())


