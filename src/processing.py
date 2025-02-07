from datetime import datetime

from src.widget import get_date


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция фильтрует входящий список словарей по значению ключа 'state'
    :param data: Список словарей для фильтрации
    :param state: Значение ключа 'state', по умолчанию 'EXECUTED'
    :return: Новый список словарей, где значение ключа 'state' совпадает с указанным
    """
    if not isinstance(data, list):
        raise TypeError("data должно быть списком словарей")


    new_filtered_list = []
    for item in data:
        if not isinstance(item, dict):
            continue

        if item.get("state") == state:
            new_filtered_list.append(item)

    return new_filtered_list


def sort_by_date(data: list, decrease: bool = False) -> list:
    """
    Функция, создающая новый список словарей с читаемым форматом дат
    :param data: Список словарей с ключем "data"
    :param decrease: Сортировка по убыванию - если TRUE, по возрастанию FALSE
    :return: Новый список словарей с датами в формате ДД.ММ.ГГГГ,
     отсортированный по дате.
    """

    new_data = []
    for item in data:
        # Копируем словарь, чтобы не менять старый
        new_item = item.copy()
        # Преобразуем дату в читаемый формат
        new_item["date"] = get_date(item["date"])
        new_data.append(new_item)

    # Сортируем новый список словарей
    sorted_data = sorted(new_data, key=lambda x: datetime.strptime(x["date"], "%d.%m.%Y"), reverse=decrease)
    return sorted_data
