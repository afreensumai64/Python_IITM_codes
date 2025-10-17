def count_element_frequency(lst: list) -> dict:
    """
    Count the frequency of each unique element in the list.

    Args:
        lst (list): List containing elements (any hashable type).

    Returns:
        dict: Dictionary with elements as keys and their frequencies as values.

    Example:
        >>> count_element_frequency(['a', 'b', 'a', 'c', 'b', 'a'])
        {'a': 3, 'b': 2, 'c': 1}
    """
    freq = {}
    for item in lst:
      if item in freq:
         freq[item]+= 1
      else:
         freq[item]=1
    return freq
print(count_element_frequency(['a', 'b', 'a', 'c', 'b', 'a']))