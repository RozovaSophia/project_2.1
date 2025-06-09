import typing
from colorsys import yiq_to_rgb

transactions = [
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
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
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
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list, currency: str) -> typing.Any:
    """функция, которая фильтрует транзакции в зависимости от валюты"""
    filter_dict = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    if not filter_dict:
        yield "There is no required currency in transactions"
    else:
        yield from filter_dict


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, currency=input("Enter the currency: "))
    transactions_list = list(usd_transactions)
    if transactions_list != ['There is no required currency in transactions']:
        for item in transactions_list:
            print(item)
    else:
        print(" ".join(list(transactions_list)))


def transaction_descriptions(transactions: typing.List[dict]) -> typing.Any:
    """функция, которая выводит описание каждой транзакции по ключу ["description"]"""
    acceptable_values = [
        "Перевод организации", "Перевод со счета на счет",
        "Перевод со счета на счет", "Перевод с карты на карту",
        "Перевод организации"
    ]
    try:
        filter_descriptions = [*(x["description"] for x in transactions if x["description"] in acceptable_values)]
        if not filter_descriptions:
            yield "No correct description of the transaction was found"
        else:
            yield from filter_descriptions
    except:
        yield "Incorrect data entered"


if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    descriptions_list = list(descriptions)
    if descriptions_list != ['No correct description of the transaction was found'] or ["Incorrect data entered"]:
        for item in descriptions_list:
            print(item)
    else:
        print(" ".join(list(descriptions_list)))


def card_number_generator(start: int, stop: int) -> typing.Any:
    """функция, которая принимает начальное и конечное значение и
    генерирует номер карты в формате XXXX XXXX XXXX XXXX"""
    try:
        if start > stop or start < 0:
            yield "Incorrect data entered"
        else:
            result = [str(x) for x in range(start, stop + 1)]
            formatted_number = "{} {} {} {}"
            new_number = [formatted_number.format(х[:4], х[4:8], х[8:12], х[12:16]) for х in [x.zfill(16) for x in result]]
            yield from new_number
    except:
            yield "Incorrect data entered"



if __name__ == "__main__":
    try:
        for card_number in card_number_generator(1, 5):
            print(card_number)
    except:
        print("Please provide both start and stop arguments")
