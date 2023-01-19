kuukausi = 0
paiva = 0

print("Anna kuukausi:")
kuukausi = int(input())
if 1 <= kuukausi and kuukausi <= 12:
    print("Anna päivä:")
    paiva = int(input())
    if paiva >= 1 and paiva <= 31:
        if paiva == 24 and kuukausi == 12:
            print("Hyvää joulua")
        else:
            print("Ei ole vielä joulu")
    else:
        print("Anna päivä väliltä 1-31!")
else:
    print("Anna kuukausi väliltä 1-12!")
