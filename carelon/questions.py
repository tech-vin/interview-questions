def first_non_repeating_char(s):
    """
    Given a string `s`, return the first non-repeating character.

    A non-repeating character is defined as a character that occurs exactly once in the string.
    If there is no such character, return None.

    Examples:
        >>> first_non_repeating_char("aabc")
        'b'
        >>> first_non_repeating_char("aabbcc")
        None
        >>> first_non_repeating_char("swiss")
        'w'

    Constraints:
        - Input string can contain lowercase/uppercase letters or any ASCII character.
        - Function should run in O(n) time, where n is the length of the string.
    """
    counts = word_freq(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

def word_freq(s):
    mapping = {}
    for char in s:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1

    return mapping

testcase = ['aabc', '', 'aaa', 'aabb']
print([first_non_repeating_char(x) for x in testcase])