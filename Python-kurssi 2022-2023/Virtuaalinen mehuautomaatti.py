#!/bin/python3#
print("VALUUTTAMUUNNIN")

euro = 1

punta = 0.88
kruunu = 11.17
yuan = 7.50
dollari = 1.06

print("Mitä valuuttaa haluat vaihtaa?")
print("1. Englannin punta")
print("2. Ruotsin kruunu")
print("3. Kiinan yuan")
print("4. USA:n dollari")

while True:

  try:
    osta = int(input("Valitse valuutta (1-4): "))
    if osta == 1 or osta == 2 or osta == 3 or osta == 4:
      pass
    else:
      osta = int(input("Väärä valuutta. Valitse se uudelleen: "))
  
  except ValueError:
    print("Tapahtui virhe. Anna lukuarvo.")
    continue
      
  raha = int(input("Kuinka monta euroa haluat vaihtaa? "))
  
  if osta == 1:
    muunnos = raha * punta
    print(raha, "euroa on yhteensä", muunnos, "Englannin puntaa")
    break
  
  elif osta == 2:
    muunnos = raha * kruunu
    print(raha, "euroa on yhteensä", muunnos, "Ruotsin kruunua")
    break
  
  elif osta == 3:
    muunnos = raha * yuan
    print(raha, "euroa on yhteensä", muunnos, "Kiinan yuania")
    break
  
  elif osta == 4:
    muunnos = raha * dollari
    print(raha, "euroa on yhteensä", muunnos, "USA:n dollaria")
    break
  
  else:
    print("Väärä valuutta, valitse uudelleen.")