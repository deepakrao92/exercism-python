"""module level docstring"""

def is_valid(isbn):
    """Check if given string contains 10 digits"""
    _isbn = isbn.upper().replace("-", "")
    
    if not len(_isbn) == 10:
        return False
    
    res_isbn = 0
    multiplier = 10
    
    for idx, digit in enumerate(_isbn):
        if digit == "X" and idx == 9:
            res_isbn += 10 * multiplier
        elif digit.isdigit():
            res_isbn += int(digit) * multiplier
        else:
            return False
        
        multiplier -= 1
    
    return (res_isbn % 11 == 0)
