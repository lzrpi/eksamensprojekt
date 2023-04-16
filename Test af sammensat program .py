#Importer de ting vi skal burge 
import math

#Liste med værdier til strøm og bevæglese 
uMuligheder=['U','u','Spændingsforskellen','spændingsforskellen']
rMuligheder=['R','r','resistansen','Resistansen','Resistivitet','resistivitet']
iMuligheder=['I','i','Strømstyrke','strømstyrke','Strømstyrken','strømstyrken']
pMuligheder=['P','p','effekt','Effekt']
vMuligheder=['V','v','hastighed','Hastighed']
sMuligheder=['s','S','Strækning','strækning']
tMuligheder=['t','T','tid','Tid']
aMuligheder=['a','A','Acceleration','acceleration']
  
#Velkomst funktion 
def welcome():
    print("\n\nHej og velkommen til fysikopgave løseren")
    print("Programmet er udviklet af Mads og Philip fra X21 som en del af eksamensprojekt i programmering C")
    print("Programmet kan løse opgaver indenfor de 3 nedenstående emner:\n \n")
    print("\t1. Elektriske Kredsløb")
    print("\t2. Termodynamik")
    print("\t3. Bevægelse\n")

#Funktion til beregning af strøm 
def strøm_beregning():
  print('Hvad vil du finde inden for strøm')
  findeUdAf = input()
  if findeUdAf in uMuligheder:
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
          
          print('Når strømstyrken er ' + str(I) + ' ampere, og spændingsforskellen er ' + str(U) + ' volt, er resistansen ' + str(R) + ' ohm')
      
      if option == '2':
          print('Hvad er strømstyrken i ampere?')
          I = input()
          print('Hvad er effekten i watt?')
          P = input()
          R= int(P) / (int(I) ** 2)
          
          print('Når strømstyrken er ' + str(I) + ' ampere, og effekten er ' + str(P) + ' watt, er resistansen ' + str(R) + ' volt')
      

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
          
          print('Når resistansen er ' + str(I) + ' ohm, og spændingsforskellen er ' + str(U) + ' volt, er strømstyrken ' + str(I) + ' ampere')
      
      if option == '2':
          print('Hvad er spædningsforskellen i volt')
          U = input()
          print('Hvad er effekten i watt')
          P = input()
          I= int(P) / int(U)
          
          print('Når spædningsforskellen er ' + str(U) + ' volt, og effekten er ' + str(P) + ' watt, er strømstyrken ' + str(I) + ' ampere')
      
      if option == '3':
          print('Hvad er resistansen i ohm?')
          R = input()
          print('Hvad er effekten i watt?')
          P = input()
          I= math.sqrt((int(P) / int(R)))
          
          print('Når resistansen er ' + str(R) + ' ohm, og effekten er ' + str(P) + ' watt, er strømstyrken ' + str(I) + ' ampere')
    

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
          
          print('Når strømstyrken er ' + str(I) + ' ampere, og spændingsforskellen er ' + str(U) + ' volt, er effekten ' + str(P) + ' watt')
      
      if option == '2':
          print('Hvad er resistansen i ohm')
          R = input()
          print('Hvad er strømstyrken i ampere')
          I = input()
          P= int(R) * int(I)**2
          
          print('Når resistansen er ' + str(R) + ' ohm, og strømstyrken er ' + str(I) + ' ampere, er strømstyrken ' + str(P) + ' watt')

#Funktioner til termodynamik beregning. 
def spørg_efter_værdier(message):
  værdi = input(f"{message} : ")
  return float(værdi)

def vælg_emne(message):
  value = input(f"{message} : ")
  return int(value)

def beregn_tryk (F , A):
    return F/A

def beregn_kraft (A , P):
   return A * P

def beregn_areal (F , P): 
   return F/P

def termo_beregning():
  while True: 
    emne_valg = vælg_emne("Hvilken værdi vil du gerne finde Tryk(1), Kraft(2), Areal(3)")
    if emne_valg == 1 : 
        kraft = spørg_efter_værdier("Indtast kraft i newton")
        areal = spørg_efter_værdier("Indtast areal i m^2")
        P = beregn_tryk (kraft , areal)
        print("Tryk er fundet ved P=F/A , beregningen ser ud som følgende:" + str(P) + " = " + str(kraft) + "/" + str(areal))
    if emne_valg == 2: 
        areal = spørg_efter_værdier("Indtast areal i m^2")
        tryk = spørg_efter_værdier("Indtast tryk i pascal")
        F=beregn_kraft(areal , tryk)
        print(F)
    if emne_valg == 3:
        kraft = spørg_efter_værdier("Indtast kraft i newton")
        tryk = spørg_efter_værdier("Indtast tryk i pascal")
        A = beregn_areal(kraft , tryk)
        print(A)
    
    break

#Funktion til beregning af bevægelse 
def bevægelse_beregning():
  print('Hvad vil du finde inden for bævegelse')
  findeUdAf = input()
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
      
      print('Når strækningen er ' + str(s) + ' meter, og tiden er ' + str(t) + ' sekunder, er hastigheden ' + str(v) + ' m/s')
  
  if option == '2':
      print('Hvad er accelerationen i m/s^2?')
      a = input()
      print('Hvad er tiden i sekunder?')
      t = input()
      v= int(a) * int(t)
      
      print('Når accelerationen er ' + str(a) + ' m/s^2, og tiden er ' + str(t) + ' sekunder, er hastigheden ' + str(v) + ' m/s')


  if findeUdAf in sMuligheder:
      print('Du vil finde stækningen (s).')
      print('Hvad er hastigheden i m/s?')
      v = input()
      print('Hvad er tiden i sekunder?')
      t = input()
      s = int(v) * int(t)

      print('Når hastigheden er ' + str(v) + ' m/s, og tiden er ' + str(t) + ' sekunder, er strækningen ' + str(s) + ' meter')

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
          
          print('Når strækningen er ' + str(s) + ' meter, og hastiheden er ' + str(v) + ' m/s, er tiden ' + str(t) + ' s')
      
      if option == '2':
          print('Hvad er hastigheden i m/s?')
          v = input()
          print('Hvad er accelerationen i m/s^2?')
          a = input()
          t= int(v) / int(a)
          
          print('Når accelerationen er ' + str(a) + ' m/s^2, og tiden er ' + str(t) + ' sekunder, er hastigheden ' + str(v) + ' m/s')


  if findeUdAf in aMuligheder:
      print('Du vil finde stækningen (a).')
      print('Hvad er hastigheden i m/s?')
      v = input()
      print('Hvad er tiden i sekunder?')
      t = input()
      a = int(v) / int(t)

      print('Når hastigheden er ' + str(v) + ' m/s, og tiden er ' + str(t) + ' sekunder, er strækningen ' + str(s) + ' meter')



while True: 
    def origin():
      back_or_exit=vælg_emne("Hvis du gerne vil tilbage til forsiden tast 1 \n Hvis du gerne vil aflsutte programmet tast 2")
      if back_or_exit == 1:
          continue
      if back_or_exit == 2:
          break 
    
    welcome()
    main_topic = vælg_emne("Indtast nu 1, 2 eller 3")
    if main_topic == 1 : 
      strøm_beregning()
      origin()
    if main_topic == 2:    
      termo_beregning()
      origin()
    if main_topic == 3 :
      bevægelse_beregning()
      origin()
    break

