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