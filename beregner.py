import math

print('Hvad vil du finde inden for strøm eller bævegelse')
findeUdAf = input()

uMuligheder=['U','u','Spændingsforskellen','spændingsforskellen']
rMuligheder=['R','r','resistansen','Resistansen','Resistivitet','resistivitet']
iMuligheder=['I','i','Strømstyrke','strømstyrke','Strømstyrken','strømstyrken']
pMuligheder=['P','p','effekt','Effekt']
vMuligheder=['V','v','hastighed','Hastighed']
sMuligheder=['s','S','Strækning','strækning']
tMuligheder=['t','T','tid','Tid']
aMuligheder=['a','A','Acceleration','acceleration']


if findeUdAf in uMuligheder:
    print('Du vil finde Spændingsforskellen (U).')
    print('Hvis du kender strømstyrken (I) og effekten (P) skriv 1')
    print('Hvis du kender strømstyrken (I) og  resistansen (R)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er effekten i watt?')
        P = input()
        U= int(P) / int(I)
        
        print(f'Når strømstyrken er {I} ampere, og effekten er {P} watt, er spændingsforskellen {U} volt')
    
    if option == '2':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er resistansen i ohm?')
        R = input()
        U= int(I) * int(R)
        
        print(f'Når strømstyrken er {I} ampere, og resistansen er {R} ohm, er spændingsforskellen {U} volt')
    

if findeUdAf in rMuligheder:
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
        
        print(f'Når strømstyrken er {I} ampere, og spændingsforskellen er {U} volt, er resistansen {R} ohm')
    
    if option == '2':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er effekten i watt?')
        P = input()
        R= int(P) / (int(I) ** 2)
        
        print(f'Når strømstyrken er {I} ampere, og effekten er {P} watt, er resistansen {R} volt')
    

if findeUdAf in iMuligheder:
    print('Du vil finde Strømstyrken (I).')
    print('Hvis du kender resistansen (R) og spædningsforskellen (U) skriv 1')
    print('Hvis du kender spædningsforskellen (U) og  effekten (P)  skriv 2')
    print('Hvis du kender resistansen (R) og  effekten (P)  skriv 3')
    option = input()
    if option == '1':
        print('Hvad er resistansen i ohm?')
        R = input()
        print('Hvad er spændingsforskellen i volt?')
        U = input()
        I= int(U) / int(R)
        
        print(f'Når resistansen er {I} ohm, og spændingsforskellen er {U} volt, er strømstyrken {I} ampere')
    
    if option == '2':
        print('Hvad er spædningsforskellen i volt')
        U = input()
        print('Hvad er effekten i watt')
        P = input()
        I= int(P) / int(U)
        
        print(f'Når spædningsforskellen er {U} volt, og effekten er {P} watt, er strømstyrken {I} ampere')
    
    if option == '3':
        print('Hvad er resistansen i ohm?')
        R = input()
        print('Hvad er effekten i watt?')
        P = input()
        I= math.sqrt((int(P) / int(R)))
        
        print(f'Når resistansen er {R} ohm, og effekten er {P} watt, er strømstyrken {I} ampere')
   

if findeUdAf in pMuligheder:
    print('Du vil finde Effekten (P).')
    print('Hvis du kender strømstyrken (I) og spædningsforskellen (U) skriv 1')
    print('Hvis du kender strømstyrken (I) og  resistansen (R)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strømstyrken i ampere?')
        I = input()
        print('Hvad er spændingsforskellen i volt?')
        U = input()
        P= int(U) * int(I)
        
        print(f'Når strømstyrken er {I} ampere, og spændingsforskellen er {U} volt, er effekten {P} watt')
    
    if option == '2':
        print('Hvad er resistansen i ohm')
        R = input()
        print('Hvad er strømstyrken i ampere')
        I = input()
        P= int(R) * int(I)**2
        
        print(f'Når resistansen er {R} ohm, og strømstyrken er {I} ampere, er strømstyrken {P} watt')


if findeUdAf in vMuligheder:
    print('Du vil finde hastigheden (v).')
    print('Hvis du kender strækningen (s) og tiden (t) skriv 1')
    print('Hvis du kender accelerationen (a) og  tiden (t)  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strækningen i meter?')
        s = input()
        print('Hvad er tiden i sekunder?')
        t = input()
        v= int(s) / int(t)
        
        print(f'Når strækningen er {s} meter, og tiden er {t} sekunder, er hastigheden {v} m/s')
    
    if option == '2':
        print('Hvad er accelerationen i m/s^2?')
        a = input()
        print('Hvad er tiden i sekunder?')
        t = input()
        v= int(a) * int(t)
        
        print(f'Når accelerationen er {a} m/s^2, og tiden er {t} sekunder, er hastigheden {v} m/s')


if findeUdAf in sMuligheder:
    print('Du vil finde stækningen (s).')
    print('Hvad er hastigheden i m/s?')
    v = input()
    print('Hvad er tiden i sekunder?')
    t = input()
    s = int(v) * int(t)

    print(f'Når hastigheden er {v} m/s, og tiden er {t} sekunder, er strækningen {s} meter')

if findeUdAf in tMuligheder:
    print('Du vil finde tiden (t).')
    print('Hvis du kender strækningen (s) og hastigheden (v) skriv 1')
    print('Hvis du kender hastigheden (v) og accelerationen (a))  skriv 2')
    option = input()
    if option == '1':
        print('Hvad er strækningen i meter?')
        s = input()
        print('Hvad er hastigheden i m/s?')
        v = input()
        t= int(s) / int(v)
        
        print(f'Når strækningen er {s} meter, og hastiheden er {v} m/s, er tiden {t} s')
    
    if option == '2':
        print('Hvad er hastigheden i m/s?')
        v = input()
        print('Hvad er accelerationen i m/s^2?')
        a = input()
        t= int(v) / int(a)
        
        print(f'Når accelerationen er {a} m/s^2, og tiden er {t} sekunder, er hastigheden {v} m/s')


if findeUdAf in aMuligheder:
    print('Du vil finde acceleration (a).')
    print('Hvad er hastigheden i m/s?')
    v = input()
    print('Hvad er tiden i sekunder?')
    t = input()
    a = int(v) / int(t)

    print(f'Når hastigheden er {v} m/s, og tiden er {t} sekunder, er accelerationen {a} m/s^2')


else:
    print('Du har givet et forkert input')
    