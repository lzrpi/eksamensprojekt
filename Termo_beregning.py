def spørg_efter_værdier(message):
  line = input(f"{message} : ")
  return float(line)

def beregn_u (R , I):
    return I*R

Resistans = spørg_efter_værdier("Indtast resistans")
Styrke = spørg_efter_værdier("Indtast I")

u = beregn_u(Resistans, Styrke)

print(u)
