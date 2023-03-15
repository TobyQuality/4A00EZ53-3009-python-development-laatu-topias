from string_helper import is_name

# asking for a name while ignoring case
print("Your name:")
name = input()

if is_name(name, True):
    print(f"Hello {name}!")
else:
    print("You did not give a proper name.")

# asking for a name while not ignoring case
print("Your name:")
name = input()

if is_name(name, False):
    print(f"Hello {name}!")
else:
    print("You did not give a proper name.")

#default settings of the app
print("Your name:")
name = input()

if is_name(name):
    print(f"Hello {name}!")
else:
    print("You did not give a proper name.")
