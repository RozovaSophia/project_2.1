import masks

def mask_account_card(value: str) -> str:
    # функция принимает номер счета или номер карты
    value_splited = value.split(" ")
    new_list = []
    for symbols in value_splited:
        if symbols.isalpha():
            the_first_part = symbols
            new_list.append(the_first_part)
        else:
            if len(symbols) == 16:
                formatted_number = get_mask_card_number(symbols)
                new_list.append(formatted_number)
            else:
                formatted_number = get_mask_account(symbols)
                new_list.append(formatted_number)
        update_value = " ".join(new_list)
    return update_value

if __name__ == "__main__":
    result_1 = mask_account_card(input("Enter your account or card number: "))
    print(result_1)