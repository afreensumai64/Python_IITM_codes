def even_length_words(sentence: str) -> list:
    """
    Returns a list of words that have even length.

    Args:
        sentence (str): Input sentence.

    Returns:
        list: List of even-length words.

    Example:
        >>> even_length_words("I love programming in Python")
        ['love', 'Python']
    """
    words = sentence.split()
    result = []
    for word in words:
        if len(word)>2 and len(word) %2==0:
            result.append(word)
    return result
print(even_length_words("I love programming in Python"))