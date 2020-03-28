import re
import emoji

class ValidatePassaword():
  def __init__(self,contraseña,expresion):
     self.contraseña=contraseña
     self.expresion=expresion
   
  @staticmethod
  def validar():
      if re.search(expresion, contraseña):
        print("Contraseña valida \U0001f44d \U0001F604")
      else:
        print("contraseña invalida \U0001F44E \U0001F641	")


print("Ingrese Contraseña")
contraseña=input()
expresion='^[A-Z][0-9]{3}[a-z]+[\W]{3}$'
validar=ValidatePassaword(contraseña,expresion)
validar.validar()