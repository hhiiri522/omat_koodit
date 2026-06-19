print("VALITSE SALASANA")
print("""Anna salasana. Sen pituus tulee olla ainakin kahdeksan merkkiä.
Anna vähintään yksi iso kirjain ja pieni kirjain, yksi numero ja yksi erikoismerkki.""")

while True:
  salasana = input("Keksi ja anna salasana:")
  
  if len(salasana) >= 8 and any(i.isdigit() for i in salasana) and any(i.isalpha() for i in salasana) and any(not i.isalnum() for i in salasana) and any(i.isupper() for i in salasana):
    
    print("Salasana on hyvä =) Kirjaudutaan sisään")
    break
    
  else:
    print("Keksimäsi salasanasi ei täytä vaatimuksia!")