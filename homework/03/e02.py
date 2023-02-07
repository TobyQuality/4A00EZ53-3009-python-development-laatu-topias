def output(start, end, step=1):
    for index in range(start, end, step):
        print(f"{index},", end="")
    print(end)

output(1, 10)
output(0, 10, 2)
output(10,0,-1)
