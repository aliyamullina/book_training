import logging


def segments_indices_list(user_list: list):
    """Получить вторую половину списка неизвестного размера."""
    logging.info('{0} входящий список'.format(user_list))
    half_list_length = int(len(user_list) / 2)
    half_user_list = user_list[half_list_length:]
    logging.info('{0} вторая половина списка'.format(half_user_list))
    return half_user_list
