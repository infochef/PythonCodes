def two_sum(nums, target):
    """
    Finds two indices such that the numbers at those indices add up to the target.

    Args:
        nums (list of int): List of integers.
        target (int): Target sum value.

    Returns:
        list of int: Indices of the two numbers that add up to the target.
        None: If no such pair exists.

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    prev_map = {}  # Dictionary to store numbers and their indices

    for i, n in enumerate(nums):
        diff = target - n  # Calculate the difference needed
        if diff in prev_map:
            return [prev_map[diff], i]  # Return indices if complement exists
        prev_map[n] = i  # Store the index of the current number

    return None  # Return None if no solution is found


# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
