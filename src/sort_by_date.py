from src.widget import get_date
from datetime import datetime


def sort_by_date(data: list, decrease: bool= True) -> list:
	'''
	Функиця, создающая новый список словарей с читаемым форматом дат
	:param data: Список словарей с ключем "data"
	:param decrease: Сортировка по убыванию - если TRUE, по возрастанию FALSE
	:return: Новый список словарей с датами в формате ДД.ММ.ГГГГ, отсортированный по дате.
	'''

	new_data = []
	for item in data:
		#Копируем словарь, чтобы не менять старый
		new_item = item.copy()
		# Прербразуем дату в читаемый формат
		new_item['date'] = get_date(item['date'])
		new_data.append(new_item)

	# Сортируем новый список словарей
	sorted_data = sorted(new_data, key=lambda x: datetime.strptime(x['date'], "%d.%m.%Y"), reverse=decrease)
	return sorted_data
