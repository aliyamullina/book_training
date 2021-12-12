import pytest
from story.loops_commands_if import del_negative_numbers, total_negative_numbers, output_description


@pytest.mark.parametrize('x, result', [
    pytest.param(list([1, 3, 5, 0, -1, 3, -2]), list([1, 3, 5, 0, 3])),
    pytest.param(list([-10, 23, -15, 10, 1, -2]), list([23, 10, 1]))
])
def test_del_negative_numbers(x: list, result: list):
    """Проверка удаления всех отрицательных чисел из списка."""
    assert del_negative_numbers(x) == result, 'Отрицательные числа не удалены!'


@pytest.mark.parametrize('y, result', [
    pytest.param(list([[1, -1, 0], [2, 5, -9], [-2, -3, 0]]), 4),
    pytest.param(list([[1, 1, 0], [2, 5, 9], [-2, -3, 0]]), 2)
])
def test_total_negative_numbers(y: list, result: int):
    """Проверка подсчета общего количества отрицательных чисел в списке."""
    assert total_negative_numbers(y) == result, 'Не верное количество отрицательных чисел!'


@pytest.mark.parametrize('x, result', [
    pytest.param(-10, 'very low'),
    pytest.param(-4, 'low'),
    pytest.param(0, 'neutral'),
    pytest.param(3, 'high'),
    pytest.param(10, 'very high'),
])
def test_output_description(x: int, result):
    """Проверка вывода описания в зависимости от диапазона."""
    assert output_description(x) == result, 'Не верное описание!'
