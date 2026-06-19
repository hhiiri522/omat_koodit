#!/bin/python3 #
sana = input("Anna jonkinlainen sana: ")

def sanalaskuri():
  print("Sanassa on", len(sana), "merkkiä.")
  
  if len(sana) < 15:
    print("Sana on lyhyt.")
  else:
    print("Sana on pitkä.")
    
def sanasotku():
  print(sana.replace("a", "o"))
  
def sanakaantaja():
  print(sana[::-1])

sanalaskuri()
sanasotku()
sanakaantaja()