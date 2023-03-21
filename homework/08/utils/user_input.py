def ask_int(message, min, max):
    if type(min) != int or type(max) != int:
        raise Exception("give min and max values as integers")
    if type(message) != str:
        raise Exception("give message as string")
    if (min > max):
        old_max = max
        max = min
        min = old_max
    while True:
        input_is_number = False
        user_input = input(message)
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
            if user_input >= min and user_input <= max:
                return user_input
            else:
                print("Give a correct value")
                input_is_number = False
        else:
            print("Give a number!")

def ask(choices):
    if type(choices) != list:
        raise Exception("Give a list as argument")

    menu = ""
    for i in range(0, len(choices)):
        menu = menu + f"{i + 1}) {choices[i]}\n"
    menu = menu + "0: Exit\n"
    print(menu)

    choice = ask_int("Your choice: ", 0, len(choices))
    if choice == 0:
        return -1
    else:
        return choice