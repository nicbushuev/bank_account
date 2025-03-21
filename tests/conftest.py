import pytest


@pytest.fixture
def default_number()-> str:
	"""Фикстура из цифр без пробелов (16 цифр)"""
	return '1111222233334444'


@pytest.fixture
def default_number_with_spaces()-> str:
	"""Фикстура из цифр с пробелами (16 цифр)"""
	return '1111 2222 3333 4444'

@pytest.fixture
def default_number_with_letters()-> str:
	"""Фикстура из цифр и букв без пробелов (16 цифр)"""
	return '1234as1234as1234as1234'

@pytest.fixture
def default_transactions():
	"Фикстура с произвольными входящими транзакциями для тестов"
	return(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


@pytest.fixture
def default_transactions_with_any_currency():
	"""Фикстура из транзакций с разными валютами в поле CODE"""
	return [
        {
            "id": 1111,
            "operationAmount": {
                "amount": "1",
                "currency": {"code": "USD"}
            }
        },
        {
            "id": 2222,
            "operationAmount": {
                "amount": "2",
                "currency": {"code": "USD"}
            }
        },
        {
            "id": 3333,
            "operationAmount": {
                "amount": "3",
                "currency": {"code": "EUR"}
            }
        },
        {
            "id": 4444,
            "operationAmount": {
                "amount": "4",
                "currency": {"code": "RUB"}
            }

        },
		{
			"id": 5555,
			"operationAmount": {
				"amount": "1",
				"currency": {"code": "GBP"}
			}
		}

    ]

@pytest.fixture
def default_invalid_transaction():
	"""Фикстура с неверной структурой транзакции"""
	return [
            {
                "id": 1,
                "operationAmount": {
                    "amount": "100",
                    "currency": {"code": "USD"}
                }
            },
			{
			"id": 2,
			"operationAmount": {
				"amount": "200",
				"currency": {"code": "EUR"}
			}
			},
            {
                "id": 3,
                "invalid_key": "invalid_value"
            }
        ]


@pytest.fixture
def default_not_inclusive_currency():
	"""Фикстура с отсутствующей валютой"""
	return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "JPY"}
            }
        }
    ]