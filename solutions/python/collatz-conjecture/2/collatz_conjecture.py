""" Utility funcion to calculate number of steps needed to reach 1 """

def steps(number):
    """
    Returns the number of steps needed to reach to 1
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    no_of_steps = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3) + 1

        no_of_steps += 1
    return no_of_steps
