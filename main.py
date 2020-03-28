import re
import os
def Reglas():
    print("El validador de contraseña solo valida.\n ")
    print("1- Primer caracter debe ser una letra mayuscula.")
    print("2- Los siguientes 3 caracteres son números.")
    print("3- Los siguientes caracteres deben ser letras minúsculas.")
    print("4- los últimos 3 caracteres deben ser caracteres especiales.\n")
class ValidatePassaword():
  def __init__(self,contraseña,expresion):
     self.contraseña=contraseña
     self.expresion=expresion
   
  @staticmethod
  def validar():
      if re.search(expresion, contraseña):
        print("\nContraseña valida\n")
      else:
        print("\ncontraseña invalida\n")

while True:
  Reglas()
  print("Ingrese Contraseña\n")
  contraseña=input()
  expresion='^[A-Z][0-9]{3}[a-z]+[\W]{3}$'
  validar=ValidatePassaword(contraseña,expresion)
  validar.validar()
  input("oprima ENTER para continuar")
  os.system('clear')