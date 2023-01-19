print("Anna luku:")
luku = int(input())
if luku >= 0:
    while luku >= 0:
        print(luku)
        luku = luku - 1
else:
    while 0 >= luku:
        print(luku)
        luku = luku + 1