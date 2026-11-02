horni_hodnota=10000
dolnihodnota=1
import random 
tajne=random.randint(dolni_hodnota, horni_hodnota)
max_pokusy=5
print(f"Hádání čísla od {dolnihodnota} do {horni_hodnota}. Máš {max_pokusy} pokusů.")
cislo = int(input(f"Zadej číslo od {dolnihodnota} do {horni_hodnota}: "))
pokusy=1
while cislo != tajne and pokusy < max_pokusy:
    if cislo < tajne:
        print(f"Hledané číslo je větší než {cislo}.")
        print(f"Zbývá ti {max_pokusy-pokusy} pokusů.")
        dolni_hodnota=cislo
    else:
        print(f"Hledané číslo je menší než {cislo}.")
        print(f"Zbývá ti {max_pokusy-pokusy} pokusů.")
        horni_hodnota=cislo
    cislo = int(input(f"Zadej číslo od {dolni_hodnota} do {horni_hodnota}: "))
    pokusy += 1
if pokusy <max_pokusy:
    print(f"Uhodl jsi číslo na {pokusy}. pokus. ")
    print(f"Hledané číslo bylo:{tajne}")
else:
    print(f"Počet pokusů byl vyčerpán. Číslo bylo: {tajne}")
