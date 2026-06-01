"""Module Level Docstring"""

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    factors = []
    
    for i in range(1 , number):
        if number % i == 0:
            factors.append(i)
                
    for factor in factors:
        aliquot_sum += factor
        
    if aliquot_sum == number:
        return "perfect"
    elif number < aliquot_sum:
        return "abundant"
    else:
        return "deficient"
