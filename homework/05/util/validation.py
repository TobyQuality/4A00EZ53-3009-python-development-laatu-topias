import re


def is_date(date):
    if type(date) is not str:
        raise Exception("the date must be given as string object")
    # year, month and day variables will be used in validation checks later
    year = 0
    month = 0
    day = 0
    #in the first validation check the correct form of date will be checked
    match_object = re.search("\d{1,4}-\d{1,2}-\d{1,2}", date)
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
    # In the fourth validation 
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
    if type(email) is not str:
        raise Exception("the email must be given as string object")
    # For validation the following form was taken from:
    # https://knowledge.validity.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
    match_object = re.search("[a-zA-Z0-9!#$%&'*+-/=?^_`{|.]+@[a-zA-Z0-9-.]+[.][a-z]{2,4}", email)
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