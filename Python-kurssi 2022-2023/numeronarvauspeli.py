#!/bin/python3#
import random
numero = random.randint(1,10)
arvaus = int(input("Arvaa: "))

while True:
  if arvaus == numero:
    print("Arvasit oikein!")
    break
  elif arvaus < numero:
    print("Tietokone valitsi suuremman numeron.")
    arvaus = int(input("Arvaa: "))
  elif arvaus > numero:
    print("Tietokone valitsi pienemmän numeron.")
    arvaus = int(input("Arvaa: "))