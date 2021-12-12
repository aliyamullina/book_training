import pytest
from io import StringIO
from story.create_dict import create_dict, find_from_dict


@pytest.mark.parametrize('name_age, result', [
    pytest.param(list(['Маша', '10', 'Ира', '9', 'Кристина', '11']), dict({'Маша': 10, 'Ира': 9, 'Кристина': 11})),
    pytest.param(list(['Александр', '18', 'Анна', '19', 'Яна', '20']), dict({'Александр': 18, 'Анна': 19, 'Яна': 20})),
])
def test_create_dict(monkeypatch, name_age: list, result: dict):
    """Проверка создания словаря имя-возраст."""
    elem_inputs = StringIO('\n'.join(name_age))
    monkeypatch.setattr('sys.stdin', elem_inputs)
    assert create_dict() == result, 'Неправильный словарь!'


@pytest.mark.parametrize('name_age, name_to_search, found_age', [
    pytest.param(dict({'Маша': 10, 'Ира': 9, 'Кристина': 11}), 'Ира', 9),
    pytest.param(dict({'Александр': 18, 'Анна': 19, 'Яна': 18}), 'Яна', 18),
])
def test_find_from_dict(monkeypatch, name_age: dict, name_to_search: str, found_age: int):
    """Проверка поиска возраста по имени в словаре."""
    elem_inputs = StringIO(name_to_search + '\n')
    monkeypatch.setattr('sys.stdin', elem_inputs)
    assert find_from_dict(name_age) == found_age, 'Неправильный возраст!'
