import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(default_number: str)-> None:
    """Проверка на правильное отображение маски карты по заданному формату"""
    assert get_mask_card_number(default_number) == "1111 22** **** 4444"


def test_get_mask_card_number_with_spaces(default_number_with_spaces: str)-> None:
    """Проверка на наличие пробелов в номере карты"""
    with pytest.raises(ValueError, match="В номере карты не должно быть пробелов"):
        get_mask_card_number(default_number_with_spaces)


def test_get_mask_card_number_len_digit(default_number_with_letters: str)-> None:
    """Проверка количества символов карты и наличия только цифр"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(default_number_with_letters)


def test_get_mask_account_number(default_number: str)-> None:
    """Проверка на правильное отображение маски счета по заданному формату"""
    assert get_mask_account(default_number) == "**4444"


def test_get_mask_account_number_with_spaces(default_number_with_spaces: str)-> None:
    """Проверка наличие пробелов в номере аккаунта"""

    with pytest.raises(ValueError, match="Номер аккаунта не должен содержать пробелов"):
        get_mask_account(default_number_with_spaces)


def test_get_mask_account_number_with_letters(default_number_with_letters: str)-> None:
    """Проверка наличия букв в номере аккаунта"""
    with pytest.raises(ValueError, match="Номер аккаунта должен содержать только цифры"):
        get_mask_account(default_number_with_letters)
