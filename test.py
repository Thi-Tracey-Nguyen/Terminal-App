import random
import string
import itertools

with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

player_rack = ['Y', 'T', 'N', 'O', 'E', 'V', 'H']
# group_number = random.randint(2, 6)
group_number = 5
print(group_number)

def shuffle_letters():
    words_to_test= []
    # group_number = random.randint(2, 6)
    # print(group_number)
    t = list(itertools.permutations(player_rack, group_number))
    for i in range(len(t)):
        words_to_test.append(''.join(t[i]))
    return words_to_test

x = shuffle_letters()
# print(x)

def is_english_word(player_word):
    if player_word in english_words:
        return True

def computer_play(): 
    for word in x: 
      if is_english_word(word): 
        return word

print(computer_play())