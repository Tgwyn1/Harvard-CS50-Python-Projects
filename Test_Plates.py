import pytest
import re
import plates
from plates import is_valid

def test_letters():
    assert is_valid('AC5478') == True # The first two characters need to be letters
    assert is_valid('355478') == False # Numbers should not pass within the first 2 characters
    assert is_valid ('ABCDEF') ==  True # All letters should function

def test_invalid_length_2_6(): # Length needs to be in between 2 and 6 characters
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_digits_no_revert(): # Digits should not reverd back to numbers
    assert is_valid('ABC58A') == False

def test_no_periods_spaces_punctuaction(): # No periods, spaces, or punctuation
    assert is_valid('AB.478') == False

def test_zero_placement(): # No zeros are allows
    assert is_valid('ABD015') == False
