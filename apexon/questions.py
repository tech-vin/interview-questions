def is_valid_parentheses(s):
    """
    Determine if a bracket string has valid/balanced parentheses.

    Supports (), {}, [] — every opening bracket must be closed in the correct order.
    Non-bracket characters (if any) are ignored.

    Args:
        s: String potentially containing '()[]{}' and other characters.

    Returns:
        True if parentheses are valid/balanced; otherwise False.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def two_sum(nums, target):
    """
    Return indices of the two numbers such that they add up to target.

    Uses a single-pass hash map.

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    seen = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], j)
        seen[x] = j
    return None


def is_palindrome_ignoring_non_alnum(s):
    """
    Check if a string is a palindrome considering only alphanumeric characters
    and ignoring case.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def top_k_frequent(nums, k):
    """
    Return the k most frequent elements from nums.

    Uses bucket sort to avoid sorting all frequency pairs.

    Complexity:
        Time: O(n) average
        Space: O(n)
    """
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for val, f in freq.items():
        buckets[f].append(val)

    res = []
    for f in range(len(buckets) - 1, 0, -1):
        for val in buckets[f]:
            res.append(val)
            if len(res) == k:
                return res
    return res


def max_profit(prices):
    """
    Best Time to Buy and Sell Stock (single transaction).

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    min_price = float('inf')
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        else:
            profit = p - min_price
            if profit > best:
                best = profit
    return best


# -----------------------------
# SAMPLE TESTS
# -----------------------------
if __name__ == "__main__":
    # Test is_valid_parentheses
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("({[]})") is True
    assert is_valid_parentheses("abc(d)e") is True

    # Test two_sum
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([1, 2, 3], 100) is None

    # Test is_palindrome_ignoring_non_alnum
    assert is_palindrome_ignoring_non_alnum("A man, a plan, a canal: Panama") is True
    assert is_palindrome_ignoring_non_alnum("race a car") is False
    assert is_palindrome_ignoring_non_alnum("No 'x' in Nixon") is True

    # Test top_k_frequent
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert set(result) == {1, 2}
    result = top_k_frequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 2)
    assert set(result) == {4, 6}
    assert top_k_frequent([1], 1) == [1]

    # Test max_profit
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2, 3, 4]) == 3

    print("✅ All tests passed successfully!")
