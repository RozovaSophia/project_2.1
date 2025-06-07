from src.masks import get_mask_card_number

def test_get_mask_card():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_for_atypical_numbers():
    assert get_mask_card_number("!@#$%^&*()--===") == "Error: invalid number format"


def test_for_an_empty_value():
    assert get_mask_card_number("") == "Error: invalid number format"
