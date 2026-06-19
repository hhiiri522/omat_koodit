#!/bin/python3#
import random
print("KIVI, SAKSET, PAPERI-peli\n")
pistemaara = 0
while True:
  tietokone = random.randint(1,3)
  try:
    valinta = input("Kirjoita, minkä valitset.")
  except Exception:
    print("Nyt tapahtui valitettavasti virhe.")
  
  if tietokone == 1:
    tietokone = "kivi"
  elif tietokone == 2:
    tietokone = "sakset"
  elif tietokone == 3:
    tietokone = "paperi"
    
  print("Tietokone:", tietokone)
  
  if valinta == 1:
    valinta = "kivi"
  elif valinta == 2:
    valinta = "sakset"
  elif valinta == 3:
    valinta = "paperi"
    
  if valinta == tietokone:
    print("tasapeli")
  
  elif valinta == "kivi":
    if tietokone == "sakset":
      print("Kivi tylsyttää sakset. Sinä voitit!")
      pistemaara = pistemaara+8
      print(pistemaara)
    else:
      print("Paperi voittaa kiven. Sinä hävisit!")
      pistemaara = pistemaara-3
      print(pistemaara)
  elif valinta == "sakset":
    if tietokone == "paperi":
      print("Sakset leikkaa paperin. Sinä voitit!")
      pistemaara = pistemaara+8
      print("Pisteitä sinulla on", pistemaara, ".")
    else:
      print("Kivi tylsyttää sakset. Sinä hävisit!")
      pistemaara = pistemaara-3
      print(pistemaara)
  elif valinta == "paperi":
    if tietokone == "kivi":
      print("Paperi voittaa kiven. Sinä voitit!")
      pistemaara = pistemaara+8
      print("Pisteitä sinulla on", pistemaara, ".")
    else:
      print("Sakset leikkaa paperin. Sinä hävisit!")
      pistemaara = pistemaara-3
      print(pistemaara)
  elif valinta == "lopeta":
    print("Peli lopetetaan. Kiva, että pelasit!")
    break