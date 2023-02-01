def calculate_sum(a, b):
    return a + b

def get_max(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

def reverse(word):
    backwards = ""
    i = len(word)
    while 0 < i:
        backwards = backwards + word[i-1]
        i = i - 1
    return backwards

def is_palindrome(word, lowercase):
    if type(word) is str and type(lowercase) is bool:
        if lowercase == True:
            word = word.lower()

        backwards = reverse(word)

        if backwards == word:
            return True
        else:
            return False
    else:
        raise Exception("Give a string and/or a bool as arguments!")