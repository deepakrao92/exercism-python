"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """ Returns whether the given lists are sublists of each other or not.

    :param list_one (list)
    :param list_two (list)

    :returns: Enum
    """
    if list_one == list_two:
        return EQUAL
    
    if list_two == []:
        return SUPERLIST
    
    if list_one == []:
        return SUBLIST

    # Sublist Slicing
    if len(list_one) < len(list_two):
        for idx in range(0, len(list_two) - len(list_one) + 1):
            if list_one == (list_two[idx:idx + len(list_one)]):
                return SUBLIST
    
    if len(list_one) > len(list_two):
        for idx in range(0, len(list_one) - len(list_two) + 1):
            if list_two == (list_one[idx:idx + len(list_two)]):
                return SUPERLIST

    return UNEQUAL
