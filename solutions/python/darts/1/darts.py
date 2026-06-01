"""Module level docstring"""

def score(x, y):
    """ Calculate and return points scored based on dart position"""
    OUTER_CIRCLE = 10
    MIDDLE_CIRCLE = 5
    INNER_CIRCLE = 1

    radius = (x**2 + y**2) ** 0.5

    if radius > OUTER_CIRCLE:
        return 0
    elif MIDDLE_CIRCLE < radius <= OUTER_CIRCLE:
        return 1
    elif INNER_CIRCLE < radius <= MIDDLE_CIRCLE:
        return 5
    elif radius <= INNER_CIRCLE:
        return 10
