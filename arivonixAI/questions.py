def group_consecutive(arr):
    '''
    Groups consecutive integers from a sorted list into sublists.

    Args:
        nums (list[int]): A sorted list of integers.

    Returns:
        list[list[int]]: A list of sublists where each sublist contains
                         consecutive numbers from the input.

    Example:
        >>> group_consecutive([1, 2, 3, 6, 7, 9, 11, 12])
        [[1, 2, 3], [6, 7], [9], [11, 12]]
    '''

    if not arr:
        return []
    
    result = []
    current = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            current.append(arr[i])
        else:
            result.append(current)
            current = [arr[i]]
    result.append(current)
    return result

testcases = [[], [-1], [1, 2, 3, 6, 7, 8, 9, 11, 12]]
print([group_consecutive(x) for x in testcases])