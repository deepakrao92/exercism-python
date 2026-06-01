"""Module Level Docstring"""

def rebase(input_base, digits, output_base):
    """a tool to translate between bases"""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    input_number = 0
    result = []

    # for idx, digit in enumerate(digits[::-1]):
    #     if not 0 <= digit < input_base:
    #         raise ValueError("all digits must satisfy 0 <= d < input base")
    #     input_number += digit * input_base**idx

    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        input_number = input_number * input_base + digit

    if input_number == 0 or digits == []:
        return [0]

    while input_number > 0:
        last_digit = input_number % output_base
        result.append(last_digit)
        input_number //= output_base

    return result[::-1]
