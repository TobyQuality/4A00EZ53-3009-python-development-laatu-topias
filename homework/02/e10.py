def reverse(word, lowercase = False):
    if type(lowercase) is bool and type(word) is str:
        if lowercase == True:
            word = word.lower()

        backwards = ""
        i = len(word)

        while 0 < i:
            backwards = backwards + word[i-1]
            i = i - 1

        return backwards

    else:
        raise Exception( "Give a string and a boolean, in this order!")

print(reverse("Kalle"))
print(reverse("Kalle", True))
#print(reverse(1, "Moi"))