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

def value(colors):
    """Returns the value of duo resistor band"""
    res_value = ""
    for color in colors:
        if colors.index(color) < 2:
            res_value += str(RES_COL[color])
    return int(res_value)