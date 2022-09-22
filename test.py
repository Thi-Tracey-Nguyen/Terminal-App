import pytest
import word
from main import Game
from exceptions import InvalidInput


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
        with pytest.raises(InvalidInput):
            game = Game()
            game.choose_character()
