import random
from time import sleep
from itertools import permutations
import data as d
import word as w

class Character():
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rack = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Computer(Character):
    def __init__(self, name):
        super().__init__(name)
        if self.name == 'The Kid':
            self.word_length = [3, 4, 5]
        else:
            self.word_length = [4, 5, 6, 7]

    def random_number(self, word_length):
        group_numbers = random.sample(self.word_length, len(word_length) - 1)
        return group_numbers

    def play(self):
        words_to_test = []
        for number in self.random_number(self.word_length):
            letter_combinations = list(permutations(self.rack, number))
            for combination in letter_combinations:
                words_to_test.append(''.join(combination))
            for word in words_to_test:
                if word in w.english_words:
                    print(f'{self.name} played {word}\n')
                    return word
        return None

    def response(self, tone):
        """This function picks a random response to the opponent's word from a list of positive responses

        Returns:
            _int_: a phrase chosen at random
        """
        print('\n')
        print(f'{self.name}: ', end = '')
        if tone == 'positive':
            message = random.choice(d.positive)
        elif tone == 'negative':
            message = random.choice(d.negative) + '\n' + random.choice(d.encourage)
        else:
            message = random.choice(d.skip)
        d.typewriter(message)
        print('\n')

    def think(self):
        print('Now let me think... ')
        if self.name == 'The Kid':
            repeats = 1
        else: 
            repeats = 3
        for i in range(repeats):
            print('...')
            sleep(1)

    def response_end(self, message):
        print(f'{self.name}: ', end='')
        d.typewriter(message)