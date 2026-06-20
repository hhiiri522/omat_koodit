import random
print("NUMERONARVAUSPELI - JUNIOR")
print("Valitse ja kirjoita numero väliltä 1-9.")
numero = random.randint(1,9)
arvaus = int(input("Arvaa ja kirjoita:"))
  
while True:
    
    if arvaus < numero:
      print("h")
      arvaus = int(input("Arvaa uudestaan: "))
      
    elif arvaus > numero:
      print("H")
      arvaus = int(input("Arvaa uudestaan: "))
      
    else:
      print("KYLLÄ, NUMERO ON ", numero ,"!")
      break
