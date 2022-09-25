"""This module contains essential functions for game flow."""

import random
from time import sleep
import clearing
from numpy import random as nur
import data as d
import word as w
import exceptions as ex
import character as ch

        
class Game:
    """This class is used to instantiate a game. It has methods that are essential in a game.""" 

    def __init__(self):
        pass

    def get_input(self, prompt):
        """Gets user input and compares it to values which raise exceptions.
        
        Args:
            - prompt (str): prompt to get user input

        Returns:
            - exceptions: appropriate exceptions for user input
            - user_input (str): if input is not terms that raise exceptions, returns user input.
        """

        input_value = input(prompt).lower()
        if input_value == '%quit':
            raise ex.Quit
        elif input_value == '%help':
            self.get_help()
            raise ex.HelpRequired
        elif input_value == '%skip':
            raise ex.SkipTurn
        else:
            return input_value

    def announce_blocks(self, message):
        """Print out messages that are in blocks.

        Args:
            - message (str): multiple-lined messages
        """
        sleep(0.5)
        print(message)
        sleep(0.5)

    def get_help(self):
        """Print out 'Help' message"""

        print("""
        \nThings to note:
        1. %Help to see this message again
        2. %Quit to quit at any point of the game
        3. %Skip to skip your turn
        4. Q, Z, J and Z bring higher points.
        """)

    def announce_player(self, player):
        """Print the annoucement of computer player with typewriter effect
        
        Args:
            - player (Computer): computer player
        """

        if player.name == 'The Kid':
            d.typewriter('\nThe Kid just run in from outside. He will play with you!')
        else:
            d.typewriter('\nThe Word Master just roused from a siesta. He will take you on.')

    def announce_rack(self, player):
        """Print human player's and computer player's racks with typewriter effect
        
        Args:
            - player (Computer): computer plaer
        """

        if player.name == 'Human':
            d.typewriter(f'Your rack is: {player.rack}\n')
        else: 
            d.typewriter(f"{player.name}'s rack is: {player.rack}\n")

    def announce_turn(self):
        """Print announcement of human player's turn"""

        print("\nIt's your turn. Play an English word.")
        print("""***Type %Help to get help at any time***\n""")

    def announce_scores(self, list_of_players):
        """Print computer player's and human players' scores
        
        Args:
            - list_of_players (list): List of players
        """

        s = "'s"
        for player in list_of_players:
            print(f"{player.name + s if player.name != 'Human' else 'Your'} {'point is' if player.points <= 0 else 'points are'}: {player.points}.", end = ' ')
        if list_of_players[0].points == list_of_players[1].points == 0: 
            print('Let\'s begin.')
        elif list_of_players[0].points == list_of_players[1].points: 
            print('It\'s a tie.')
        elif list_of_players[0].points > list_of_players[1].points: 
            print('You are in front.')
        else: 
            print(f'{list_of_players[1]} is in front.')

    def announce_end(self, list_of_players):
        """Print final scores of human and computer players, and the final verdict
        
        Args:
            - list_of_players (list): list of players
        """

        s = "'s"
        for player in list_of_players:
            print(f"{player.name + s if player.name != 'Human' else 'Your'} {'point is' if player.points <= 0 else 'points are'}: {player.points}.", end = ' ')
        print('\n')
        if list_of_players[0].points == list_of_players[1].points: 
            print('It\'s a tie.') 
            print('\n')
            message = 'Well done! With a little more training, you will be ready to take on the Jokester.'
        elif list_of_players[0].points > list_of_players[1].points: 
            print('You won!')
            print('\n')
            message = 'I have never met such a competent player. You are ready to battle the Jokester.'
        else:
            print('You lost!')
            print('\n')
            message = 'Solid effort. But you are not ready yet. Go back and train some more.'
        return message
        
    def countdown(self, message):
        """Print countdown numbers on the terminal
        
        Args:
            - message (str): announcement of new round
        """
        print(message)
        for i in (3, 2, 1, 0):
            sleep(1)
            print(f'{i}...')
            sleep(0.5)
        
    def choose_character(self):
        """Compares user input to available characters.
        
        Returns:
            - user input if valid
            - raises InvalidInput if user input is invalid
        """
        
        kid_name_options = ['kid', 'the kid']
        master_name_options = ['master', 'the master', 'word master', 'the word master']
        player_choice = str(self.get_input('>>>>  ')).strip().lower()
        choices = ['The Kid', 'The Word Master']
        if player_choice in kid_name_options:
            return 'The Kid'
        elif player_choice in master_name_options:
            return 'The Word Master'
        elif player_choice == 'random':
            return random.choice(choices)
        else:
            raise ex.InvalidInput

    def get_word(self):
        """Compares user input to '%skip'
        
        Returns:
            - user input if it is not '%skip'
            - raises SkipTurn exception if it is '%skip
        """

        human_input = self.get_input('>>>  ')
        if human_input == '%skip':
            raise ex.SkipTurn
        else:
            human_word = human_input
            return human_word.upper()

    def letter_probability(self):
        """This function calculates probabilities of each letter in the collection

        Returns:
            _dict_: name of letter and its associated probability
        """

        total_number_of_letters = sum(d.letter_collection.values())
        return {letter : d.letter_collection[letter] / total_number_of_letters for letter in d.letter_collection.keys()}

    def deal_letters(self, player):
        """This function randomly randomize 7 letters for each player propotionally to the letters' frequencies.

        Args:
            rack(_list_): whose rack to deal letters to
            
        Returns:
            __list__: player's rack
        """

        letters = list(self.letter_probability().keys())
        probabilities = list(self.letter_probability().values())
        player.rack = nur.choice(letters, 7,p=probabilities, replace = True)
        return list(player.rack)

    def calculate_points(self, word):
        """This function calculates points based on the word played

        Args:
            word (_str_): word played by the player
        Returns:
            _int_: points
        """

        points = 0
        word = word.strip().upper()
        for letter in word:
            points += d.letter_values[letter]
        return points

    def play(self):
        """Main flow of the game"""

        try:
            d.typewriter(d.greetings)
            self.announce_blocks(d.greetings_block_1)
            self.announce_blocks(d.greetings_block_2)
            d.typewriter(d.available_characters)
            human_player = ch.Character('Human')
            players = [human_player]
            while True:
                print('\n')
                print('Please choose a valid opponent ("Kid", "Master" or "Random"). ')
                try:
                    player_choice = self.choose_character()
                except ex.InvalidInput:
                    print('Invalid character. Type %Help to get help.')
                except ex.HelpRequired:
                    continue
                except ex.SkipTurn:
                    print('You cannot skip here. Type %Help to get help.')
                    continue
                else:
                    if player_choice:
                        computer_player = ch.Computer(player_choice)
                        players.append(computer_player)
                        break
            self.announce_player(computer_player)
            print('\n')
            self.countdown('Get Ready. Starting in... ')
            for i in range(1, 8):
                clearing.clear()
                print('------------------------------------------------------------')
                print('Round ', i)
                self.announce_scores(players)
                print('\n')
                for player in players:
                    player.rack = self.deal_letters(player)
                    self.announce_rack(player)
                self.announce_turn()
                while True:
                    try:
                        human_word = self.get_word()
                    except ex.HelpRequired:
                        continue
                    except ex.SkipTurn:
                        human_word = '####'
                        print('You chose to skip.\n')
                        break
                    else:
                        word = w.Word(human_word)
                        is_verified = word.verify(human_player.rack)
                        if is_verified:
                            human_player.points += self.calculate_points(human_word)
                            computer_player.response('positive')
                            break
                        else:
                            computer_player.response('negative')
                sleep(1)
                computer_player.think()
                computer_word = computer_player.play()
                if not computer_word:
                    computer_player.response('skip')
                else:
                    computer_player.points += self.calculate_points(computer_word)
                if i == 7:
                    continue
                self.countdown('Starting next round: ')

            print('------------------------------------------------------------')
            message = self.announce_end(players)
            computer_player.response_end(message)

        except (ex.Quit, KeyboardInterrupt):
            print('\n')
            print('Okay! Come back when you are ready!')
        finally:
            print('\n')
            print('------------------------------------------------------------')
            print('Thi Nguyen. Copyright (c) 2022.')
            print('\n')

