horni_hranice=100
dolni_hranice=1
tajne = ""
pokusy = 0
print("Mysli si číslo od 1 do 100 já ho hádám. Odpovídej 'v' pro větší, 'm' pro menší a 's' pro správné číslo.")
while tajne != "s":
    tajne = (dolni_hranice + horni_hranice) // 2
    odpoved = input(f"Je tvoje číslo {tajne}?: ")
    pokusy += 1
    if odpoved ==  "v":
        dolni_hranice = tajne 
    elif odpoved == "m":
        horni_hranice = tajne
    else:
        print("Uhodl jsem tvoje číslo.")
        print(f"Tvoje číslo je {tajne}. a já jsem ho uhodl na {pokusy} pokus.")
