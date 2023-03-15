def is_name(name):
    firstname_and_surname = name.split(" ")
    if len(firstname_and_surname) == 2:
        firstname = firstname_and_surname[0]
        surname = firstname_and_surname[1]
        if firstname[0].isupper() and surname[0].isupper():
            if len(firstname) >= 2 and len(surname) >= 2:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

