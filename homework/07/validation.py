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

def main():
    print(is_name("Hello World"))
    print(is_name("Apina Apina"))

if __name__ == "__main__":
    main()