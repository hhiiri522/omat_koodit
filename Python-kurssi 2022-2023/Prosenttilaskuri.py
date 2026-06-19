#!/bin/python3#
print("PROSENTTILASKURI")

def luvunpyytaja():
  while True:
    try:
      luku = float(input("Anna luku:"))
      return luku
    except Exception:
      print("Virheellinen arvo, yritä uudelleen.")
      
numero = luvunpyytaja()

print("Anna prosentti (0-100):")
prosentti = luvunpyytaja()

tulos = (numero/100 * prosentti)
print(prosentti, "% luvusta", numero, "on", round(tulos))