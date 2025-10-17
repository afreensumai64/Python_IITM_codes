def char_count(s: str) -> dict:
    """
    Returns a dictionary with count of each character in the string.

    Args:
        s (str): The input string.

    Returns:
        dict: Dictionary of character: frequency.

    Example:
        >>> char_count("aabbcc")
        {'a': 2, 'b': 2, 'c': 2}
    """
    result = {}
    for char in s:
        result[char] = result.get(char,0)+1
    return result
print(char_count("aabbcc"))