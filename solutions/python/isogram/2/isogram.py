""" module level docstring"""

def is_isogram(user_input):
    """ Isogram test """
    seen = set()

    for char in user_input.lower():
        if char in seen and char.isalpha():
            return False
        seen.add(char)
        
    return True