import pytest
import word
from main import Game
import exceptions as ex


class TestVerifyWord: 

    def test_valid(self):
        words_to_test = ['LIMBATE', 'BIMETAL', 'TIMBALE', 'ALBITE', 'LAMBIE', 'ALBITE', 'TIMBAL', 'ALBEIT', 'EMAIL', 'TELIA', 'AMBIT', 'LIMBA', 'TABLE', 'BALM', 'BLAM', 'AMIE', 'MABE', 'ABLE', 'LIB', 'BAT', 'MIB', 'MEL', 'MAT', 'LI', 'TA', 'BA', 'AM', 'AT']
        rack = ['B', 'A', 'I', 'T', 'L', 'E', 'M']
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert test_word.verify(rack) == test_word.word

    def test_not_in_rack(self): 
        rack = ['A', 'C', 'E', 'Y', 'D', 'A', 'M']
        words_to_test = ['CAMERA', 'AGED', 'YEAR', 'DAMP', 'ACHY', 'QUEEN', 'CAKE', 'DYED', 'DICE', 'AIMED' ]
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)

    def test_used_too_many_times(self): 
        rack = ['M', 'O', 'N', 'T', 'A', 'L']
        words_to_test = ['MOON', 'TOTAL', 'NOON', 'TOOL', 'TALL', 'MOM'] 
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)

    def test_not_english(self):
        rack = ['O', 'R', 'T', 'S', 'L', 'A', 'W']
        words_to_test = ['OWTS', 'SRAWLO', 'SALWOD', 'TORALS', 'RTSAWO', 'LS', 'ROTSLAW', 'LARTSW']
        for test_word in words_to_test:
            test_word = word.Word(test_word)
            assert not test_word.verify(rack)


class TestChooseCharacter:

    def test_invalid_character(self, monkeypatch):
        inputs = iter(['hero', 'lion king', 'hulk', '326', '15.5', 'j@kesteR'])

        monkeypatch.setattr('builtins.input', lambda prompt: next(inputs))
        with pytest.raises(ex.InvalidInput):
            game = Game()
            game.choose_character()

class TestExceptions:
    
    def test_quit(self, monkeypatch):
        input = '%quit'
        monkeypatch.setattr('builtins.input', lambda prompt: input)
        with pytest.raises(ex.Quit):
            game = Game()
            game.choose_character()
            game.get_word()

    def test_get_help(self, monkeypatch):
        input = '%help'
        monkeypatch.setattr('builtins.input', lambda prompt: input)
        with pytest.raises(ex.HelpRequired):
            game = Game()
            game.choose_character()
            game.get_word()

    def test_skip(self, monkeypatch):
        input = '%skip'
        monkeypatch.setattr('builtins.input', lambda prompt: input)
        with pytest.raises(ex.SkipTurn):
            game = Game()
            game.choose_character()
            game.get_word()

class TestScoreKeeping: 
    def test_calculate_points(self):
        words = ['PADLE', 'QUEEN', 'MOODY', 'ZIPPY', 'TESTER', 'ED', 'PAT', 'MARS']
        points =[8, 14, 11, 21, 6, 3, 5, 6]
        game = Game()
        for index, value in enumerate(words):
            assert game.calculate_points(value) == points[index]