import logging


def sort_by_second_el(user_list: list):
    """Отсортировать список по второму элементу каждого списка."""
    logging.info('{0} входящий список'.format(user_list))
    user_list.sort(key=lambda x: x[1])
    logging.info('{0} отсортированный список'.format(user_list))
    return user_list
