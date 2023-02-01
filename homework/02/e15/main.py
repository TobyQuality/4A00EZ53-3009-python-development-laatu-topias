def get_first_index(word, char):
    if type(word) is str and type(char) is str:
        if len(char) == 1:
            i = 0
            while i < len(word):
                if word[i] == char:
                    return i
                i = i + 1
            return -1
        else:
            raise Exception("The second argument must contain a single character.")
    else:
        raise Exception("Check the data types of the arguments.")

#index = get_first_index("kalle", "l")
#print(index) # 2
#index = get_first_index("kalle", "z")
#print(index)