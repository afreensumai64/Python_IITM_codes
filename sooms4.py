def count_unique_pairs(nums: list, target: int) -> int:
    """
    Count the number of unique pairs (a, b) such that a + b == target.

    Args:
        nums (list): List of integers.
        target (int): Target sum.

    Returns:
        int: Number of unique pairs that sum to target.

    Example:
        >>> count_unique_pairs([1, 5, 7, -1, 5], 6)
        2
    """
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num,complement))))
        seen.add(num)
    return len(pairs)
print(count_unique_pairs([1, 5, 7, -1, 5], 6))