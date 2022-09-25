"""This module contains Character class, its subclass (Computer), its attributes and methods"""

import random
from time import sleep
from itertools import permutations
import data as d
import word as w

class Character():
    """This is the parent class, used to instantiate Human player
    
    Attributes:
        - name (str): player's name
        - points (int): player's points
        - rack (list): player's rack of letters
    """

    def __init__(self, name):
        """Constructor for character object"""
        self.name = name
        self.points = 0
        self.rack = []

    def __repr__(self):
        """String representation of a character object"""

        return self.name

    def __str__(self):
        """String representation of a character object"""
        
        return self.name

class Computer(Character):
    """This class is a subclass of Character class, it is used to instantiate a computer player"""

    def __init__(self, name):
        """Constructor for computer player

        Attributes:
            - name (str): supered from super class
            - word_length (list): list of possible word lengths
        """

        super().__init__(name)
        if self.name == 'The Kid':
            self.word_length = [3, 4, 5]
        else:
            self.word_length = [4, 5, 6, 7]

    def random_number(self, word_length):
        """Generates a random number from word_length list
        
        Arg:
            - word_length (list): list of possible word lengths
        
        Return:
            - group_number (int): number of letters in word
        """

        group_numbers = random.sample(self.word_length, len(word_length) - 1)
        return group_numbers

    def play(self):
        """Creates combinations of letters based on group_number and player's rack
        and iterates through each member of the combination and checks if 
        it is an English word
        
        Returns:
            - word (str): if an English word is found
            - None is the options are exhausted and no English word is found
        """

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
        """Prints thinking  message to the terminal"""

        d.typewriter('Now let me think... \n')
        if self.name == 'The Kid':
            repeats = 1
        else: 
            repeats = 3
        for i in range(repeats):
            print('...\n')
            sleep(1)

    def response_end(self, message):
        """Prints a response at the end of the game"""
        
        print(f'{self.name}: ', end='')
        d.typewriter(message)