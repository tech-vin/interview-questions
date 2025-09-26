def count_word_frequency(word):
    '''
    Count vowels in the given word

    Args:
        word [str]: string
    
    Example:
        if the word = "Vineet" then output will be
        3
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    count  = 0

    for ch in word:
        if ch in vowels:
            count+=1
    return count

testcases = ['', 'Vineet', 'Hello, world']
print([count_word_frequency(x) for x in testcases])


def fibonacci_series(num):
    """
    Generates a Fibonacci series of length 'num' using an iterative approach.
    """
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    
    series = [0, 1]
    # The loop runs 'num - 2' times to append the remaining numbers.
    for _ in range(num - 2):
        next_num = series[-1] + series[-2]
        series.append(next_num)
    
    return series

testcases = [0, 1, 6]
print([fibonacci_series(x) for x in testcases])
