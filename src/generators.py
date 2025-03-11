
def filter_by_currency(transactions: list, str_currency: str):
	"""Функция, фильтрующая транзакции по заданной валюте"""
	for transaction in transactions:
		try:
			if transaction['operationAmount']['currency']['code'] == str_currency:
				yield transaction
		except KeyError:
			continue



