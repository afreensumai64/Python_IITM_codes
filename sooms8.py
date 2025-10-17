def swap_first_last(t: tuple) -> tuple:
    """
    Swap the first and last elements of a tuple.

    Args:
        t (tuple): A tuple with at least 2 elements.

    Returns:
        tuple: A new tuple with first and last elements swapped.

    Example:
        >>> swap_first_last((1, 2, 3, 4))
        (4, 2, 3, 1)
    """

    return (t[-1],)+t[1:-1]+(t[0],)
print(swap_first_last((1, 2, 3, 4)))
