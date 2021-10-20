import pytest
from main_006 import operation_string, operation_string_mississippi


@pytest.mark.parametrize('list_x, result_list_x', [
    pytest.param(list(['"abc"', 'def', '"ghi"', '"klm"', 'nop']), list(['abc', 'def', 'ghi', 'klm', 'nop'])),
    pytest.param(list(['"Ice cream"', 'is a', '"dessert"']), list(['Ice cream', 'is a', 'dessert'])),
])
def test_operation_string(list_x: list, result_list_x: list):
    """Проверка удаления только двойных кавычек из каждого элемента в списке строк."""
    assert operation_string(list_x) == result_list_x, 'Двойные кавычки не удалены!'


@pytest.mark.parametrize('user_word, result_word', [
    pytest.param('Mississippi', 'Mississipi'),
    pytest.param('Misisippi', 'Misisipi'),
    pytest.param('Mississipppian', 'Mississippian'),
])
def test_operation_string_mississippi(user_word: str, result_word: str):
    assert operation_string_mississippi(user_word) == result_word, 'Последняя буква p не удалена!'
