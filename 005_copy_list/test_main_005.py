import pytest
from main_005 import copy_list


@pytest.mark.parametrize('user_list, result_list', [
    pytest.param(list([1, 2, 3]), list([1, 2, 3])),
    pytest.param(list(['A', 'B', 'C']), list(['A', 'B', 'C'])),
])
def test_copy_list_valid(user_list: list, result_list: list):
    """Проверка создания копии у входящего списка."""
    assert copy_list(user_list) == result_list, 'Списки не совпадают!'
