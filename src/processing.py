def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    # функция принимает список словарей, фильтрует их и записывает отфильтрованные по ключу слова в новый список
    filtered_list = []
    for dict in list_of_dict:
        for key, value in dict.items():
            if dict.get("state") == state:
                filtered_list.append(dict)
            else:
                continue
    return filtered_list


result = filter_by_state(list_of_dict=eval(input("Enter the list of dictionaries: ")))
print(result)


def sort_by_date(list_of_dict: list, descending: bool = True) -> list:
    # функция принимает список словарей, сортирует их даты по убыванию (сначала самые новые)
    for dict in list_of_dict:
        for key, value in dict.items():
            sorted_date = sorted(list_of_dict, key=lambda dict: dict.get("date", 0), reverse=descending)
    return sorted_date


result = sort_by_date(list_of_dict=eval(input("Enter the list of dictionaries: ")))
print(result)
