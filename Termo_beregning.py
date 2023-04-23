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
        # print(P)
        print(f"Tryk er fundet ved P=F/A , beregningen ser ud som følgende: {P} Pa = {kraft} N / {areal} m^2")
    if emne_valg == 2: 
        areal = spørg_efter_værdier("Indtast areal i m^2")
        tryk = spørg_efter_værdier("Indtast tryk i pascal")
        F=beregn_kraft(areal , tryk)
        print(f"Kraft er fundet ved F=A*P, beregningen ser ud som følgende: {F} N = {areal} m^2 * {tryk} pa ")
    if emne_valg == 3:
        kraft = spørg_efter_værdier("Indtast kraft i newton")
        tryk = spørg_efter_værdier("Indtast tryk i pascal")
        A = beregn_areal(kraft , tryk)
        print(f"Areal er fundet ved A=F/P, beregningen ser ud som følgende: {A} m^2 = {kraft} N * {tryk} pa ")
    
    break

termo_beregning()

