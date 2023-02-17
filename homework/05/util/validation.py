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