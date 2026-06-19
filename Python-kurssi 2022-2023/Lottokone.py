#!/bin/python3#
import random
print("LOTTOKONE\n")
# Kone arpoo seitsemän numeroa väliltä 1-40. Yritä arvata samat!

numerot = []

while True:
  if len(numerot) == 7:
    break
  
  luku = random.randint(1,40)
  if luku not in numerot:
    numerot.append(luku)
    numerot.sort()
    
print("Kone arpoi seuraavat numerot:")
for i in numerot:
  print(i, end =" ")