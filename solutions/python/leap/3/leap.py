""" Returns whether a given year is a leap year """
def leap_year(year):
    """
    Returns whether a given year is a leap year
    """
    if year % 4 == 0 and not year % 100 == 0:
        return True
    if year % 100 == 0 and year % 400 == 0:
        return True
    return False
