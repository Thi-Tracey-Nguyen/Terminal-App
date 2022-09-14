from spellchecker import SpellChecker
import itertools
dictionary = open("dic.txt").read().splitlines()

# spell = SpellChecker()
# x = bool(spell.known('battle'))
# print(x)

char = ['a', 't', 'c']
list_words_to_test = []
s = ''.join(char)
print(s)

t = list(itertools.permutations(s,len(s)))
print(t)
for i in range(0,len(t)):
    list_words_to_test.append(''.join(t[i]))
print(list_words_to_test)

meaningful_words = []
for word in list_words_to_test:
    if word.upper() in dictionary: 
        meaningful_words.append(word)