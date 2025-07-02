import logging
import os
import typing

app_logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
log_file_path = os.path.join(project_root, "logs", "example.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)

app_logger.info("Подключение к базе данных установлено")
app_logger.warning("Используется устаревшая функция get_data()")
app_logger.error("Ошибка при обработке файла")
app_logger.critical("Повреждение данных обнаружено! Завершение работы...")


def get_mask_card_number(card_number: typing.Any) -> str:
    """функция, которая принимает номер карты, и возвращает ее маску"""
    if isinstance(card_number, str):
        if card_number.isdigit() and len(card_number) == 16:
            formatted_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
            return formatted_number
        else:
            return "Error: invalid number format"
    else:
        # return "Please, enter your card number"
        filter_list = []
        for item in card_number:
            if isinstance(item, str):
                if item.isdigit() and len(item) == 16:
                    formatted_number = item[:4] + " " + item[4:6] + "** **** " + item[-4:]
                    filter_list.append(formatted_number)
        return " ".join(filter_list)


if __name__ == "__main__":
    result = get_mask_card_number(input("Enter your number card: "))
    print(result)

    app_logger.debug("Введенный номер карты (ЗАМАСКИРОВАННЫЙ): %s", result)


def get_mask_account(account: typing.Any) -> str:
    """функция, которая принимает номер счета, и возвращает его маску"""
    if isinstance(account, str):
        if account.isdigit() and len(account) == 20:
            mask_account = account.replace(account[0:16], "**")
            return mask_account
        else:
            return "Error: invalid account format"
    else:
        # return "Please, enter your account number"
        filter_list = []
        for item in account:
            if isinstance(item, str):
                if item.isdigit() and len(item) == 20:
                    mask_account = item.replace(item[0:16], "**")
                    filter_list.append(mask_account)
        return " ".join(filter_list)


if __name__ == "__main__":
    result = get_mask_account(input("Enter account: "))
    print(result)
