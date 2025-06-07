import pytest
from src.widget import mask_account_card
from src.widget import get_date


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


@pytest.mark.parametrize("value, expected_result", [
    ("МИР 1234567890123456", "МИР 1234 56** **** 3456"),
    ("Mastercard 0934567890123453", "Mastercard 0934 56** **** 3453"),
    ("Счет 09876543210987654321", "Счет **4321"),
    ("Счет 12345678901234567890", "Счет **7890")
])
def test_mask_ac_card_advanced(value, expected_result):
    assert mask_account_card(value) == expected_result

def test_for_atypical_number():
    assert mask_account_card("!@#$%^&*()") == "Error: invalid number or account format"
    assert mask_account_card("") == "Error: invalid number or account format"


def test_get_date():
    assert get_date("2025-04-11T02:26:18.671407") == "11.04.2025"

def test_for_atypical_date(fixture_for_date):
    assert get_date(fixture_for_date) == "07.12.3034"

def test_for_empty_date():
    assert get_date("") == "Please, enter the date in the 'year-month-day' format"