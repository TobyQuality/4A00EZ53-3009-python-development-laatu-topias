import datetime
import re

"""
Module that contains validation related functions.
"""
def is_date(date):
    """
    Validates the given string as a date.

    Args:
    ----------
    date (str): The string to be validated as a date. Must be in the format of 'yyyy-mm-dd'.
    Returns:
    ----------
    bool: True if the given string is a valid date. False otherwise.
    Raises:
    ----------
    Exception: If the date is not given as a string object.
    """
    if type(date) is not str:
        raise Exception("the date must be given as string object")
    # year, month and day variables will be used in validation checks later
    year = 0
    month = 0
    day = 0
    #in the first validation check the correct form of date will be checked
    match_object = re.search("^\d{1,4}-\d{1,2}-\d{1,2}$", date)
    if bool(match_object):
        # the date will be converted to int according to day, month and year
        year_month_day = re.split("-", date)
        year = int(year_month_day[0])
        month = int(year_month_day[1])
        day = int(year_month_day[2])
    else:
        return False
    # in the second validation check the days, months and years will be tested
    if month > 0 and month <= 12 and day > 0 and day <= 31 and year >= 0:
        pass
    else:
        return False
    # In the third validation the month's last day will be checked
    # If the day is greater than month's greatest day number, the validation will fail
    months_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if months_days[month-1] >= day:
        pass
    else:
        return False
    # Final validation is checking the leap year
    if day==29 and month==2:
        # centuries are not leap years,
        # unless they are multiples of 400
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            if year % 100 == 0 and year % 400 == 0:
                return True
            else:
                return False
    else:
        return True

def is_email(email):
    """
    Validates the given string as an email address.

    Args:
    ----------
    email (str): The string to be validated as an email address.
    Returns:
    ----------
    bool: True if the given string is a valid email address. False otherwise.
    Raises:
    ----------
    Exception: If the email is not given as a string object.
    """
    if type(email) is not str:
        raise Exception("the email must be given as string object")
    # For validation the following form was taken from:
    # https://knowledge.validity.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
    match_object = re.search("[a-zA-Z0-9!#$%&'*+-/=?^_`{|.]+@[a-zA-Z0-9-.]+[.]{1}[a-z]{2,4}$", email)
    if bool(match_object):
        pass
    else:
        print("Does not comply with the form")
        return False
    # next the recipient name of email address ne (the part before @) will be validated
    index_of_at = email.find("@")
    recipient_name = email[0:index_of_at]
    # local part must not exceed the length of 64 characters
    if len(recipient_name) > 64:
        print("Recipient name is longer than 64 characters")
        return False
    # local part must not start with a special character
    if recipient_name[0].isalnum() == False:
        print("starts with a non-word character: " + recipient_name[0])
        return False
    # local part must not end with a special character
    if recipient_name[len(recipient_name) - 1].isalnum()  == False:
        print("ends with a non-word character: " + recipient_name[len(recipient_name) - 1])
        return False
    # next check is about finding out, if non-word characters are separate or not
    non_word_characters = re.findall("\W", recipient_name)
    # same character must not appear consecutively two or more times
    # For example: "john.doe" is okay. "john..doe" is not okay.
    if len(non_word_characters) > 0:
        i = 0
        while len(non_word_characters) > i:
            # to insert variable inside regex string, one part of the string
            # has to be f-string and the other part has to be concatenated in it
            two_or_more_check = re.search(f"[{non_word_characters[i]}]" + "{2,}", email)
            i = i + 1
            if bool(two_or_more_check):
                print("There is 2 or more special characters grouped together")
                return False
    # next the domain name will be checked (the part after "@")
    domain_name = email[index_of_at + 1:]
    # the domain name can have max length of 253 characters
    if len(domain_name) > 253:
        print("the length of the domain name exceeds the limit of 253")
        return False
    # if there are no problems with validation checks above, True value will be returned
    return True

def is_personal_id(id):
    """
    Checks if the given ID string is a valid Finnish personal identification number.

    Args:
    ----------
    id (str): The ID string to be checked.
    Returns:
    ----------
    bool: True if the ID is valid, False otherwise.
    Raises:
    ----------
    Exception: If the ID is not given as a string object.
    """
    if type(id) is not str:
        raise Exception("the id must be given as string object")
    #First check is about finding out, if the overall syntax is correct
    match_object = re.search("\d{6}[-A]\d{3}[0-9A-FHJ-OPR-Y]", id)
    if bool(match_object) == False:
        return False
    # Next validations involve checking if the date format is alright using is_date function
    # There can be no values such as month being 55 or day being 65 for 
    day = id[0:2]
    month = id[2:4]
    year = ""
    # converting year needs a little extra checking
    # if the seventh character is '-', then the person has been born in 1900's
    # if it is 'A', the person has been born in 2000's
    if id[6] == "-":
        year = "19" + id[4:6]
    if id[6] == "A":
        year = "20" + id[4:6]
    # then utilizing the function is_date we can determine,
    # if the date syntax is correct
    date = year + "-" + month + "-" + day
    if is_date(date) == False:
        return False
    # then we can check if the id argument is right
    # in the sense that if the id's year is greater than the current year,
    # then it is certainly a fake ID
    date_now = datetime.datetime.now()
    current_year = date_now.year
    if int(year) > current_year:
        return False
    # id has individual number consisting of three digits after "-" or "A"
    # valid individual number is between 002-899
    individual_number = id[7:10]
    if int(individual_number) > 1 and int(individual_number) < 900:
        pass
    else:
        return False
    # lastly the id has a character in the end,
    # which is a hash from merging all the numbers together (date and individual number)
    # by dividing them with 31 and determining the check digit based on
    # the remainder of the division.
    # The check digits are based on Finnish Id standard.
    # Check digit table is found on: https://fi.wikipedia.org/wiki/Henkil%C3%B6tunnus
    # The remainder is also the index for the check digit
    checkDigits = ['0','1','2','3','4','5','6','7','8','9','A',
            'B','C','D','E','F','H','J','K','L','M','N','P','R','S','T','U',
            'V','W','X','Y']
    digits_merged = day + month + id[4:6] + individual_number
    remainder = int(digits_merged) % 31
    checkDigit = checkDigits[remainder]
    # last validation check
    if checkDigit != id[10]:
        return False
    else:
        return True