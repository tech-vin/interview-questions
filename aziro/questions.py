def replace_even_occurrences(s):
    """
    Replace every even-numbered occurrence (2nd, 4th, 6th, ...) of each non-space
    character in the input string with '$'. Spaces are preserved and not counted.
    
    Args:
        s: Input string.

    Returns:
        New string with replacements applied.

    Example:
        >>> replace_even_occurrences("welcome to python programming")
        'welcom$ t$ py$h$n $r$g$a$$i$$'

    Complexity:
        Time: O(n), Space: O(k + n).
    """
    counts = {}
    result = []
    for ch in s:
        if ch == " ":  # skip spaces
            result.append(" ")
            continue
        counts[ch] = counts.get(ch, 0) + 1
        if counts[ch] % 2 == 0:  # even occurrence
            result.append("$")
        else:
            result.append(ch)
    return "".join(result)


def remove_all_occurrences_of_last_char(s):
    """
    Remove ALL occurrences of the character that appears at the last position
    of the string. If the string is empty, it is returned unchanged.

    Args:
        s: Input string.

    Returns:
        The string with every occurrence of s[-1] removed.

    Example:
        remove_all_occurrences_of_last_char("Bengaluru") -> "Bengalr"

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if not s:
        return s
    last = s[-1]
    # Using replace (implemented in C) is efficient and simple.
    return s.replace(last, "")


def remove_only_final_occurrence(s):
    """
    Remove only the rightmost occurrence of the last character of the string
    (i.e., delete one character at the index of the final character's last position).

    Example:
        remove_only_final_occurrence("Bengaluru") -> "Bengalur"

    Complexity:
        Time: O(n)
        Space: O(n)
    """
    if not s:
        return s
    last = s[-1]
    idx = s.rfind(last)
    return s[:idx] + s[idx+1:]


def words_to_length_dict(words):
    """
    Convert each word in the iterable/list to uppercase and map it to its
    length (number of characters). Returns a dict with WORD.upper() -> len(word).

    Args:
        words: Iterable/list of strings.

    Returns:
        Dict mapping uppercase word to its length.

    Example:
        words_to_length_dict(["Hi","Happy","New","Year"]) -> {'HI':2,'HAPPY':5,'NEW':3,'YEAR':4}

    Complexity:
        Time: O(total characters across words)
        Space: O(w) for number of words (keys)
    """
    return {w.upper(): len(w) for w in words}


def sentence_to_words_length_dict(sentence):
    """
    Split a sentence on whitespace into words, then convert to uppercase keys
    and map to character counts. Punctuation remains attached to words unless stripped.

    Args:
        sentence: Input string sentence.

    Returns:
        Dict mapping uppercase word to its length.

    Example:
        sentence_to_words_length_dict("Hi Happy New Year") -> {'HI':2, 'HAPPY':5, 'NEW':3, 'YEAR':4}
    """
    parts = sentence.split()
    return words_to_length_dict(parts)


def merge_new_dict(d1, d2):
    """
    Merge two dictionaries and return a NEW dictionary. If a key exists in both,
    the value from d2 overrides (right-hand wins). Inputs are not modified.

    Args:
        d1: first dictionary
        d2: second dictionary

    Returns:
        new dict containing entries from both d1 and d2 (d2 overrides conflicts)

    Complexity:
        Time: O(len(d1) + len(d2))
        Space: O(len(d1) + len(d2))
    """
    # Use copy + update for maximum compatibility across Python versions.
    merged = d1.copy()
    merged.update(d2)
    return merged


def merge_inplace(d_target, d_src):
    """
    Merge d_src into d_target in-place (like dict.update). d_target is modified.

    Args:
        d_target: dictionary to be modified
        d_src: dictionary with values to add

    Returns:
        None (d_target modified)

    Complexity:
        Time: O(len(d_src))
        Space: O(1) additional
    """
    d_target.update(d_src)


# --------------------
# Quick demo + tests
# --------------------
if __name__ == "__main__":
    # 1) replace even occurrences
    s = "welcome to python programming"
    print("1) replace_even_occurrences:")
    print(" input: ", s)
    print(" output:", replace_even_occurrences(s))
    print()

    # 2) remove all occurrences of last char
    t = "Bengaluru"
    print("2) remove_all_occurrences_of_last_char:")
    print(" input: ", t)
    print(" output:", remove_all_occurrences_of_last_char(t))
    print()

    # 2b) remove only final occurrence
    print("2b) remove_only_final_occurrence:")
    print(" input: ", t)
    print(" output:", remove_only_final_occurrence(t))
    print()

    # 3) words -> uppercase:length
    words = ["Hi", "Happy", "New", "Year"]
    print("3) words_to_length_dict:")
    print(" input:", words)
    print(" output:", words_to_length_dict(words))
    print()

    # 3b) from sentence
    sentence = "Hi Happy New Year"
    print("3b) sentence_to_words_length_dict:")
    print(" input:", sentence)
    print(" output:", sentence_to_words_length_dict(sentence))
    print()

    # 4) merge dicts
    d1 = {1: 5, 3: 6, 5: 7}
    d2 = {2: 8, 4: 0}
    print("4) merge_new_dict:")
    print(" d1:", d1)
    print(" d2:", d2)
    print(" merged:", merge_new_dict(d1, d2))
    print()

    # inplace merge demo
    print("4b) merge_inplace:")
    x = d1.copy()
    merge_inplace(x, d2)
    print(" after inplace merge x:", x)
    print()

    # quick assertions (basic)
    assert replace_even_occurrences("aabbc") == "a$b$c"
    assert remove_all_occurrences_of_last_char("Bengaluru") == "Bengalr"
    assert remove_only_final_occurrence("Bengaluru") == "Bengalur"
    assert words_to_length_dict(["Hi", "Happy"]) == {"HI": 2, "HAPPY": 5}
    assert merge_new_dict({1: 5, 3: 6, 5: 7}, {2: 8, 4: 0}) == {1: 5, 3: 6, 5: 7, 2: 8, 4: 0}

    print("All quick tests passed.")