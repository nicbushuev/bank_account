# bank_account

## Описание:

Проект для работы с банковскими данными

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/nicbushuev/bank_account.git
```
2. Установите зависимости:
```
pip install poetry
poetry install pytest

```
## Использование:
processing.py: Функция, которая фильтрует 
входящий список словарей по значению ключа 'state'
    
sort_by_date.py: Функция, создающая новый список словарей с читаемым форматом дат

masks.py, widget.py: Функции по маскированию карты/счета

generators.py: 

Функции:
filter_by_currency - Функция, фильтрующая транзакции по заданной валюте

transaction_descriptions - Функция, поочередно выдающая описание каждой транзакции

card_number_generator - Функция, генерирующая номера карт в заданном диапазоне
## Тестирование:

В тестировании используется Pytest

test_masks: Тесты для модуля masks.py

test_processing.py: Тесты для модуля processing.py

test_widget.py: Тесты для модуля widget.py

conftest.py Модуль с фикстурами для функций тестирования

test_generators.py - Тесты для generators.py



## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).