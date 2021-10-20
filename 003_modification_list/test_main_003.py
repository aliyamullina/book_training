import pytest

from main_003 import last_three_elem_modification_list


@pytest.mark.parametrize('user_list, result_list', [
    pytest.param(list([4, 5, 6, 7, 8, 9, 10, 1, 2, 3]), list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
    pytest.param(list([3, 2, 1, 0, -1, -2, -3, 6, 5, 4]), list([6, 5, 4, 3, 2, 1, 0, -1, -2, -3])),
    pytest.param(list([5, 9, 10, 20, 90, 100, 0, 3, 0, 1]), list([3, 0, 1, 5, 9, 10, 20, 90, 100, 0])),
    pytest.param(list([0, 1, 0, 1, 0, 0, 1, -1, -1, -1]), list([-1, -1, -1, 0, 1, 0, 1, 0, 0, 1]))
])
def test_last_three_elem_modification_list_valid(user_list: list, result_list: list):
    """Проверка перемещения трех последних элементов из конца в начало списка без нарушения их исходного порядка."""
    assert last_three_elem_modification_list(user_list) == result_list, 'Список не модифицирован!'
