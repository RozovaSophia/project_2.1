import typing

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card(universal_fixture: typing.Any) -> typing.Any:
    assert get_mask_card_number(universal_fixture) == None


def test_for_atypical_numbers() -> None:
    assert get_mask_card_number("!@#$%^&*()--===") == None


def test_for_an_empty_value() -> None:
    assert get_mask_card_number("") == None


def test_get_mask_account(universal_fixture: typing.Any) -> typing.Any:
    assert get_mask_account(universal_fixture) == None


def test_for_atypical_account() -> None:
    assert get_mask_account("!@#$$%^^^&^%$") == None


def test_for_incorrect_num_len() -> None:
    assert get_mask_account("1234567890") == None
