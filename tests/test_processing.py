import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_data, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(input_data: list, state: str, expected: list)-> None:
    """Тестирование фильтрации списка по значению state"""
    assert filter_by_state(input_data, state) == expected


@pytest.mark.parametrize(
    "input_data, state",
    [
        (None, "EXECUTED"),  # None вместо списка
        ("Not a list", "EXECUTED"),  # Строка вместо списка
        (123, "EXECUTED"),  # Число вместо списка
    ],
)
def test_filter_by_state_invalid_input(input_data: list, state: str)-> None:
    """Тестирование обработки некорректных входных данных"""
    with pytest.raises(TypeError):
        filter_by_state(input_data, state)


@pytest.mark.parametrize(
    "input_data, decrease, expected",
    [
        (
            [
                {"id": 1, "date": "2023-05-09T12:34:56.789000"},
                {"id": 2, "date": "2022-11-03T08:21:33.419441"},
                {"id": 3, "date": "2024-02-07T18:35:29.512364"},
            ],
            False,
            [
                {"id": 2, "date": "03.11.2022"},
                {"id": 1, "date": "09.05.2023"},
                {"id": 3, "date": "07.02.2024"},
            ],
        ),
        ([{"id": 1, "date": "2023-07-15T14:30:00.000000"}], False, [{"id": 1, "date": "15.07.2023"}]),
    ],
)
def test_sort_by_date(input_data: list, decrease: bool, expected: list)-> None:
    """Тестирование сортировки списка по дате"""
    assert sort_by_date(input_data, decrease) == expected


@pytest.mark.parametrize(
    "input_data",
    [
        [{"id": 1, "date": "10.01.2020"}],
        [{"id": 2, "date": "2019/02/01"}],
        [{"id": 3, "date": "15-07-2023"}],
        [{"id": 4, "date": "empty"}],
    ],
)
def test_sort_by_date_invalid_input(input_data: list)-> None:
    """Тестирование обработки некорректных дат"""
    with pytest.raises(ValueError):
        sort_by_date(input_data)
