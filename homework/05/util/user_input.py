from util.string_helper import *
from util.validation import *
"""
Module that contains user input related functions.
"""
# copied from 02/e08.py
def ask_int(message, min, max):
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

def ask_name(message):
    while True:
        print(message)
        name = input()
        if is_name(name, False):
            return name

def ask_email(message):
    while True:
        print(message)
        email = input()
        if is_email(email):
            return email

def ask_id(message):
    while True:
        print(message)
        id = input()
        if is_personal_id(id):
            return id

def ask_date(message):
    while True:
        print(message)
        date = input()
        if is_date(date):
            return date

def ask_person():
    """
    Asks person for name, email, id and start date at work.
    The function utilizes methods validation methods.
    The user is asked for information until it is given in valid form.
    Args:
    ----------
    No arguments.
    Returns:
    ----------
    A dict containing key-value pairs based on user input.
    """
    input_values = {
        "Name": is_name,
        "Email": is_email,
        "Personal id": is_personal_id,
        "Start date at work": is_date
    }

    for key in input_values:
        valid = False
        users_input = ""
        while valid != True:
            print("Give " + key)
            try:
                users_input = input()
            except Exception as e:
                print(e)
                users_input = ""
            if users_input:
                value = input_values.get(key)
                valid = value(users_input)
            if valid:
                input_values[key] = users_input

    return input_values