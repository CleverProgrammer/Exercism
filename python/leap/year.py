def is_leap_year(year):
    """
    Is it a leap year?

    year: int
    return: boolean
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False
