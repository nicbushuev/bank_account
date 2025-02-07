import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('input_string, expected', [
	('Visa 1111222233334444', 'Visa 1111 22** **** 4444'),
	('Mastercard 1234123412341234', 'Mastercard 1234 12** **** 1234'),
	('Mir 0123456789012345', 'Mir 0123 45** **** 2345'),
	('Maestro 0000111122223333','Maestro 0000 11** **** 3333')

])


def test_mask_account_card_if_card(input_string: str,expected: str):
	"""Проверка входной информации о карте"""
	assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("Счет 0123456789", "Счет **6789"),
    ("Счет 123123123", "Счет **3123"),
])


def test_mask_account_if_account(input_string: str, expected: str):
	"""Проверка входной информации о счете"""
	assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("Visa 1234123412341234", "Visa 1234 12** **** 1234"),
    ("Mastercard 9876543210987654", "Mastercard 9876 54** **** 7654"),
    ("mir 1111222233334444", "mir 1111 22** **** 4444"),
    ("Счет 123456789012", "Счет **9012"),
    ("Счет 987654321098", "Счет **1098"),
])


def test_mask_account_card_valid(input_string: str, expected: str):
	"""Проверка правильного определения типа карты или счета"""
	assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("input_string, message_error", [
	("Visa Avis 1231231231221", "Формат неверный, введите формат карта/счет номер"),
	("Счет Аббабабаба", "Формат неверный! В номере карты/счета должны быть только цифры"),
	("Mastercard 12341234123412341234", "Номер карты должен состоять из 16 цифр"),
	("Счет 123","Номер счёта слишком короткий"),
	("asdasdasds","Неверный формат ввода."),
	("", "Номер не может быть пустым")

])

def test_account_card_error(input_string: str, message_error: str):
	"""Отработка негативных тестов"""
	with pytest.raises(ValueError):
		mask_account_card(input_string)


@pytest.mark.parametrize('input_date, expected', [
	('2023-12-11T01:33:01.123456', '11.12.2023'),
	('2000-01-01T02:12:03.232343', '01.01.2000'),
	('1990-02-03T04:32:01.123123', '03.02.1990'),
	("2024-03-11T02:26:18.671407", '11.03.2024')
])

def test_get_date_positive(input_date: str, expected: str):
	"""Проверка дат на верное форматирование под заданный стандарт"""
	assert get_date(input_date) == expected


@pytest.mark.parametrize('input_date', [
	"07.02.2024",
	"2024/02/01",
	"2020-1-1",
    "2024-13-01",
    "0000-00-00",
    "aa-aa-aaaaa",
    "2019-01",
    "2010",

])

def test_get_date_negative(input_date: str):
	with pytest.raises(ValueError):
		get_date(input_date)





