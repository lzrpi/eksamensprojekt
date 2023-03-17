#Dette er menu delen til at finde rundt i vores beregnings program 
print("Hej og velkommen til fysikopgave løseren")
print("Programmet er udviklet af Mads og Philip fra X21 som en del af eksamensprojekt i programmering C")
print("Programmet kan løse opgaver indenfor de 3 nedenstående emner:")
print("")
print("1. Elektriske Kredsløb")
print("2. Termodynamik")
print("3. Bevægelse")
print("")
print("Tast 1, 2 eller 3")

emne_valg=input()
if emne_valg == '1': 
    print("Hvilken værdi vil du gerne finde?")
    print("")
    print("Resistans: R")
    print("Strømstyrke: I")
    print("Spændingsforskel: U")
    print("Effekt: P")
    værdi=input() 

    
if emne_valg == '2':
    print("Hvilken værdi vil du gerne finde?")
    print("")
    print("1. Tryk i væske (P)")
    print("2. Densitet af væske (rho)")
    print("3. Højden af væske søjlen (h)")
    print("4. Alment tryk (P)")
    print("5. Volumen (V)")
    print("6. Stofmængde (N)")
    print("7. Temperatur (T)")
    print("8. Opdrift (F)")
    værdi_termo = input()
    if værdi_termo == '1':
        print("Tryk i væske (p) er fundet ved at gøre brug af følgende formel p=rho*g*h")
        print("Indtast nu dine kendte værdier") 
        print("Densitet(rho)")
        Densitet=input()
        print("højden (h)")
        Højde=input()
        tryk_væske=float(Højde)*float(Densitet)*9.82
        print("Beregningen ser ud som følgende p = " + str(Højde) + " m * " + str(Densitet) + " kg/m^3 * " + "9.82 N/kg")
        print("Tryk i væske (p) bliver dermed: " + str(tryk_væske) + " Pa")
    if værdi_termo == '2':
        print("For at finde rho er rho isoleret i følgende formel p=rho*g*h")
        print("Den isolerede formel ser ud som følgende: rho=P/g*h")
        print("Indtast nu dine kendte værdier")
        print("Tryk i væsken (P)")
        tryk_væske=input() 
        print("højden (h)")
        højde=input()
        densitet=float(tryk_væske) / 9.82 * float(højde)
        print("Beregningen ser ud som følgende rho= " + str(tryk_væske)+ " Pa / 9.82 N/kg * " + str(højde) + " m")

else:
    exit()