import logging


def last_three_elem_modification_list(user_list: list):
    """Перемещение трех последних элементов из конца в начало списка без нарушения их исходного порядка."""
    logging.info('{0} входящий список'.format(user_list))
    slice_user_list = user_list[7:]
    del user_list[7:]
    user_list[:0] = slice_user_list
    logging.info('{0} модифицированный список'.format(user_list))
    return user_list
