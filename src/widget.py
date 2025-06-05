import masks


def mask_account_card(value: str) -> str:
    """функция принимает номер счета или номер карты"""
    value_splited = value.split(" ")
    new_list = []
    for symbols in value_splited:
        if symbols.isalpha():
            the_first_part = symbols
            new_list.append(the_first_part)
            """ условие записывает первую буквенную часть в список """
        else:
            if len(symbols) == 16:
                formatted_number = masks.get_mask_card_number(symbols)
                new_list.append(formatted_number)
            else:
                formatted_number = masks.get_mask_account(symbols)
                new_list.append(formatted_number)
            """ побочное условие форматирует номер в зависимости от кол-ва цифр """
        update_value = " ".join(new_list)
    return update_value


if __name__ == "__main__":
    result_1 = mask_account_card(input("Enter your account or card number: "))
    print(result_1)


def get_date(date_time: str) -> str:
    """функция принимает дату и время, форматирует их и выдает по шаблону в удобном формате"""
    times = date_time[: date_time.find("T")].split("-")
    return ".".join(times)


if __name__ == "__main__":
    result_2 = get_date(input("Enter date: "))
    print(result_2)
