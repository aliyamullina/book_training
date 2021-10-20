import copy
import logging


def copy_list(user_list: list):
    """Создание копии y входящего списка."""
    logging.info('{0} входящий список'.format(user_list))
    copy_user_list = copy.deepcopy(user_list)
    logging.info('{0} копия входящего списка'.format(copy_user_list))
    return copy_user_list
