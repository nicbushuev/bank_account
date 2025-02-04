from src.masks import get_mask_card_number
import pytest


def test_get_mask_card_number():
	#Проверка на правильное отображение маски по заданному формату
	assert get_mask_card_number('1111222233334444') == '1111 22** **** 4444'
	assert get_mask_card_number('1234123412341234') == '1234 12** **** 1234'


def test_get_mask_card_number_with_spaces():
	#Проверка на наличие пробелов в номере карты
	card_number = '1234 1234 1234 1234'
	with pytest.raises(ValueError, match='В номере карты не должно быть пробелов'):
		get_mask_card_number(card_number)


def test_get_mask_card_number_len_digit():
	#Проверка количества символов карты и наличия только цифр
	card_number = '1234as1234as1234as1234'
	with pytest.raises(ValueError, match='Номер карты должен состоять из 16 цифр'):
		get_mask_card_number(card_number)









