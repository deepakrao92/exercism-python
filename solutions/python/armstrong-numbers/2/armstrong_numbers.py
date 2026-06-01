""" Helper function to detect Armstrong number """

def is_armstrong_number(number) -> bool:
    """
    Returns whether a given number is an Armstrong number

    Parameters:
        number(int): Given user input to check for Armstrong condition

    Returns:
        bool: whether the given number is an Armstrong number or not
    
    """
    temp = number
    no_of_digits = 0

    # Count the digits in number
    while temp > 0:
        temp = temp // 10
        no_of_digits += 1

    temp = number
    total = 0

    # Add the digits multiplied by number of digits
    while temp > 0:
        digit = temp % 10
        total += digit ** no_of_digits
        temp = temp // 10

    return total == number
