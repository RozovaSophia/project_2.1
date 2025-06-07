def get_mask_card_number(card_number: str) -> str:
    """функция, которая принимает номер карты, и возвращает ее маску"""
    if card_number.isdigit() and len(card_number) == 16:
        formatted_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
        return formatted_number
    else:
        return "Error: invalid number format"



# result = get_mask_card_number(input("Enter your number card")
# print(result)


def get_mask_account(account: str) -> str:
    """функция, которая принимает номер счета, и возвращает его маску"""
    if account.isdigit() and len(account) == 20:
        mask_account = account.replace(account[0:16], "**")
        return mask_account
    else:
        return "Error: invalid account format"


# result = get_mask_account(input("Enter account: "))
# print(result)
