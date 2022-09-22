import sys
from time import sleep

letter_values = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

letter_collection = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 9, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 3, "Z": 1}

# letter_probability = {'A': 0.09, 'B': 0.02, 'C': 0.02, 'D': 0.04, 'E': 0.12, 'F': 0.02, 'G': 0.03, 'H': 0.02, 'I': 0.09, 'J': 0.01, 'K': 0.01, 'L': 0.04, 'M': 0.02, 'N': 0.06, 'O': 0.09, 'P': 0.02, 'Q': 0.01, 'R': 0.06, 'S': 0.04, 'T': 0.06, 'U': 0.04, 'V': 0.02, 'W': 0.02, 'X': 0.01, 'Y': 0.03, 'Z': 0.01}

greetings = 'Hello! Welcome to Word Play!\n'
greetings_block_1 = "\nYou are a word enthusiast from Fancy Town who wants to beat the Jokester at a Word Game so he will stop bothering your village. But before that, you want to train with the local Word Master to see if you are up for the challenge. The Kid is the Word Master's grandson, he is cheeky and smart. He likes to interrupt his grandfather's visitors." 

greetings_block_2 = "\nThe goal of the game is to form a word from the provided 'rack'. Z, Q, and X have much higher points than the others. Try to use them if they are in your rack. Whoever has the highest score after 7 rounds wins." 

available_characters = """
Choose your opponent: 
    - The Kid is smart and fast but he plays mostly short words
    - The Word Master is wise but slow, he sometimes falls asleep and has to skip a turn, but his words are intricate.
    - Random to let the computer choose for you.\n
    """

negative = ['You think I am silly, don\'t you?', 'You just made that up, didn\'t you?', 'Is that all you got?', 'Lame effort.', 'I thought you were better than that.']

positive = ['That\'s brilliant!\n', 'You\'re very clever!\n', 'No wonder the people of Fancy Town think so highly of you\n', 'Well played!\n', 'A worthy opponent!\n']

encourge = ['Now give it another go\n', 'Don\'t give up! Try again.\n']

skip = ['I don\'t know, this is too much for me!\n', 'Hmmmm... I have no answers\n', 'I must have fallen asleep. I\'ll have to skip\n']

def typewriter(message):
        for letter in message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.01) if letter != '\n' else sleep(0.1)