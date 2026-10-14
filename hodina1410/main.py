osoby = int(input("Zadejte počet osob:"))
cena = 500

if osoby>=4:
    print("Množstevní sleva")
    print("Cena je",cena*osoby*0.75)
    print("Cena za jednoho:", cena*0.75)

else:
    vek = int(input("Zadejte věk: "))
    if vek >= 65:
        #senior
        print ("Seniorská sleva")
        print("Cena je:", cena*osoby*0.8)
        print("Cena za jednoho", cena*0.8)
    elif vek >= 26:
        print("Normální cena")
        print("Cena je:", cena*osoby)
        print("Cena za jednoho", cena)
    elif vek>0 and vek<26:
        student = input("Jste student? [ano/ne]:")
        if student=="ano":
            print("Studentská sleva")
            print("Cena je:", cena*osoby*0.7)
            print("Cena za jednoho", cena*0.7)
        else student=="ne":
            print("Beze slevy")
            print("Cena je ", cena*osoby)
            print("Cena za jednoho", cena)