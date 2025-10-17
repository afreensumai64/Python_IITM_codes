def longest_word(sentence: str) -> str:
    """
    Returns the longest word in the given sentence.
    If multiple words have the same maximum length, return the first one.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The longest word.

    Example:
        >>> longest_word("I love competitive programming")
        'competitive'
    """
    words = sentence.split()
    return max(words, key=len)
        
print(longest_word("I love competitive programming"))