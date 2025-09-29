def reverseString(string):
    '''
    Reverse the given string

    Args:
        string[str]: set of characters
    
    Example:
        If the given string is 'Linux'
        then output will be 'xuniL'
    '''
    # return string[::-1] # pythonic way

    result = ''
    for ch in string:
        result = ch + result

    return result

def reverseSentence(string):
    '''
    Reverse a sentence without reverse each word

    Args:
        string [str]: set of characters
    
    Example:
        If the sentence is 'Betty bought a bit of butter'
        then output will be: 'butter of bit a bought Betty'
    '''
    word = string.split()
    # return word[::-1] # pythonic way

    result = []
    for w in word:
        result.append(w)
    return result

testcase = ['vineet', 'Betty bought a bit of butter']
print("Reverse String: ", [reverseString(x) for x in testcase])
print("Reverse Sentence: ", [reverseSentence(x) for x in testcase])

def remove_duplicates(iterative):
    '''
    Remove duplicate values from the given array.

    Args:
        iterative [list] = list of numbers
    
    Example:
        If the given array is [1, 2, 3, 3, 2, 1],
        then the output will be []

        if the given array is [1, 2, 3, 1]
        then the output will be [2, 3]
    '''
    freq = {}
    for item in iterative:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return [k for k, v in freq.items() if v == 1]

arr = [[1, 2, 3, 3, 2, 1], [1, 2, 3], [1, 2, 3, 1]]
print("Remove Duplicates: ",[remove_duplicates(x) for x in arr])