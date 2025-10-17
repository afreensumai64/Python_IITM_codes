def shuffle_digits(num: int) -> int:
    '''Returns the number with digits shuffled in order 2413.

    Examples:
    >>> shuffle_digits(1234)
    2413
    >>> shuffle_digits(2413)
    4321
    >>> shuffle_digits(4321)
    3142
    >>> shuffle_digits(3142)
    1234

    Args:
        num (int): A 4-digit positive integer

    Returns:
        int: digit shuffled integer.
    '''
    s = str(num)
    reordered = s[1]+s[3]+s[0]+s[2]
    return(int(reordered))
    
