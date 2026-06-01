"""Module level docstring"""

RES_COL =  {
        "black"  : 0,
        "brown"  : 1,
        "red"    : 2,
        "orange" : 3,
        "yellow" : 4,
        "green"  : 5,
        "blue"   : 6,
        "violet" : 7,
        "grey"   : 8,
        "white"  : 9  
}

def color_code(color: str) -> int:
    """Returns the color code of resistance band"""
    if color in RES_COL.keys():
        return RES_COL[color]
    raise KeyError


def colors() -> list:
    """Returns list of resistance band colors"""
    return list(RES_COL.keys())
