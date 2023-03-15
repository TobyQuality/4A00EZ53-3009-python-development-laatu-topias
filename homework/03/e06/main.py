from string_helper import is_name, get_title

title = get_title("Battleship", 30, "-")
print(title)

print("Give name:")
name = input()
if is_name(name, True):
    print(f"Hello {name}! and welcome to Battleship - game!")
else:
    print("You did not give a proper name.")