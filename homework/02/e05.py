print("Give a grade between 0-5")
not_passed = True

while not_passed:
    grade = int(input())
    if grade >= 0 and grade <= 5:
        not_passed = False
    else:
        print("Give a valid grade!")

if grade == 5:
    print("Excellent")
elif grade == 4 or grade == 3:
    print("Good")
elif grade == 2 or grade == 1:
    print("Weak")
else:
    print("Fail")