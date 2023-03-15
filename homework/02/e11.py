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

def reverse(word):
    backwards = ""
    i = len(word)
    while 0 < i:
        backwards = backwards + word[i-1]
        i = i - 1
    return backwards

# outputs True
print(is_palindrome("Saippuakauppias", lowercase=True)) 
# outputs False
print(is_palindrome("Saippuakauppias", lowercase=False)) 
# outputs False
print(is_palindrome("Kalle", lowercase=False)) 
# outputs an exception
# print(is_palindrome(1, lowercase=True))
# outputs an exception
# print(is_palindrome("moi", 1))