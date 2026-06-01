""" Utilty function for raindrop implementation"""

def convert(number : int) -> str:
    """_summary_

    :param number: Number to check for
    :type number: int
    :return: A string of combinations Pling, Plang, Plong
    :rtype: str
    """
    sounds = [
        (3, "Pling"),
        (5, "Plang"),
        (7, "Plong")
    ]

    result = ""

    for divisor, sound in sounds:
        if number % divisor == 0:
            result += sound
     
    return result or str(number)
