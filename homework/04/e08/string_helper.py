"""
Module that contains String related functions.
"""
def is_name(name, ignore_case=False):
    """
    Checks if given input contains first name and surname.

    Parameters
    ----------
    name : str
        The value that is used for checking if it's a valid name.
    ignore_case : bool, optional
        The value is used for determining whether to ignore cases from the name

    Returns
    -------
    bool
        True if the input contains a valid name, False otherwise.

    Raises
    ------
    Exception
        If the input is not a string.

    """
    if type(name) is not str:
        raise Exception("Please give input in string format")
    firstname_and_surname = name.split(" ")

    if len(firstname_and_surname) == 2:
        firstname = firstname_and_surname[0]
        surname = firstname_and_surname[1]
        
        if firstname.isalpha() == False or surname.isalpha() == False:
            return False

        if ignore_case == False:
            if firstname[0].isupper() and surname[0].isupper():
                if len(firstname) >= 2 and len(surname) >= 2:
                    return True
                else:
                    return False
            #else for isupper() check
            else:
                return False
        #else for ignore_case check
        else:
            if len(firstname) >= 2 and len(surname) >= 2:
                return True
            else:
                return False
    #else for checking if there is a first name and a surname
    else:
        return False

def list_to_str(my_list):
    """
    Converts a list of strings into a string formatted as a database.

    Parameters
    ----------
    my_list : list
        The list of strings to be formatted as a database.

    Returns
    -------
    str
        The formatted database string.

    Raises
    ------
    Exception
        If the input is not a list.

        If the list contains any element that is not a string.

        If the list contains any empty string.

    """
    if type(my_list) is not list:
        raise Exception("Give a list")
    for i in range(0, len(my_list)):
        if type(my_list[i]) is not str:
            raise Exception("The list must contain only string data")
        if len(my_list[i]) == 0:
            raise Exception("The data inside list must not contain empty values")

    database = "Database:\n"
    if len(my_list) >= 1:
        i = 0
        while i < len(my_list):
            database = database + f"{i+1}: {my_list[i]}\n"
            i = i + 1
        return database
    else:
        return "Empty List\n"

#test_list=["Oukki Doukki", "James Bond"]
#print(list_to_str(test_list))