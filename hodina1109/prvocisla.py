import math
print("Testování prvočísel")
cislo = int(input("Zadej číslo: "))

if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True 
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel = 3
    while delitel <= math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel =+ 1

    if je_prvocislo:
        print("Dělitelé čísla jsou:")
        for delitel in range(2, cislo):
            if cislo % delitel == 0:
                print(delitel)
    else:
        print("Číslo je prvočíslo.")