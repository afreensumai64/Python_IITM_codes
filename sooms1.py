def reverse_each_word(sentence: str) -> str:
    """
    Reverses each word in the given sentence while maintaining word order.

    Example:
    >>> reverse_each_word("hello world")
    'olleh dlrow'
    """
    return ''.join(word [::-1]for word in sentence.split())
    
print(reverse_each_word("hello world"))
