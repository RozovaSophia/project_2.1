import os

import requests
from dotenv import load_dotenv

from src.utils import get_fin_transactions

load_dotenv()

api_key = os.getenv("API_KEY")

headers = {"apikey": f"{api_key}"}


def return_amount(transaction):
    """Принимает файл с данными о транзакциях и выводит сумму в рублях, если валюта не равна RUB, то конвертирует ее
    через сторонний сервис"""
    try:
        code = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]

        if code != "RUB":
            from_ = code
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}",
                headers=headers,
            )
            if response.status_code == 200:
                result = response.json()
                if "result" in result:
                    converted_amount = result["result"]
                    return converted_amount
                else:
                    print("Ошибка: Ключ 'result' отсутствует в ответе API.")
                    return None
            else:
                print(f"Ошибка API: Код состояния {response.status_code}, Ответ: {response.text}")
        else:
            return amount
    except requests.exceptions.RequestException as e:
        print(f"Ошибка подключения: {e}")
        return None
    except KeyError as e:
        print(f"Ошибка ключа в JSON: {e}")
        return None


if __name__ == "__main__":
    transactions = get_fin_transactions()

    if transactions:
        for transaction in transactions:
            result = return_amount(transaction)
            print(f"Сумма в рублях для транзакции: {result}")
    else:
        print("Нет данных о транзакциях для обработки.")
