import requests
from src.utils import get_fin_transactions

headers= {
  "apikey": "A2L53ElgBES9MUePDb46QBpaw10bkvzz"
}

def return_amount(data) -> float:
    for transaction in data:
        if transaction['operationAmount']['currency']['code'] != "RUB":
            from_ = transaction['operationAmount']['currency']['code']
            amount = transaction['operationAmount']['amount']
            response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}", headers=headers)
            yield response.json()

if __name__ == '__main__':
    result = return_amount(data=get_fin_transactions())
    print(next(result))

