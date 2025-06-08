from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card(fixture_for_mask):
    assert get_mask_card_number(fixture_for_mask) == "1234 56** **** 3456"


def test_for_atypical_numbers():
    assert get_mask_card_number("!@#$%^&*()--===") == "Error: invalid number format"


def test_for_an_empty_value():
    assert get_mask_card_number("") == "Error: invalid number format"


def test_get_mask_account(fixture_for_mask):
    assert get_mask_account(fixture_for_mask) == "**7890"


def test_for_atypical_account():
    assert get_mask_account("!@#$$%^^^&^%$") == "Error: invalid account format"


def test_for_incorrect_num_len():
    assert get_mask_account("1234567890") == "Error: invalid account format"