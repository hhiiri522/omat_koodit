import random
print("NUMERONARVAUSPELI")
print("Valitse ja kirjoita numero väliltä 1-9.")
numero = random.randint(1,9)
arvaus = int(input("Arvaa ja kirjoita:"))
  
while True:
    
    if arvaus < numero:
      print("Valitsit liian pienen numeron.")
      arvaus = int(input("Arvaa uudestaan: "))
      
    elif arvaus > numero:
      print("Valitsit liian suuren numeron.")
      arvaus = int(input("Arvaa uudestaan: "))
      
    else:
      print("KYLLÄ, NUMERO ON ")
      print(numero)
      break
