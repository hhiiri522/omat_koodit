#!/bin/python3#
print("LÄMPÖTILAMUUNNIN")
print("Kirjoita muunnettavan lämpötilayksikön nimi isolla alkukirjaimella!")

celsius = 1
fahrenheit = 33.80
kelvin = 274,15

yksikko = input("Mihin haluat muuntaa celsius-asteet? ")
maara = int(input("Kuinka monta astetta haluat muuntaa? "))
if yksikko == "Fahrenheit":
  muunnos = fahrenheit * maara
  print(maara, "celsiusastetta on sama kuin", muunnos, "fahrenheitastetta")
elif yksikko == "Kelvin":
  muunnos = kelvin * maara
  print(maara, "celsiusastetta on sama kuin", muunnos, "kelvinastetta")