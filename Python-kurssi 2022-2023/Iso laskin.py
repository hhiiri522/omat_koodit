#!/bin/python3#
print("Vaikeat laskut")
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
lasku = input("Kirjoita laskutoimituksen merkki: ")
if lasku == "+":
  print(luku1+luku2)
elif lasku == "-":
  print(luku1-luku2)
elif lasku == "*":
  print(luku1*luku2)
elif lasku == "/":
  print(luku1/luku2)