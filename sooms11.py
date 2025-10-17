def replace_vowels_with_index(s: str) -> str:
    """
    Replaces each vowel in the string with its index position.

    Args:
        s (str): The input string.

    Returns:
        str: Modified string with vowels replaced by their index.

    Example:
        >>> replace_vowels_with_index("apple")
        '0ppl4'
    """
    vowels = 'aeiouAEIOU'
    result = ""
    for i,char in enumerate(s):
        if char in vowels:
            result+= str(i)
        else:
            result+=char
    return result
print(replace_vowels_with_index("apple"))
