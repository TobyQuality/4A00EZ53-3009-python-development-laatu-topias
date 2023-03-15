import re
from validation import *

def read_database():
    data = open("database.txt", "r")
    return data.read()

def save_to_database(fname, lname):
    name = f"{fname} {lname}"
    if is_name(name) == False:
        print("Error")
        return

    data = read_database()
    digits = re.findall(r'\d+', data)
    next_digit = len(digits) + 1
    next_digit_str = str(next_digit)

    f = open("database.txt", "a")
    f.write(f"\n{next_digit_str},{fname},{lname}")
    f.close()

def main():
    print(read_database())
    save_to_database("Apina","Apina")
    save_to_database("A", "A")
    print(read_database())

if __name__ == "__main__":
    main()