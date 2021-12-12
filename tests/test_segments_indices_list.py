import pytest
from story.segments_indices_list import segments_indices_list


@pytest.mark.parametrize('user_list, result_list', [
    pytest.param(list(['A', 'B', 'C', 'D', 'E', 'F']), list(['D', 'E', 'F'])),
    pytest.param(list(['tea', 'coffee', 'lemonade', 'cold tea']), list(['lemonade', 'cold tea'])),
    pytest.param(list([1, 2, 3, 4, 5, 6, 7, 8]), list([5, 6, 7, 8])),
    pytest.param(list([['no', 'no'], ['no', 'no'], ['yes', 'yes'], ['yes', 'yes']]), list([['yes', 'yes'], ['yes', 'yes']])),
])
def test_segments_indices_list_valid(user_list: list, result_list: list):
    """Проверка получения второй половины списка неизвестного размера."""
    assert segments_indices_list(user_list) == result_list, 'Вторая половина списка не получена!'
