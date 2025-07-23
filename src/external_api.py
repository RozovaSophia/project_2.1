import json
import os

import requests
from dotenv import load_dotenv

from src.utils import get_fin_transactions

load_dotenv()

api_key = os.getenv("API_KEY")

headers = {"apikey": f"{api_key}"}


def return_amount(transactions):
    try:
        converted_transactions = []
        for transaction in transactions:
            if transaction:
                if transaction["operationAmount"]["currency"]["code"] == "RUB":
                    converted_transactions.append(transaction)
                elif transaction["operationAmount"]["currency"]["code"] == "USD":
                    have = transaction["operationAmount"]["currency"]["code"]
                    amount = transaction["operationAmount"]["amount"]
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={have}&amount={amount}"
                    response = requests.get(url, headers=headers)
                    data = json.loads(response.text)
                    print(data)
                    transaction["operationAmount"]["currency"]["code"] = "RUB"
                    transaction["operationAmount"]["currency"]["name"] = "руб."
                    transaction["operationAmount"]["amount"] = round(float(data["result"]), 2)
                    converted_transactions.append(transaction)
        return converted_transactions
    except Exception as e:
        print(e)


if __name__ == "__main__":
    transactions = get_fin_transactions()
    result = return_amount(transactions)
    print(result)
