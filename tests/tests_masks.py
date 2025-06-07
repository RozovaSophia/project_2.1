from src.masks import *

def test_get_mask_card():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_for_atypical_numbers():
    assert get_mask_card_number("!@#$%^&*()--===") == "Error: invalid number format"


def test_for_an_empty_value():
    assert get_mask_card_number("") == "Error: invalid number format"


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"


def test_for_atypical_account():
    assert get_mask_account("!@#$$%^^^&^%$") == "Error: invalid account format"


def test_for_incorrect_num_len():
    assert get_mask_account("1234567890") == "Error: invalid account format"