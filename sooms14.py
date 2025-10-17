def max_product_of_two(nums: list) -> int:
    """
    Returns the maximum product from any two distinct elements in the list.

    Args:
        nums (list): List of integers.

    Returns:
        int: Maximum product.

    Example:
        >>> max_product_of_two([3, 5, -2, 9])
        45
    """
    nums.sort()
    product1 = nums[-1]*nums[-2]
    product2 = nums[0]*nums[1]
    return max(product1,product2)
print(max_product_of_two([3, 5, -2, 9]))
      