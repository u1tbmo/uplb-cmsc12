def listsum(numlist: list[int], size: int) -> int:
    """Gets the sum of a list of numbers.
    Args:
        numlist (list[int]): The list of numbers.
        size (int): The number of elements in numlist.

    Returns:
        int: The sum of the list.
    """
    # --Base Case--
    # If the list is empty.
    if size == 0:
        return 0
    # If the list contains a single element.
    elif size == 1:
        return numlist[0]

    # Get the Halfway Point
    # So we'll know where to divide the list in half.
    mid = size // 2

    # --Recursive Step--
    # Add the sum of the left side with the sum of the right side.
    return listsum(numlist[:mid], mid) + listsum(numlist[mid:], size - mid)


numbers = [3, 5, 4, 1, 7, 2, 9, 8, 0, 6]
print(listsum(numbers, len(numbers)))
