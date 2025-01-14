import re

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_bank_information: str) ->str:
	'''Функция, которая маскирует строковую входящую информацию о карте или счете'''

	try_match = re.search(r'(\d+)$', input_bank_information)
	if not try_match:
		raise ValueError('Формат ввода неверный! Введите верный формат Карта/счет номер')

	number = try_match.group(1)
	'''Определяем, является ли входящая банковская информация картой или счетом'''

	if input_bank_information.lower().startswith(('visa','mastercard','mir','maestro')):
		masked_number = get_mask_card_number(number)
	elif input_bank_information.lower().startswith('счет'):
		masked_number = get_mask_account(number)
	else:
		raise ValueError('Неверный формат ввода. Строка должна начинаться с названия платежной системы или слова счет')
