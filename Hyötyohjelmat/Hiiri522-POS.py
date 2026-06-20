#!/bin/python3#
ostoslista = []
print("Kirjoita asiakkaan tuotteet.")

while True:
  kysymys = input("Mitä hän ostaa?")
  
  if kysymys == "jäätelö":
    ostoslista.append("Jäätelö 3,99€")
  elif kysymys == "cocacola":
    ostoslista.append("Coca Cola 1,50€")
  elif kysymys == "jaffa":
    ostoslista.append("Fanta 1,50€")
  elif kysymys == "näytä":
    print(ostoslista)
  elif kysymys == "lopeta":
    print(ostoslista)
    break
  else:
    print("Se ei kuulu listaan")