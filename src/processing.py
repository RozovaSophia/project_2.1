def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:
    filtered_list = []
    for dict in list_of_dict:
        for key, value in dict.items():
            if dict.get('state') == state:
                filtered_list.append(dict)
            else:
                continue
    return filtered_list

result = filter_by_state(list_of_dict=eval(input('Enter the list of dictionaries: ')))
print(result)


def sort_by_date(list_of_dict: list, ascending=True):
    for dict in list_of_dict:
        for key, value in dict.items():
            sorted_date = sorted(list_of_dict, key=lambda dict: dict.get('date', 0), reverse=ascending)
    return sorted_date
result = sort_by_date(list_of_dict=eval(input('Enter the list of dictionaries: ')))
print(result)