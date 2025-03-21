def filter_by_currency(transactions: list, str_currency: str):
    """Функция, фильтрующая транзакции по заданной валюте"""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == str_currency:
                yield transaction
        except KeyError:
            continue


def transaction_descriptions(transactions: list):
    """Функция, поочередно выдающая описание каждой транзакции"""
    for transaction in transactions:
        try:
            yield transaction["description"]
        except KeyError:
            continue

    descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(description)


def card_number_generator(start: int, end: int):
    """Функция, генерирующая номера карт в заданном диапазоне"""
    # Проверка на корректность диапазона
    if start < 0 or end < 0:
        raise ValueError("Числа не могут быть отрицательными")
    if start > end:
        raise ValueError("Начальное значение не может превышать конечное")
    if start > 9999999999999999 or end > 9999999999999999:
        raise ValueError("Числа превышают максимально допустимое значение")

    for num in range(start, end + 1):
        num_string = f"{num:016d}"
        formatted_string = " ".join([num_string[0:4], num_string[4:8], num_string[8:12], num_string[12:16]])
        yield formatted_string
