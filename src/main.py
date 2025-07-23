from pandas import Timestamp

from filtering_transactions import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.transactions import reads_financial_transactions, reads_financial_transactions_excel
from src.utils import get_fin_transactions
from src.widget import get_date, mask_account_card


def main(data: list[dict]):
    """объединяет весь функционал проекта"""

    while True:
        print(
            """
        Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла """
        )
        user_choice = int(input())
        if user_choice == 1:
            data = get_fin_transactions(file_path="../data/operations.json")
            print("Для обработки выбран JSON-файл.")
            break
        elif user_choice == 2:
            data = reads_financial_transactions("C:/Users/Thunderobot/Downloads/transactions.csv")
            print("Для обработки выбран CSV-файл.")
            break
        elif user_choice == 3:
            data = reads_financial_transactions_excel("C:/Users/Thunderobot/Downloads/transactions_excel.xlsx")
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Повторите попытку.")

    while True:
        print(
            """
        Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING """
        )
        user_choice = input().upper()
        if user_choice == "EXECUTED":
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            filtered_data = filter_by_state(data, state=user_choice)
            break
        elif user_choice == "CANCELED":
            print("Операции отфильтрованы по статусу 'CANCELED'")
            filtered_data = filter_by_state(data, state=user_choice)
            break
        elif user_choice == "PENDING":
            print("Операции отфильтрованы по статусу 'PENDING'")
            filtered_data = filter_by_state(data, state=user_choice)
            break
        else:
            print(f"Статус операции {user_choice} недоступен.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_choice = input().capitalize()
        if user_choice == "Да":
            print("Отсортировать по возрастанию или по убыванию?")
            user_choice = input().lower()
            if user_choice == "по возрастанию":
                filtered_data = sort_by_date(filtered_data, descending=False)
                break
            elif user_choice == "по убыванию":
                filtered_data = sort_by_date(filtered_data, descending=True)
                break
            else:
                print("Повторите попытку.")
        elif user_choice == "Нет":
            break
        else:
            print("Повторите попытку.")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_choice = input().capitalize()
        filtered_by_currency = []
        if user_choice == "Да":
            for transaction in filtered_data:
                currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
                if currency == "RUB" or transaction.get("currency_code", {}) == "RUB":
                    filtered_by_currency.append(transaction)
            filtered_data = filtered_by_currency
            break
        elif user_choice == "Нет":
            break
        else:
            print("Повторите попытку.")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании?")
        user_choice = input().capitalize()
        if user_choice == "Да":
            filtered_data = process_bank_search(filtered_data, search=input("Введите слово: "))
            break
        elif user_choice == "Нет":
            break
        else:
            print("Повторите попытку.")

    list_of_final_transactions = []
    for transaction in filtered_data:
        final_transactions = []
        date = get_date(transaction.get("date", {}))

        if date == "Please, enter the date in the 'year-month-day' format":
            timestamp = transaction.get("date", {})
            formatted_date = timestamp.strftime("%Y-%m-%d")
            date = get_date(formatted_date)

        final_transactions.append(date)
        description = transaction.get("description", {})
        final_transactions.append(description)

        if description == "Открытие вклада":
            account = mask_account_card(transaction.get("to", {}))
            final_transactions.append(account)

        else:
            card_1 = mask_account_card(transaction.get("from", {}))
            card_2 = mask_account_card(transaction.get("to", {}))
            operation = card_1 + " -> " + card_2
            final_transactions.append(operation)

        if transaction.get("operationAmount", 0) != 0:
            currency = transaction.get("operationAmount", {}).get("currency", {}).get("name", {})
            sum = "Сумма: " + str(transaction.get("operationAmount", {}).get("amount", {})) + " " + currency
            final_transactions.append(sum)
        else:
            currency = transaction.get("currency_name")
            sum = "Сумма: " + str(transaction.get("amount", {})) + " " + currency
            final_transactions.append(sum)
            list_of_final_transactions.append("\n" + "\n".join(final_transactions))
    print(
        f"""
    Распечатываю итоговый список транзакций...
    Всего банковских операций в выборке: {len(filtered_data)}"""
    )

    print("\n".join(list_of_final_transactions))


if __name__ == "__main__":
    main(data="data")
