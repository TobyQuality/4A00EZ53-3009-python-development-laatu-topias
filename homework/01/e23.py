print("Anna korkeus:")
korkeus = int(input())
i = 0
while i < korkeus:
    valiviiva = ""
    j = i
    while j > 0:
        valiviiva = valiviiva + " "
        j = j - 1
    print(valiviiva + "X")
    i = i + 1