import csv
import pandas as pd


def reads_financial_transactions():
    with open('C:/Users/Thunderobot/Downloads/transactions.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        transactions = []
        for row in reader:
             transactions.append(row)
        return transactions


def reads_financial_transactions_excel():
    excel_data = pd.read_excel('C:/Users/Thunderobot/Downloads/transactions_excel.xlsx')
    transactions = []
    for index, row in excel_data.iterrows():
        transactions.append(row)
    return transactions


result_1 = reads_financial_transactions()
result_2 = reads_financial_transactions_excel()
print(result_1, result_2)