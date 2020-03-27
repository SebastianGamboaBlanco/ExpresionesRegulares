import re

print("Ingrese Contraseña")
Contraseña=input()
if re.search('^[A-Z][0-9]{3}[a-z]+[\W]{3}$',Contraseña):
  print("Contraseña Valida")
else:
  print("Contraseña invalida")