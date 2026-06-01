"""Module level docstring"""

def line_up(name: str, number: int) -> str:
    """ Returns a pretty message for the customer based on ordinal number logic.
    
    :param name: str Name of customer
    :param number: int Ordinal number of customer
    
    :returns: string Formatted message for customer bill
    """
    
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")  
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
