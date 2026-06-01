""" Module level docstring """

def reverse(text):
    """ Reverses a given string. """    
    reversed = ""
    rev_idx = len(text) -1
    
    for i in text:
        reversed += text[rev_idx]
        rev_idx -= 1
        
    return reversed
