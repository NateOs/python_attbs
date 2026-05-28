# test_reverse_string.py
from reverse_string import reverse_string


def test_basic_word():
    assert reverse_string("hello") == "olleh"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("a") == "a"


def test_palindrome():
    assert reverse_string("racecar") == "racecar"


def test_numbers():
    assert reverse_string("12345") == "54321"


def test_spaces_and_punctuation():
    assert reverse_string("hello world!") == "!dlrow olleh"