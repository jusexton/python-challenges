import math


def is_triangle_number(number: int) -> bool:
    """
    Testing strategy inspired by the below linked math forum:
    http://mathforum.org/library/drmath/view/57162.html

    :param number: The number that will be tested
    :return: Whether the given number was a triangle number or not
    """
    number_sqrt = math.floor(math.sqrt(number * 2))
    return number == (number_sqrt * (number_sqrt + 1)) // 2
