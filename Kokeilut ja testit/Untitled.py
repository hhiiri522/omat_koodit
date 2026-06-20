import random
arpoja = random.randint(1,10)

while True:
kysymys = int(input("Arvaa numero väliltä 1-10: "))

  if kysymys > arpoja:
    print("Arvottu luku on pienempi.")
  elif kysymys < arpoja:
    print("Arvottu luku on suurempi.")
  elif kysymys == arpoja:
    print("Nyt arvasit oikein!")
    break