def is_name(name, ignore_case=False):
    
    if type(name) is not str:
        raise Exception("Please give name as string object")

    firstname_and_surname = name.split(" ")

    if len(firstname_and_surname) == 2:
        firstname = firstname_and_surname[0]
        surname = firstname_and_surname[1]
        
        if firstname.isalpha() == False or surname.isalpha() == False:
            return False

        if ignore_case == False:
            if firstname.istitle() and surname.istitle():
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