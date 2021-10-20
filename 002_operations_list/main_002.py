import logging


def del_find_el(user_list: list, user_el: int):
    """Удаление элемента в том случае, если значение присутствует в списке."""
    logging.info('%s входящий список, ' % user_list + '%s входящий элемент' % user_el)
    if user_el in user_list:
        user_list.remove(user_el)
        logging.info('{0} измененный список'.format(user_list))
        return user_list
    else:
        logging.info('{0} возвращаемый список'.format(user_list))
        return user_list
