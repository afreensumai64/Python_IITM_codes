def double_ends(l: list) -> list:
    '''
    Given a list with at least two elements, return a new list where:
    - the first element is duplicated at the beginning
    - the last element is duplicated at the end

    The original list should remain unchanged.

    Examples:
    >>> double_ends([10, 20, 30])
    [10, 10, 20, 30, 30]
    >>> double_ends(['a', 'b', 'c'])
    ['a', 'a', 'b', 'c', 'c']
    >>> double_ends([1, 2])
    [1, 1, 2, 2]
    >>> double_ends([5, 6, 7, 8])
    [5, 5, 6, 7, 8, 8]

    Args:
        l (list): A list with at least two elements

    Returns:
        list: A new list with first and last elements duplicated
    '''
   
    return [l[0]]+l+[l[-1]]
    
