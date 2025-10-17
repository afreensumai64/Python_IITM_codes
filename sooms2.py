def sum_of_even_squares(lst: list) -> int:
    """
    Return the sum of squares of all even numbers in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of squares of even numbers.

    Example:
        >>> sum_of_even_squares([1, 2, 3, 4])
        20
    """
   
    return sum(x**2 for x in lst if x%2==0)
print (sum_of_even_squares([1, 2, 3, 4]))