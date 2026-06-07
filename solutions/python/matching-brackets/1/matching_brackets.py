""" Module level docstring"""

def is_paired(input_string: str) -> bool:    
    "Checks whether all brackets, braces and parentheses are correctly matched and nested."
    
    pairs: dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    seen: list = []
    
    for char in input_string:
        if char in pairs.values():
            seen.append(char)
            
        elif char in pairs:
            if not seen:
                return False
            
            if seen.pop() != pairs[char]:
                return False
            
    return len(seen) == 0
