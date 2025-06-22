import os
from dotenv import load_dotenv
import requests
from src.utils import get_fin_transactions

load_dotenv()

api_key = os.getenv('API_KEY')

headers= {
    "apikey": f"{api_key}"
}

def return_amount(data):
    for transaction in data:
            if transaction['operationAmount']['currency']['code'] != "RUB":
                from_ = transaction['operationAmount']['currency']['code']
                amount = transaction['operationAmount']['amount']
                response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}", headers=headers)
                result = response.json()
                converted_amount = result['result']
                yield converted_amount
            else:
                yield transaction['operationAmount']['amount']

if __name__ == '__main__':
    result = return_amount(data=get_fin_transactions())
    print(next(result))


