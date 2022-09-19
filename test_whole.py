import itertools
from numpy.random import choice

player_rack = ['A', 'G', 'A', 'R', 'T']
group_number = 3
def shuffle_letters(player_rack):
    words_to_test= []
    # group_number = random.randint(2, 6)
    group_number = 3
    large_combinations = list(itertools.permutations(player_rack, group_number))
    for combination in large_combinations:
        words_to_test.append(''.join(combination))
    return words_to_test

# print(shuffle_letters(player_rack))

print(type(choice(player_rack)))