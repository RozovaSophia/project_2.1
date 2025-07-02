import json
import logging
import os

app_logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
log_file_path = os.path.join(project_root, "logs", "example.log")
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)

app_logger.debug("json файл считан успешно")
app_logger.info("Подключение к базе данных установлено")
app_logger.warning("Используется устаревшая функция get_fin_transactions()")
app_logger.error("Ошибка при обработке файла")
app_logger.critical("Повреждение данных обнаружено! Завершение работы...")


def get_fin_transactions():
    """Считывает файл json в папке data и выводит содержимое"""
    try:
        with open(r"..\data\operations.json", "r", encoding="utf-8") as f:  # Откройте файл для чтения
            data = json.load(f)  # Загрузите JSON из файла
            if not data:
                return []
        return data
    except FileNotFoundError:
        return r"Файл '..\data\operations.json' не найден"
    except json.JSONDecodeError as e:
        return f"Ошибка декодирования JSON: {e}"


if __name__ == "__main__":
    result = get_fin_transactions()
    print(result)
