def count_multiples_in_list(l: list, x: int) -> int:
    """
    Counts how many elements in the list are multiples of x.

    Args:
        l (list): List of integers.
        x (int): Number to check multiples of.

    Returns:
        int: Count of multiples.

    Examples:
        >>> count_multiples_in_list([2, 4, 5, 8, 10], 2)
        4
    """
    return sum(1 for num in l if num%x==0)
print(count_multiples_in_list([2, 4, 5, 8, 10], 2))