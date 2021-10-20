import pytest
from main import sort_by_second_el


@pytest.mark.parametrize('input_list, result_list', [
    pytest.param(list([[1, 2, 3], [2, 1, 3], [4, 0, 1]]), list([[4, 0, 1], [2, 1, 3], [1, 2, 3]])),
    pytest.param(list([[6, 5, 4], [4, 3, 2], [5, 4, 3]]), list([[4, 3, 2], [5, 4, 3], [6, 5, 4]])),
    pytest.param(list([[5, 4], [3, 2], [4, 3]]), list([[3, 2], [4, 3], [5, 4]])),
    pytest.param(list([[10, 15], [17, 20], [12, 10]]), list([[12, 10], [10, 15], [17, 20]])),
])
def test_sort_by_second_el_valid(input_list, result_list):
    """Позитивная проверка сортировки списка по второму элементу каждого списка."""
    assert sort_by_second_el(input_list) == result_list, 'Сортировка по второму элементу списка не произведена!'
