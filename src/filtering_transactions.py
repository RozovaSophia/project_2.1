import re
from collections import Counter

from src.utils import get_fin_transactions

def process_bank_search(data:list[dict], search:str)->list[dict]:
    """возвращает совпадения описания транзакции и поисковой строки"""
    matches = []
    for transaction in data:
        if transaction:
            match = re.search(f'{search}', transaction['description'], flags=re.IGNORECASE)
            if match:
                matches.append(transaction)
    return matches

if __name__ == "__main__":
    transactions = get_fin_transactions()
    result = process_bank_search(data=transactions, search=input())
    print(result)


def process_bank_operations(data:list[dict], categories:list)->dict:
    """возвращает количество введенных описаний из списка словарей файла json"""
    descriptions = []
    for transaction in data:
        if transaction:
            if transaction['description'] in categories:
                descriptions.append(transaction['description'])
    counted = Counter(descriptions)
    return dict(counted)


if __name__ == "__main__":
    transactions = get_fin_transactions()
    result = process_bank_operations(data=transactions, categories=input())
    print(result)