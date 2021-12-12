import logging


def create_dict():
    """Создание словаря имя-возраст."""
    name_age = {}
    for i in range(3):
        name = input('Имя? ')
        age = int(input('Возраст? '))
        logging.info('Введены имя: {0}, возраст: {1}.'.format(name, age))

        name_age[name] = age
    logging.info('Создан словарь: {0}'.format(name_age))
    return name_age


def find_from_dict(name_age: dict):
    """Поиск возраста по имени в словаре."""
    logging.info('Словарь: {0}'.format(name_age))
    name_choice = input('Для кого найти возраст? ')
    logging.info('Найден возраст: {1} по введенному имени: {0}.'.format(name_choice, name_age[name_choice]))
    return name_age[name_choice]
