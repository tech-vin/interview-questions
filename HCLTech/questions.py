def change_to_uppercase_v1(sentence: str) -> str:
    """
    Question:
    Given a sentence, return a new sentence where 
    the first and last characters of each word are converted 
    to uppercase. If the word has only one character, it should 
    be fully uppercase.

    Example:
    >>> change_to_uppercase("This is a programming hub")
    'ThiS IS A ProgramminG HuB'
    """
    def transform(w: str) -> str:
        if len(w) == 1:
            return w.upper()
        return w[0].upper() + w[1:-1] + w[-1].upper()

    return " ".join(transform(w) for w in sentence.split())

testcases = ['a', 'vineet', 'A', 'This is a programming hub']
print([change_to_uppercase_v1(x) for x in testcases])
