import pytest
import typing

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


@pytest.mark.parametrize(
    "transactions, currency, expected_result",
    [
        (transactions, "USD", [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]),
        (transactions, "RUB", [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]),
        (transactions, "JPY", []),
        (transactions, "EUR", []),
        (transactions, "", [])
    ],
)

def test_filter_by_currency(transactions: typing.List[dict], currency: str, expected_result) -> None:
    """проверяет функцию filter_by_currency, используя корректный тип данных"""
    assert filter_by_currency(transactions, currency) == expected_result


def test_filter_by_atypical_currency(universal_fixture) -> None:
    """проверяет на ошибки при вводе некорректного типа данных"""
    assert filter_by_currency(transactions, universal_fixture) == []


@pytest.mark.parametrize(
    "transactions, expected_result",
    [
        (transactions, [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
            ]),
        ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ], [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации"
            ]),
        ([
                        {
                            "id": 939719570,
                            "state": "EXECUTED",
                            "date": "2018-06-30T02:08:58.425572",
                            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                            "description": "",
                            "from": "Счет 75106830613657916952",
                            "to": "Счет 11776614605963066702",
                        },
                        {
                            "id": 142264268,
                            "state": "EXECUTED",
                            "date": "2019-04-04T23:20:05.206878",
                            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                            "description": "Perevod organizaci",
                            "from": "Счет 19708645243227258542",
                            "to": "Счет 75651667383060284188",
                        },
                        {
                            "id": 873106923,
                            "state": "EXECUTED",
                            "date": "2019-03-23T01:09:46.296404",
                            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                            "description": "ТТТТТ",
                            "from": "Счет 44812258784861134719",
                            "to": "Счет 74489636417521191160",
                        },
                        {
                            "id": 895315941,
                            "state": "EXECUTED",
                            "date": "2018-08-19T04:27:37.904916",
                            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                            "description": "???",
                            "from": "Visa Classic 6831982476737658",
                            "to": "Visa Platinum 8990922113665229",
                        },
                        {
                            "id": 594226727,
                            "state": "CANCELED",
                            "date": "2018-09-12T21:27:25.241689",
                            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                            "description": "№",
                            "from": "Visa Platinum 1246377376343588",
                            "to": "Счет 14211924144426031657",
                        },
                    ], []),
        ([], [])
    ]
)

def test_transaction_descriptions(transactions: typing.List[dict], expected_result: list) -> None:
    """проверяет функцию transaction_descriptions, используя корректный тип данных"""
    assert list(transaction_descriptions(transactions)) == expected_result


def test_transaction_random_descriptions(universal_fixture):
    """проверяет функцию transaction_descriptions, используя некорректный тип данных"""
    assert transaction_descriptions(universal_fixture) == []


@pytest.mark.parametrize(
    "start, stop, expected_result",
    [
        (0, 1, ["0000 0000 0000 0000", "0000 0000 0000 0001"]),
        (34, 35, ["0000 0000 0000 0034", "0000 0000 0000 0035"]),
        (1345, 1346, ["0000 0000 0000 1345", "0000 0000 0000 1346"]),
        (2345678, 2345679, ["0000 0000 0234 5678", "0000 0000 0234 5679"]),
        (99999999999998, 99999999999999, ["0099 9999 9999 9998", "0099 9999 9999 9999"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
        (-0, -1, ["Incorrect data entered: start must be less than or equal to stop and non-negative"])
    ],
)

def test_card_number_generator(start: int, stop: int, expected_result) -> None:
    """проверяет функцию card_number_generator, используя корректный тип данных"""
    assert list(card_number_generator(start, stop)) == expected_result


def test_atypical_card_number_generator(universal_fixture):
    """проверяет функцию card_number_generator, используя некорректный тип данных"""
    assert (list(card_number_generator(universal_fixture, universal_fixture)) ==
            ["Incorrect data entered: start and stop must be integers"])


