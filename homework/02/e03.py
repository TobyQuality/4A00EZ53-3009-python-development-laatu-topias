a = "hel'lo" #shows ' in the middle of l characters
b = 'hel"lo' #shows " in the middle of l characters
c= """hello
        world"""
d= '''hello
        world'''

print (a, b , c ,d )

matti = "Matti"
print("hello " + matti)
body_mass_index = 25.112312
print(f"Hello {matti}, you have bmi = {body_mass_index:.2f}")
print(f"Hello {matti}, you have bmi = {body_mass_index:.1f}")

name_length = len(matti)
print(matti[0], matti[name_length-1])

#count() is used to count how many times a specified value is found within a string object
test_1 = "hello hello hello"
print(test_1.count("hello"))

#find() is used to find the index where a specified value first occurs
test_2 = "what should we do with a drunken sailor"
print(test_2.find("drunken"))

#upper() converts string to upper case
test_3 = "wazzup everybody!?"
print(test_3.upper())

#replace() is used to replace a certain word within a string with another value
test_4 = "You shall not pass!"
print(test_4.replace("not", ""))

#isdigit() returns True, if all characters in the string are digits
test_5 = "010101001010"
print(test_5.isdigit())

#split() creates a list from a string object using a specified separator
test_6 = "to be or not to be"
print(test_6.split())

#endswith() Returns true if the string ends with the specified value
test_7 = "this it the end"
print(test_7.endswith("d"))

print("give a:", end=" ")
a = input()
print("give b:", end=" ")
b = input()
print(f"value {a} in memory address {id(a)}")
print(f"value {b} in memory address {id(b)}")
print(a == b)

print("give a:", end=" ")
a = input()
print("give b:", end=" ")
b = input()
print(f"value {a} in memory address {id(a)}")
print(f"value {b} in memory address {id(b)}")
print(a is b)

