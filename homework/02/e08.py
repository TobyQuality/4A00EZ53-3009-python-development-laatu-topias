def get_int(message, min, max):
    # First we have to make sure that the min and max variables have the right values
    if (min > max):
        old_max = max
        max = min
        min = old_max

    # Then the user will be asked for a digit until a valid one has been given
    # The loop will end, once the right value is returned
    while True:
        # first we need to make sure that the input is a number/digit
        input_is_number = False
        print(message)
        user_input = input()
        #isdigit method doesn't include the minus sign, so it can give a misleading result
        #that is why there needs to be another special conditional check for the minus sign
        if user_input[0] == '-':
            remove_minus_from_input = user_input[1:]
            if remove_minus_from_input.isdigit():
                user_input = int(user_input)
                input_is_number = True
        else:
            if user_input.isdigit():
                user_input = int(user_input)
                input_is_number = True

        if input_is_number:
            # In this conditional check we need to make sure the numerical input is between min and max
            if user_input >= min and user_input <= max:
                return user_input
            else:
                print("Give a correct value")
                input_is_number = False
        else:
            print("Give a number!")

# Here's how the function can be implemented
min = 0
max = 120
message = "give age"
value = get_int(message, min, max)
print(value)