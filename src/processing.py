def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция фильтрует входящий список словарей по значению ключа 'state'
    :param data: Список словарей для фильтрации
    :param state: Значение ключа 'state', по умолчанию 'EXECUTED'
    :return: Новый список словарей, где значение ключа 'state' совпадает с указанным
    """

    new_filtered_list = []
    for item in data:
        if item.get("state") == state:
            new_filtered_list.append(item)
    return new_filtered_list
