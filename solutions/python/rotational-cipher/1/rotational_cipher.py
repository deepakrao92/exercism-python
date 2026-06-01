"""Module Level Docstring"""

def rotate(text, key):
    """ Caesar cipher implementation. """
    if key == 0 or key == 26:
        return text
    
    cipher = []
    lower_base = ord("a") # 97 - 122
    upper_base = ord("A") # 65 - 90

    for char in text:
        if char.islower():
            new_char = chr(((ord(char) - lower_base) + key) % 26 + lower_base)
            cipher.append(new_char)
            
        elif char.isupper():
            new_char = chr(((ord(char) - upper_base) + key) % 26 + upper_base)
            cipher.append(new_char)

        else:
            cipher.append(char)

    return "".join(cipher)
