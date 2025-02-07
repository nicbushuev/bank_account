
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_bank_information: str) -> str:
    """Функция маскирует строковую входящую информацию о карте или счете"""

    cleaned_input = input_bank_information.strip()
    parts = cleaned_input.split()

    if len(parts) < 2:
        raise ValueError("Формат неверный, введите формат карта/счет номер")

    card_type = parts[0].casefold()
    number = "".join(parts[1:]).replace(" ", "")

    if not number.isdigit():
        raise ValueError("Формат неверный! В номере карты/счета должны быть только цифры")

    if card_type in ("visa", "mastercard", "mir", "maestro"):
        if len(number) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")
        masked_number = get_mask_card_number(number)
    elif len(number) == 0:
        raise ValueError("Номер не может быть пустым")
    elif card_type == "счет":
        if len(number) < 6:
            raise ValueError("Номер счёта слишком короткий")
        masked_number = get_mask_account(number)
    else:
        raise ValueError("Неверный формат ввода.")

    return f"{parts[0]} {masked_number}"

def get_date(date_string: str) -> str:
    """Преобразует дату в новый формат"""

    date_obj = datetime.fromisoformat(date_string)
    return f"{date_obj.day:02}.{date_obj.month:02}.{date_obj.year}"
