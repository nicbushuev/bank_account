import pytest


@pytest.fixture
def default_number():
	"""Фикстура из цифр без пробелов (16 цифр)"""
	return '1111222233334444'


@pytest.fixture
def default_number_with_spaces():
	"""Фикстура из цифр с пробелами (16 цифр)"""
	return '1111 2222 3333 4444'

@pytest.fixture
def default_number_with_letters():
	"""Фикстура из цифр и букв без пробелов (16 цифр)"""
	return '1234as1234as1234as1234'


