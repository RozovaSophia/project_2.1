import json
import logging
import os

app_logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
log_dir = os.path.join(project_root, "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, "example.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)

app_logger.info("Программа запущена")


def get_fin_transactions():
    """Считывает файл json в папке data и выводит содержимое"""
    try:
        with open(r"../data/operations.json", "r", encoding="utf-8") as f:  # Откройте файл для чтения
            data = json.load(f)  # Загрузите JSON из файла
            if not data:
                app_logger.warning("В данном файле отсутствуют данные")
                return []
        app_logger.info("Функция выполнена успешно")
        return data
    except FileNotFoundError:
        app_logger.error("Файл '../data/operations.json' не найден")
        return None


if __name__ == "__main__":
    result = get_fin_transactions()
    print(result)
