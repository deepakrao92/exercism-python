""" Utilty function for raindrop implementation"""

def is_divisible_by_divisor(number, divisor) -> bool:
    """ Generic divisibility test function

    :param number: _description_
    :type number: int
    :param divisor: _description_
    :type divisor: int
    :return: True or False
    :rtype: bool
    """
    if number % divisor == 0:
        return True
    return False

def convert(number : int) -> str:
    """_summary_

    :param number: Number to check for
    :type number: int
    :return: A string of combinations Pling, Plang, Plong
    :rtype: str
    """

    if is_divisible_by_divisor(number, 3):
        if is_divisible_by_divisor(number, 5):
            if is_divisible_by_divisor(number, 7):
                return "PlingPlangPlong"    
            return "PlingPlang"
        if is_divisible_by_divisor(number, 7):
            return "PlingPlong"
        return "Pling"
    
    if is_divisible_by_divisor(number, 5):
        if is_divisible_by_divisor(number, 7):
            return "PlangPlong"
        return "Plang"
    
    if is_divisible_by_divisor(number, 7):
        return "Plong"

    return str(number)
