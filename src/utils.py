import json

def get_fin_transactions():
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

if __name__ == '__main__':
    result = get_fin_transactions()
    print(result)