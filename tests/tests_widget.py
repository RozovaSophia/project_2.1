import pytest
from src.widget import mask_account_card


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