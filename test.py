import random
import string
import itertools

with open("dic.txt") as word_file:
    english_words = set(word.strip() for word in word_file)

rack = ['d', 'o', 's', 'a', 'g', 'e']

# for i in range(7): 
#     random_letter = random.choice(string.ascii_uppercase)
#     rack.append(random_letter)

print(rack)

list_words_to_test = []
group_number = 5
t = list(itertools.permutations(rack, group_number))
for i in range(len(t)):
  list_words_to_test.append(''.join(t[i]))

# print(t)
# print(list_words_to_test)

def is_english_word():
  meaningful_words = []
  for word in list_words_to_test:
    if word.upper() in english_words:
      meaningful_words.append(word.upper())
  return meaningful_words

print(is_english_word())