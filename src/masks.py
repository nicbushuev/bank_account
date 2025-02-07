def get_mask_card_number(card_number: str) -> str:
    """Функция, возвращающая номер карты по заданной маске"""

    card_number = str(card_number)

    # Проверка условия отсутствия пробелов при вводе
    if " " in card_number:
        raise ValueError("В номере карты не должно быть пробелов")

    # Проверка количества символов карты и наличия только цифр
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает номер аккаунта по заданной маске"""

    account_number = str(account_number)

    # Проверка условия отсутствия пробелов при вводе
    if " " in account_number:
        raise ValueError("Номер аккаунта не должен содержать пробелов")

    # Проверка наличия только цифр
    if not account_number.isdigit():
        raise ValueError("Номер аккаунта должен содержать только цифры")

    return '**' + account_number[-4:]
