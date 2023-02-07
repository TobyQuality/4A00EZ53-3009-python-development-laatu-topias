
"""
Module that contains String related functions.
"""
def is_name(name, ignore_case=False):
    """Checks if given input contains first name and surname.
    Parameters
    ----------
    value : `name`
        The value that is used for checking if it's a valid name.
    value : `ignore_case`
        The value is used for determining whether to ignore cases from the name
    Returns
    -------
    absolute value : `boolean`
        True or False.
    """
    firstname_and_surname = name.split(" ")
    if len(firstname_and_surname) == 2:
        firstname = firstname_and_surname[0]
        surname = firstname_and_surname[1]
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

def get_title(title, amount, char):
    """The method is used for creating a title and a frame for it with a specified character.
    Parameters
    ----------
    value : `title`
        This is a string that contains the title.
    value : `amount`
        This specifies the length of the frame for the title.
    value : `char`
        This specifies which character is used for the frame around the title.
    Returns
    -------
    absolute value : `String`
        If the frame length is greater than title length,
        a title surrounded by a frame of specified characters is returned,
        otherwise a text explaining that creating the frame failed.
    """
    result = ""
    top_layer = ""
    middle_layer = ""
    bottom_layer = ""
    if len(title) <= amount:
        #The top layer is formed
        for x in range(amount):
            top_layer = top_layer + char

        #The middle layer is formed
        i = 0
        frame_middle_point = (int) ((amount / 2) - 1)
        title_middle_point = (int) ((len(title) / 2) - 1)
        title_starting_point = frame_middle_point - title_middle_point
        if len(title) <= amount - 3:  
            while i < amount:
                if i == 0:
                    middle_layer = middle_layer + char
                    i = i + 1
                elif i == amount - 1:
                    middle_layer = middle_layer + char
                    i = i + 1
                elif i == title_starting_point:
                    j = 0
                    for x in range(len(title)):
                        middle_layer = middle_layer + title[j]
                        j = j + 1
                        i = i + 1
                else:
                    middle_layer = middle_layer + " "
                    i = i + 1
        else:
            while i < amount:
                middle_layer = middle_layer + title[i]
                i = i + 1
        # bottom layer is formed
        for x in range(amount):
            bottom_layer = bottom_layer + char
        
        #creating the final result by piling layers on top of each other
        #and then returning the result
        result = f"""{top_layer}
{middle_layer}
{bottom_layer}"""
        return result

    else:
        result = "invalid values, title length is > graph length"
    return result