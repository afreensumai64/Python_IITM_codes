def alternate_upper(sentence: str) -> list:
    """
    Given a sentence, return a list where every alternate word starting from the first is in uppercase.

    Example:
    alternate_upper("this is a test case")
    >>> ['THIS', 'is', 'A', 'test', 'CASE']

    Args:
        sentence (str): A single string containing words separated by spaces.

    Returns:
        list: A list of words with alternate words in uppercase.
    """
    words = sentence.split()
    result = []
    for i,word in enumerate(words):
        if i %2==0:
            result.append(word.upper())
        else:
            result.append(word)
    return result
        
    
