def count_char_types(text: str) -> dict:
    """
    Count the number of letters, digits, and spaces in a string.

    Args:
        text (str): The input string.

    Returns:
        dict: Dictionary with counts of 'letters', 'digits', and 'spaces'.

    Example:
        >>> count_char_types("Hi 123 there")
        {'letters': 6, 'digits': 3, 'spaces': 2}
    """
    result = {'letters': 0, 'digits':0,'spaces':0}
    for char in text:
        if char.isalpha():
            result['letters']+=1
        elif char.isdigit():
            result['digits']+=1
        elif char.isspace():
            result['spaces']+=1
    return result
print(count_char_types("Hi 123 there"))