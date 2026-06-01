"""Module Level Docstring"""

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return "deficient"

    aliquot_sum = 1
    
    for num in range(2 , int(number**0.5) + 1):
        if number % num == 0:
            aliquot_sum += num
            pair = number // num
            
            if pair != num:
                aliquot_sum += pair
        
    if aliquot_sum == number:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    return "deficient"
