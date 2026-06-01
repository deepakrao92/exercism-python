"""Module level docstring"""

def color_code(color: str) -> int:
    """Returns the color code of resistance band"""
    for idx, value in enumerate(colors()):
        if value == color:
            return idx


def colors() -> list:
    """Returns list of resistance band colors"""
    return [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"  
    ]
