import pytest
import word

english_words = ['LIMBATE', 'BIMETAL', 'TIMBALE', 'ALBITE', 'LAMBIE', 'ALBITE', 'TIMBAL', 'ALBEIT', 'EMAIL', 'TELIA', 'AMBIT', 'LIMBA', 'TABLE', 'BALM', 'BLAM', 'AMIE', 'MABE', 'ABLE', 'LIB', 'BAT', 'MIB', 'MEL', 'MAT', 'LI', 'TA', 'BA', 'AM', 'AT']


class TestVerifyWord: 
    def test_valid(self): 
        rack = ['B', 'A', 'I', 'T', 'L', 'E', 'M']
        for test_word in english_words:
            test_word = word.Word(test_word)
            assert test_word.verify(rack) == str(test_word)


    def test_not_in_rack(self, monkeypatch): 
        pass

    def test_not_english(self, monkeypatch): 
        pass