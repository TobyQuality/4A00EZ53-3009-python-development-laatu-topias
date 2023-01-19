kuukausi = 0
paiva = 0

print("Anna kuukausi:")
kuukausi = int(input())
if 1 <= kuukausi and kuukausi <= 12:
    print("Anna päivä:")
    paiva = int(input())
    if paiva >= 1 and paiva <= 31:
        if paiva == 1 and kuukausi == 5 or paiva == 6 and kuukausi == 12:
            print("Nyt on vappu tai itsenäisyyspäivä")
        else:
            print("Nyt ei ole vappu tai itsenäisyyspäivä")
    else:
        print("Anna päivä väliltä 1-31!")
else:
    print("Anna kuukausi väliltä 1-12!")
