"This module contains testing procedures"

import pytest
import word as word
from game import Game
import exceptions as ex


class TestVerifyWord:
    "Tests if the verify method works as intended"

    def test_valid(self):
        '''Test if the verify method works as intended
        
        Inputs:
            - words that only contain letters in the rack and are English.
        
        Returns:
            - Assertions checks if the valid words are returned.
        '''

        words_to_test = ['LIMBATE', 'BIMETAL', 'TIMBALE', 'ALBITE', 'LAMBIE'
        , 'ALBITE', 'TIMBAL', 'ALBEIT', 'EMAIL', 'TELIA', 'AMBIT', 'LIMBA'
        , 'TABLE', 'BALM', 'BLAM', 'AMIE', 'MABE', 'ABLE', 'LIB', 'BAT'
        , 'MIB', 'MEL', 'MAT', 'LI', 'TA', 'BA', 'AM', 'AT']
        rack = ['B', 'A', 'I', 'T', 'L', 'E', 'M']
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert test_word.verify(rack) == test_word.word

    def test_not_in_rack(self):
        '''Tests to catch words that use letters which are not in the rack
        
        Inputs:
            - words that only contain some letters which are not in the rack.
        
        Returns:
            - Assertions checks for False values.
        '''

        rack = ['A', 'C', 'E', 'Y', 'D', 'A', 'M']
        words_to_test = ['CAMERA', 'AGED', 'YEAR', 'DAMP', 'ACHY'
        , 'QUEEN', 'CAKE', 'DYED', 'DICE', 'AIMED' ]
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)

    def test_used_too_many_times(self):
        '''Tests to catch words that use letters in the rack too many times
        
        Inputs:
            - words which contain letters whose count is higher than their
            occurrences in the rack
        
        Returns:
            - Assertions checks for False values.
        '''

        rack = ['M', 'O', 'N', 'T', 'A', 'L']
        words_to_test = ['MOON', 'TOTAL', 'NOON', 'TOOL', 'TALL', 'MOM']
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)

    def test_not_english(self):
        '''Tests to catch words that contain valid letters but are not English
        
        Inputs:
            - words which contain valid letters but are not English
        
        Returns:
            - Assertions checks for False values.
        '''

        rack = ['O', 'R', 'T', 'S', 'L', 'A', 'W']
        words_to_test = ['OWTS', 'SRAWLO', 'SALWOD', 'TORALS', 'RTSAWO', 'LS', 'ROTSLAW', 'LARTSW']
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)


class TestChooseCharacter:
    "Test to catch invalid characters being input from the terminal"

    def test_invalid_character(self, monkeypatch):
        """Tests if InvalidInput is raised when an invalid character is input from the terminal

        Input:
            - input (iter object): list of invalid characters

        Returns: 
            - InvalidInput exception.
        """

        fake_inputs = iter(['hero', 'lion king', 'hulk', '326', '15.5', 'j@kesteR'])

        monkeypatch.setattr('builtins.input', lambda prompt: next(fake_inputs))
        with pytest.raises(ex.InvalidInput):
            game = Game()
            game.choose_character()

class TestExceptions:
    "Tests if exceptions are raised appropriately"
    
    def test_quit(self, monkeypatch):
        "Tests if Quit exception is raised when '%quit' is input from the terminal."

        fake_input = '%quit'
        monkeypatch.setattr('builtins.input', lambda prompt: fake_input)
        with pytest.raises(ex.Quit):
            game = Game()
            game.choose_character()
            game.get_word()

    def test_get_help(self, monkeypatch):
        "Tests if GetHelp exception is raised when '%help' is input from the terminal."

        fake_input = '%help'
        monkeypatch.setattr('builtins.input', lambda prompt: fake_input)
        with pytest.raises(ex.HelpRequired):
            game = Game()
            game.choose_character()
            game.get_word()

    def test_skip(self, monkeypatch):
        "Tests if SkipTurn exception is raised when '%skip' is input from the terminal."

        fake_input = '%skip'
        monkeypatch.setattr('builtins.input', lambda prompt: fake_input)
        with pytest.raises(ex.SkipTurn):
            game = Game()
            game.choose_character()
            game.get_word()


class TestScoreKeeping:
    "Tests if word points are calculated correctly"

    def test_calculate_points(self):
        """Tests if calculated word points are correct
        
        Inputs:
            - words (dict): stores English words and their points
        """
        words = {'PADLE': 8, 'QUEEN': 14, 'MOODY': 11, 'ZIPPY': 21
        , 'TESTER': 6, 'ED': 3, 'PAT': 5, 'MARS': 6}

        game = Game()
        for key, value in words.items():
            assert game.calculate_points(key) == value
            