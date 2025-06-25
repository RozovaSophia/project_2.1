import os
import time
import random
from dotenv import load_dotenv
import requests
from src.utils import get_fin_transactions

load_dotenv()

api_key = os.getenv('API_KEY')

headers= {
    "apikey": f"{api_key}"
}

def return_amount(data):
    max_retries = 5
    for attempt in range(max_retries):
        try:
            result_transactions =[]
            for transaction in data:
                if transaction['operationAmount']['currency']['code'] != "RUB":
                    from_ = transaction['operationAmount']['currency']['code']
                    amount = transaction['operationAmount']['amount']
                    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_}&amount={amount}", headers=headers)
                    if response.status_code == 200:
                        result = response.json()
                        if 'result' in result:
                            converted_amount = result['result']
                            result_transactions.append(float(converted_amount))
                        else:
                            print("Ошибка: Ключ 'result' отсутствует в ответе API.")
                            return None
                    else:
                        print(f"Ошибка API: Код состояния {response.status_code}, Ответ: {response.text}")
                else:
                    result_transactions.append(float(transaction['operationAmount']['amount']))
            return " ".join(map(str, result_transactions))
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return None
        except ValueError as e:
            print(f"Ошибка парсинга JSON: {e}")
            return None
        except KeyError as e:
             print(f"Ошибка ключа в JSON: {e}")
             return None

    print(f"Не удалось получить данные после {max_retries} попыток.")
    return None

if __name__ == '__main__':
    result = return_amount(data=get_fin_transactions())
    print(result)


