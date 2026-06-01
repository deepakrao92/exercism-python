""" Utility functions for triangle check """
def is_valid_triangle(sides):
    """
    Returns whether a triangle is valid or not
    """
    side1, side2, side3 = sides
    return(
        all(side > 0 for side in sides) and
        side1 + side2 >= side3 and
        side2 + side3 >= side1 and
        side3 + side1 >= side2
    )

def equilateral(sides):
    """
    Returns whether a triangle is equilateral or not
    """
    if not is_valid_triangle(sides):
        return False
    side1, side2, side3 = sides
    return side1 == side2 and side2 == side3


def isosceles(sides):
    """
    Returns whether a triangle is isosceles or not
    """
    if not is_valid_triangle(sides):
        return False
    side1, side2, side3 = sides
    return side1 == side2 or side2 == side3 or side3 == side1


def scalene(sides):
    """
    Returns whether a triangle scalene or not
    """
    if not is_valid_triangle(sides):
        return False
    side1, side2, side3 = sides
    return side1 !=side2 and side2 != side3 and side3 != side1
