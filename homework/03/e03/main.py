from string_helper import is_name

print("Your name:")
name = input()

if is_name(name):
    print(f"Hello {name}!")
else:
    print("You did not give a proper name.")
