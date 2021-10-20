import pytest
from main_002 import del_find_el


@pytest.mark.parametrize('input_list, input_el, result_list', [
    pytest.param(list([1, 2, 3]), int(3), list([1, 2])),
    pytest.param(list([2, 2, 1]), int(2), list([2, 1])),
    pytest.param(list([15, 10, 25, 20]), int(10), list([15, 25, 20]))
])
def test_del_find_el_valid(input_list: list, input_el: int, result_list: list):
    """Позитивная проверка удаления элемента в том случае, если значение присутствует в списке."""
    assert del_find_el(input_list, input_el) == result_list, 'Элемент из списка не удален!'


@pytest.mark.parametrize('input_list, input_el, result_list', [
    pytest.param(list([0, 1, 2, 3]), int(4), list([0, 1, 2, 3])),
    pytest.param(list([10, 15, 20, 25]), int(5), list([10, 15, 20, 25])),
])
def test_not_find_el_valid(input_list: list, input_el: int, result_list: list):
    """Позитивная проверка, если значение элемента не присутствует в списке."""
    assert del_find_el(input_list, input_el) == result_list, 'Элемент присутствует в списке!'
