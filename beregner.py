findeUdAf = input()

if findeUdAf == 'U' or 'u' or 'Spændingsforskellen' or 'spændingsforskellen':
    print('Du vil finde Spændingsforskellen (U).')
    print('Hvis du kender strømstyrken (I) og effekten (P) skriv 1')
    print('Hvis du kender strømstyrken (I) og  resistansen (R)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er effekten i watt?')
        W = input()
        U= int(W) / int(I)
        
        print('Når strømstyrken er ' + str(I) + ' ampere, og effekten er ' + str(W) + ' watt, er spændingsforskellen ' + str(U) + ' volt')
    
    if option == '2':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er resistansen i ohm?')
        R = input()
        U= int(I) * int(R)
        
        print('Når strømstyrken er ' + str(I) + ' ampere, og resistansen er ' + str(R) + ' ohm, er spændingsforskellen ' + str(U) + ' volt')
    

if findeUdAf == 'R' or 'r' or 'resistansen' or 'Resistansen' or 'Resistivitet' or 'resistivitet':
    print('Du vil finde Resistansen (R).')
    print('Hvis du kender strømstyrken (I) og spædningsforskellen (U) skriv 1')
    print('Hvis du kender strømstyrken (I) og  effekten (P)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er spændingsforskellen i volt?')
        U = input()
        R= int(U) / int(I)
        
        print('Når strømstyrken er ' + str(I) + ' ampere, og spændingsforskellen er ' + str(U) + ' watt, er resistansen ' + str(R) + ' ohm')
    
    if option == '2':
        print('Hvad er strømstyrken i ampere')
        I = input()
        print('Hvad er effekten i watt')
        P = input()
        R= int(P) / (int(I) ** 2)
        
        print('Når strømstyrken er ' + str(I) + ' ampere, og effekten er ' + str(P) + ' watt, er resistansen ' + str(R) + ' volt')
    




