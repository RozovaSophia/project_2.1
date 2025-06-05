def get_mask_card_number(card_number: str) -> str:
    # функция, которая принимает номер карты, и возвращает ее маску
    formatted_number = card_number[:4] + " " + card_number[6:8] + "** **** " + card_number[-4:]
    return formatted_number


result = get_mask_card_number(input("Enter card number: "))
print(result)


def get_mask_account(account: str) -> str:
    # функция, которая принимает номер счета, и возвращает его маску
    mask_account = account.replace(account[0:16], "**")
    return mask_account


result = get_mask_account(input("Enter account: "))
print(result)
