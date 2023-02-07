def is_name(name, ignore_case=False):
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