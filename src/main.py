import datetime

from filtering_transactions import process_bank_search
from src.external_api import return_amount
from src.masks import get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.transactions import reads_financial_transactions, reads_financial_transactions_excel
from src.utils import get_fin_transactions


def main(data: list[dict]):

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
                # print([i["date"] for i in filtered_data])
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


#     while True:
#         print("Выводить только рублевые транзакции? Да/Нет")
#         user_choice = input().capitalize()
#         filtered_by_amount = []
#         if user_choice == "Да":
#             for transaction in filtered_data:
#                 result = return_amount(transaction)
#                 filtered_by_amount.append(result)
#             print(filtered_by_amount)
#             break
#         elif user_choice == "Нет":
#             break
#         else:
#             print("Повторите попытку.")
#
#     while True:
#         print("Отфильтровать список транзакций по определенному слову в описании?")
#         user_choice = input().capitalize()
#         if user_choice == "Да":
#             filtered_data = process_bank_search(filtered_data, search=input("Введите слово: "))
#             break
#         elif user_choice == "Нет":
#             break
#         else:
#             print("Повторите попытку.")
#
#         def
#
#     print(f"""
#     Распечатываю итоговый список транзакций...
#     Всего банковских операций в выборке: {len(filtered_data)}
# #
# # 08.12.2019 Открытие вклада
# # Счет **4321
# # Сумма: 40542 руб.
# #
# # 12.11.2019 Перевод с карты на карту
# # MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# # Сумма: 130 USD
# #
# # 18.07.2018 Перевод организации
# # Visa Platinum 7492 65** **** 7202 -> Счет **0034
# # Сумма: 8390 руб.
# #
# # 03.06.2018 Перевод со счета на счет
# # Счет **2935 -> Счет **4321
# # Сумма: 8200 EUR
# #     """)


if __name__ == "__main__":
    main(data="data")
