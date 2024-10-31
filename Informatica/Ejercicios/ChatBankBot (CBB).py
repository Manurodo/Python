from Bank_account import BankAccount
from random import *
print ("Por favor introduzca su MyBank ID")
print ("Si no tiene un MyBank ID introduzca su nombre y le proporcionaremos un MyBanl ID nuevo")

in_ = input ("|:")
ID = in_
try:
    int(in_)
except:
    ValueError
    name = in_
    ID = randint (11111, 99999)
    print ("Buenas tardes",name,", soy su asistente personal del Banco MyManueBank y su nuevo ID es :", ID)
    



Costumer = BankAccount (ID)

print ("De entre los siguientes comandos introduzca la accion que le gustaría realizar:")
print ("1.Introducir: introduce la cantidad deseada dentro de su cuenta")
print ("2.Retirar: retire la cantidad indicada de su cuenta")
print ("3.Comprobar: Compruebe el balance de su cuenta")
comm = input ("|:")
