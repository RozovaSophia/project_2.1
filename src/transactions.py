import csv

import pandas as pd


def reads_financial_transactions(file_path, output_file_path):
    """считывает файл csv, выводит в виде списка словарей, записывает в новый файл"""
    with open(file_path, "r", encoding="UTF-8") as infile: # Открываем для чтения
        reader = csv.DictReader(infile, delimiter=";")
        data = list(reader)
        with open(output_file_path, "w", encoding="UTF-8", newline="") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=data[0].keys(), delimiter=";")
                writer.writeheader()
                writer.writerows(data)
        return data


def reads_financial_transactions_excel(file_path):
    """считывает файл excel, выводит в виде списка словарей"""
    excel_data = pd.read_excel(file_path, parse_dates=["date"])
    transactions = excel_data.to_dict(orient="records")
    return transactions


if __name__ == "__main__":
    result_1 = reads_financial_transactions("C:/Users/Thunderobot/Downloads/transactions.csv", "../data/operations.csv")
    #result_2 = reads_financial_transactions_excel("C:/Users/Thunderobot/Downloads/transactions_excel.xlsx")
    print(result_1)
