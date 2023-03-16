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
    print("Tryk i væske: P")
    print("Densitet af væske: rho")
    print("Højden af væske søjlen: h")
    print("Alment tryk: P")
    print("Volumen: V")
    print("Stofmængde: N")
    print("Temperatur: T")
    print("Opdrift: F")
    værdi_termo = input()
    if værdi_termo == 'P':
        print("Indtast nu dine kendte værdier") 
        print("Densitet(rho)")
        Densitet=input()
        print("højden (h)")
        Højde=input()
        tryk_væske=int(Højde)*int(Densitet)*9.82
        print(tryk_væske)


else:
    exit()