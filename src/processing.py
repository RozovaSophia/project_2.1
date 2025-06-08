import typing


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> typing.Any:
    """функция принимает список словарей, фильтрует их и записывает отфильтрованные по ключу слова в новый список"""
    filtered_list = []
    for dict in list_of_dict:
        if dict.get("state") == state:
            filtered_list.append(dict)
    if not filtered_list:
        return "No values were found for this key"
    else:
        return filtered_list


if __name__ == "__main__":
    result = filter_by_state(list_of_dict=eval(input("Enter the list of dictionaries: ")))
    print(result)


def sort_by_date(list_of_dict: list, descending: bool = True) -> list:
    """функция принимает список словарей, сортирует их даты по убыванию (сначала самые новые)"""
    sorted_date = sorted(list_of_dict, key=lambda dict: dict.get("date", 0), reverse=descending)
    return sorted_date


if __name__ == "__main__":
    result = sort_by_date(list_of_dict=eval(input("Enter the list of dictionaries: ")))
    print(result)
