luku = 0
pienin = -1
while luku >= 0:
    print("Anna positiivinen numero (lopetus negatiivisella luvulla)")
    luku = int( input() )
    if pienin == -1 and luku >= 0:
        pienin = luku
    elif luku >= 0:
      if pienin > luku:
        pienin = luku

if pienin >= 0:
    print("Pienin antamasi luku oli ")
    print(pienin)
else:
    print("Et antanut lukuja.")