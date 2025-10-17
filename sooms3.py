def most_frequent_char(s: str) -> str:
    """
    Find the character that appears most frequently in the given string.

    Args:
        s (str): Input string.

    Returns:
        str: Character with the highest frequency. If tie, return the first one.

    Example:
        >>> most_frequent_char("apple")
        'p'
    """
    freq = {}
    for char in s:
        freq[char]=freq.get(char,0)+1
        max_freq = max(freq.values())
        for char in s:
            if freq[char]== max_freq:
               return char
print(most_frequent_char("apple"))           
