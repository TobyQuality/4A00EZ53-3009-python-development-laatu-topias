import sys
# the method will return a set of lotto numbers
# based on the arguments given in the command console
def lotto_user_input():
    # taking arguments into variable called 'arguments'
    arguments = sys.argv
    # the length of the arguments array should be 8
    # first index[0] contains the file name
    if len(arguments) != 8:
        raise Exception("Enter seven arguments after file name.")

    # turning the arguments into integers
    # exception will be raised if not possible in the catch section
    lotto_numbers = set()
    try:
        for i in range(1,8):
            lotto_number = int(arguments[i])
            # validation check that number is not less than one
            if lotto_number < 1:
                raise Exception("You musn't give numbers that are less than one")
            # validation check that that number is not more than 40
            if lotto_number > 40:
                raise Exception("You musn't give numbers that are bigger more than fourty")
            # validated numbers will be put in the lotto_numbers set
            lotto_numbers.add(lotto_number)
    except:
        raise Exception("You must give numbers.")

    # if the set's length is not 7, it means not all
    # numbers were unique, so an exception will be raised
    if len(lotto_numbers) != 7:
        raise Exception("All given numbers must be unique")

    # if no exceptions are raised, lotto numbers given by
    # user will be returned in a set
    return lotto_numbers

# print(lotto_user_input())