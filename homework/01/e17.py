import random

salainen_luku = random.randint(1, 10)
kayttajan_syote = -1
arvaus = 0

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (1 - 10)")
    kayttajan_syote = int( input() )
    arvaus = arvaus + 1

print("oikein!")
print("Arvasit " + str(arvaus) + ":lla kerralla")