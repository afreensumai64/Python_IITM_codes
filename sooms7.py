def symmetric_difference(set1: set, set2: set) -> set:
    """
    Return the symmetric difference between two sets.

    Args:
        set1 (set): First set.
        set2 (set): Second set.

    Returns:
        set: Elements present in either set1 or set2, but not in both.

    Example:
        >>> symmetric_difference({1, 2, 3}, {3, 4})
        {1, 2, 4}
    """
    return set1^set2
print(symmetric_difference({1, 2, 3}, {3, 4}))