def reverse(word):
    if type(word) is str:
        backwards = ""
        i = len(word)

        while 0 < i:
            backwards = backwards + word[i-1]
            i = i - 1

        return backwards

    else:
        raise Exception("Give a string!")


print(reverse("Kalle"))
#print(reverse(1))