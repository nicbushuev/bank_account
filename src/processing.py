def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    '''Функция фильтрует входящий список словарей по ключу "state"'''

    new_filtered_list = []
    for item in data:
        if item.get("state") == state:
            new_filtered_list.append(item)
    return new_filtered_list
