""" Module level docstring"""
import string

def is_pangram(sentence) -> bool:
    """
    Checks whether a given sentence is a pangram or not.
    :param1 sentence(str)
    returns boolean
    """
    english_alphabet = set(string.ascii_lowercase)
    
    for letter in english_alphabet:
        if letter not in sentence.lower():
            return False
        
    return True