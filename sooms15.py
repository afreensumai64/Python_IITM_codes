def replace_vowels_with_index(text: str) -> str:
    """
    Replace each vowel in the string with its index position.

    Example:
    replace_vowels_with_index("love")
    >>> "l1v3"

    Args:
        text (str): A string of lowercase letters.

    Returns:
        str: Modified string with indexes in vowels
    """
    vowels = 'aeiouAEIOU'
    result = ""
    for i , char in enumerate(text):
        if char in vowels:
           result += str(i)
        else:
           result += char
    return result
print(replace_vowels_with_index("love"))