from string_helper import is_name
"""
Module that contains user input related functions.
"""
def ask_name(message):
    """
    Asks the user to input a name in the format "Firstname Lastname". Returns the name that the user inputs.
    
    Args:
    - message: str - a message to prompt the user for input
    
    Returns:
    - str - the name input by the user
    
    Raises:
    - Exception: if the message is not a string, exception will be raised.
    """
    if type(name) != str:
        raise Exception("Give the message in string form")
    # the only way to get out of the eternal loop is to give name
    # in correct format
    while True:
        print(message)
        user_input = input()
        if is_name(user_input, False):
            return user_input
        else:
            print("please give name in following format: Firstname Lastname\nAlso make sure the names are at least 2 characters long")

# copied from 02/e08.py
def ask_int(message, min, max):
    """
    Asks the user to input an integer between min and max, inclusive. Returns the integer that the user inputs.
    
    Args:
    - message: str - a message to prompt the user for input
    - min: int - the minimum integer value the user can input
    - max: int - the maximum integer value the user can input
    
    Returns:
    - int - the integer input by the user
    
    Raises:
    - Exception: if the user inputs a non-integer in min or max
    - Exception: if the user gives message in non-string form
    """
    if type(min) != int or type(max) != int:
        raise Exception("give min and max values as integers")
    if type(message) != str:
        raise Exception("give message as string")

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

def ask(choices):
    """
    Displays a menu of options to the user and asks them to input a choice. Returns the index of the user's
    choice in the input list. If the user inputs 0, returns -1.
    
    Args:
    - choices: List[str] - a list of strings representing the options the user can choose from
    
    Returns:
    - int - the index of the user's choice in the input list, or -1 if the user inputs 0
    
    Raises:
    - Exception: if choices is not a list
    """
    if type(choices) != list:
        raise Exception("Give a list as argument")

    menu = "Menu:\n"
    for i in range(0, len(choices)):
        menu = menu + f"{i + 1} {choices[i]}\n"
    menu = menu + "0: Exit\n"
    print(menu)

    choice = ask_int("Your choice:", 0, len(choices))
    if choice == 0:
        return -1
    else:
        return choice