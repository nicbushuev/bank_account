import pytest

from src.generators import filter_by_currency, card_number_generator
from tests.conftest import default_invalid_transaction


@pytest.mark.parametrize("currency_code, expected_id", [
    ("USD", [1111, 2222]),  # Ожидаемые ID для USD
    ("EUR", [3333]),    # Ожидаемые ID для EUR
    ("RUB", [4444]),    # Ожидаемые ID для GBP
    ("GBP", [5555]),    # Ожидаемые ID для RUB
    ("JPY", [])    # Нет ожидаемого ID
])

def test_filter_by_currency(default_transactions_with_any_currency: list, currency_code: str, expected_id: list):
    """Фильтр транзакций по валюте"""
    result = list(filter_by_currency(default_transactions_with_any_currency,currency_code))
    result_id = [transaction["id"] for transaction in result]
    assert result_id == expected_id


def test_empty_transactions_list():
    """ Пустой список транзакций"""
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0

def test_invalid_transaction(default_invalid_transaction):
    """ Некорректная структура транзакции"""
    result = list(filter_by_currency(default_invalid_transaction, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_not_inclusive_currency(default_not_inclusive_currency):
    """ Отсутствующая валюта в транзакциях"""
    result = list(filter_by_currency(default_not_inclusive_currency,'USD'))
    assert len(result) == 0


@pytest.mark.parametrize("description, expected_description_id", [
    ("Перевод организации", [939719570,594226727]),
    ("Перевод со счета на счет", [142264268, 873106923]),
    ("Перевод с карты на карту", [895315941]),
    ("Перевод себе в карман", [])
    ])

def test_transaction_descriptions(default_transactions: list,description: str,expected_description_id: list):
    """Фильтр транзакций по описанию и сбор их ID"""
    filtered_id = [trans["id"] for trans in default_transactions if trans.get("description") == description]
    assert filtered_id == expected_description_id


@pytest.mark.parametrize("start, end, expected_card_num", [
    (1,4, [
        '0000 0000 0000 0001',  # Ожидаемые номера карт в диапазоне от 1 до 4 включительно
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004']),
    (1,2, [
        '0000 0000 0000 0001',  # Ожидаемые номера карт от 1 до 2 включительно
        '0000 0000 0000 0002']),
    (9999999999999999, 9999999999999999,[
        '9999 9999 9999 9999']),
    (0, 0, [
        '0000 0000 0000 0000']),
    (9999, 10000, [
        '0000 0000 0000 9999',
        '0000 0000 0001 0000']),
])


def test_card_number_generator(start, end, expected_card_num):
    """Генерация номеров карт валидная"""
    result = list(card_number_generator(start,end))
    assert result == expected_card_num

def test_invalid_range():
    """Неверный диапазон"""
    with pytest.raises(ValueError):
        list(card_number_generator(13, 7))


def test_negative_numbers():
    """ Отрицательные входные данные"""
    with pytest.raises(ValueError):
        list(card_number_generator(-2, 10))