import logging


def del_negative_numbers(x: list):
    """Удаление всех отрицательных чисел из списка."""
    logging.info('{0} входящий список'.format(x))
    for i in x:
        if i < 0:
            x.remove(i)
    logging.info('{0} список после удаления отрицательных чисел'.format(x))
    return x


def total_negative_numbers(y: list):
    """Подсчитать общее количество отрицательных чисел в списке."""
    count = 0
    for row in y:
        for col in row:
            if col < 0:
                count += 1
    logging.info('{0} всего отрицательных чисел {1}'.format(y, count))
    return count


def output_description(x: int):
    """Вывод описания в зависимости от диапазона."""
    if x < -5:
        desc = 'very low'
        logging.info('Число {0} это {1}'.format(x, desc))
        return desc
    elif x < 0:
        desc = 'low'
        logging.info('Число {0} это {1}'.format(x, desc))
        return desc
    elif x == 0:
        desc = 'neutral'
        logging.info('Число {0} это {1}'.format(x, desc))
        return desc
    elif x <= 5:
        desc = 'high'
        logging.info('Число {0} это {1}'.format(x, desc))
        return desc
    else:
        desc = 'very high'
        logging.info('Число {0} это {1}'.format(x, desc))
        return desc
