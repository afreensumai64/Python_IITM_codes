def is_leap_year(year: int) -> bool:
    """
    Determine whether the given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if it's a leap year, False otherwise.

    Example:
        >>> is_leap_year(2024)
        True
        >>> is_leap_year(1900)
        False
    """
    return year%4==0 and (year%400==0 or year%100!=0)
print(is_leap_year(2024))
print(is_leap_year(1900))
        
        
