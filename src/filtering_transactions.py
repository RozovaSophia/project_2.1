import re

from src.utils import get_fin_transactions

def process_bank_search(data:list[dict], search:str)->list[dict]:
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
