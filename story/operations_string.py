import logging


def operation_string(user_list: list):
    """Удаление только двойных кавычек из каждого элемента в списке строк."""
    logging.info('{0} входящий список'.format(user_list))
    list_b = []
    for i in user_list:
        list_b.append(i.strip('"'))
    logging.info('{0} список без кавычек'.format(list_b))
    return list_b


def operation_string_mississippi(user_word: str):
    """Найти и удалить последнюю букву p в слове Mississippi."""
    logging.info('{0} входящее слово'.format(user_word))
    position_el = user_word.rfind('p')
    user_word = user_word[:position_el] + user_word[position_el+1:]
    logging.info('{0} измененное слово'.format(user_word))
    return user_word
