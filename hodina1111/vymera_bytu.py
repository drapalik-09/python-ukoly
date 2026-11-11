def vypocet_obsahu (a, b):
    if a <= 0 or b <= 0:
        return none
    else:
        obsah = a * b
        return obsah

print("-" * 60)
pocet_mist=int(input("Zadej počet místností: "))
mistnosti = 1
obsah = 0
while mistnosti <= pocet_mist:
    print(f"Zadej rozměry {mistnosti}. místnosti")
    strana_a = float(input ("Zadej rozměr a: "))
    strana_b = float(input ("Zadej rozměr b: "))
    obsah_mistnosti = vypocet_obsahu(strana_a, strana_b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnosti += 1
print(f"Celkový obsah bytu je: {obsah} m2")
print("-" * 60)