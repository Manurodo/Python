from Bank_account import BankAccount
from random import *
print ("Por favor introduzca su MyBank ID")
print ("Si no tiene un MyBank ID introduzca su nombre y le proporcionaremos un MyBanl ID nuevo")

in_ = input ("|:")
if int(in_)  ValueError:
    name = in_
    ID = randint (11111, 99999)
    print ("Buenas tardes",name,", soy su asistente personal del Banco MyManueBank")
else:
    ID = in_


Costumer = BankAccount (ID)

print ("De entre los siguientes comandos introduzca la accion que le gustaría realizar:")
print ("Introducir: introduce la cantidad deseada dentro de su cuenta")
print ("Retirar: retire la cantidad indicada de su cuenta")
print ("Comprobar: Compruebe el balance de su cuenta")
comm = input ("|:")
