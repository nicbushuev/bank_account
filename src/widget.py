import re

from masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(input_bank_information: str) ->str:
	'''Функция, которая маскирует строковую входящую информацию о карте или счете'''

	try_match = re.search(r'(\d+)$', input_bank_information)
	if not try_match:
		raise ValueError('Формат ввода неверный! Введите верный формат Карта/счет номер')

	number = try_match.group(1)


	if input_bank_information.lower().startswith(('visa','mastercard','mir','maestro')):
		masked_number = get_mask_card_number(number)
	elif input_bank_information.lower().startswith('счет'):
		masked_number = get_mask_account(number)
	else:
		raise ValueError('Неверный формат ввода. Строка должна начинаться с названия платежной системы или слова счет')


	return input_bank_information.replace(number,masked_number)

def get_date(date_string: str) -> str:
	"""Преобразует дату в новый формат"""

	date_obj = datetime.fromisoformat(date_string)
	return f"{date_obj.day:02}.{date_obj.month:02}.{date_obj.year}"