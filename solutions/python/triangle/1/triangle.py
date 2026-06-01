""" Utility functions for triangle check """
def is_valid_triangle(sides):
    """
    Returns whether a triangle is valid or not
    """
    a, b, c = sides
    return(
        a > 0 and b > 0 and c > 0 and
        a + b >= c and
        b + c >= a and
        c + a >= b
    )

def equilateral(sides):
    """
    Returns whether a triangle is equilateral or not
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b and b == c


def isosceles(sides):
    """
    Returns whether a triangle is isosceles or not
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or c == a


def scalene(sides):
    """
    Returns whether a triangle scalene or not
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a !=b and b != c and c != a
