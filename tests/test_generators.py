import pytest

from src.generators import filter_by_currency
from tests.conftest import default_invalid_transaction


@pytest.mark.parametrize("currency_code, expected_id", [
    ("USD", [1111, 2222]),  # Ожидаемые ID для USD
    ("EUR", [3333]),    # Ожидаемые ID для EUR
    ("RUB", [4444]),    # Ожидаемые ID для GBP
    ("GBP", [5555]),    # Ожидаемые ID для RUB
    ("JPY", []),    # Нет ожидаемого ID
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

