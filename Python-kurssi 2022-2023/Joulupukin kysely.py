print("KYSELY JOULUPUKILTA")
print("Voit vastata vain kyllä tai en.")
kysymys = input("Oletko ollut kiltti tänä vuonna?")
if kysymys == "kyllä":
  print("Hienoa, saat paljon lahjoja!")
elif kysymys == "en":
  print("Voi ei, et saa lahjoja!")
else:
  print("Voit vastata vain 'kyllä' tai 'et'.")