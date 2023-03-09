findeUdAf = input()

if findeUdAf == 'U' or 'u' or 'Spændingsforskellen' or 'spændingsforskellen':
    print('Du vil finde Spændingsforskellen (U).')
    print('Hvis du kender strømstyrken (I) og effekten (P) skriv 1')
    print('Hvis du kender strømstyrken (I) og  resistansen (R)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strømstyrken i ampere')
        I = input()
        print('Hvad er effekten i watt')
        W = input()
        print('Når strømstyrken er ' + str(I) + ' ampere og effekten er ' + str(W) + ' watt er spændingsforskellen ' + str(W/I) + ' volt' )






