from string_helper import list_to_str
from user_input import *

# global variables
db = ["Hannah Smith", "Jack Smith", "Tiina Smith"]
choices = ["Add", "Insert", "Remove", "Clear"]
user_choice = 0

# methods:
def add():
    try:
        name = ask_name("Give name:")
    except Exception as e:
        print("Adding to database failed:")
        print(e)
        return
    db.append(name)

def insert():
    index = ask_int("Where to insert?", 1, len(db) + 1)
    try:
        name = ask_name("Give name:")
    except Exception as e:
        print("Inserting into database failed:")
        print(e)
        return
    if index == len(db) + 1:
        db.append(name)
    else:
        db.insert(index -1, name)
    
def remove():
    if len(db) > 0:
        index = ask_int("What to remove?", 1, len(db))
        db.pop(index - 1)
    else:
        print("\nYou cannot remove from an empty list\n")

def clear():
    db.clear()

def operations(choice):
    if choice == 1:
        add()
    if choice == 2:
        insert()
    if choice == 3:
        remove()
    if choice == 4:
        clear()
    if choice == -1:
        return

# the user interaction happens inside this while loop
while user_choice != -1:
    print(list_to_str(db))
    user_choice = ask(choices)
    operations(user_choice)