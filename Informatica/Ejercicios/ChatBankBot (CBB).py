from Bank_account import BankAccount
from random import randint

print ("Por favor introduzca su MyBank ID")
print ("Si no tiene un MyBank ID introduzca su nombre y le proporcionaremos un MyBank ID nuevo")

in_ = input ("|:")
ID = in_
try:
    int(in_)
except:
    ValueError
    name = in_
    ID = randint (11111, 99999)
    print ("Buenas tardes",name,"soy su asistente personal del Banco MyManueBank y su nuevo ID es :", ID)
else:
    print("")
    print ("Buenas tardes Client ID nº",ID,"soy su asistente personal del Banco MyManueBank")
    
Costumer = BankAccount (ID)
while True:
    print ("De entre los siguientes comandos introduzca la accion que le gustaría realizar:")
    print ("1.Depositar: introduce la cantidad deseada dentro de su cuenta")
    print ("2.Retirar: retire la cantidad indicada de su cuenta")
    print ("3.Comprobar: Compruebe el balance de su cuenta")
    comm = input ("|:")

    while comm not in ["1", "2", "3", "Depositar", "Retirar", "Comprobar"]:
        print("Comando inválido, por favor introduzca un número o nombre de comando válido.")
        comm = input("|:")

    if comm == "Depositar" or comm == "1":
        print ("Introduzca cantidad a depositar")
        quant = int (input ("|:"))
        print (Costumer.depositar(quant))

    if comm == "Retirar" or comm == "2":
        print ("Introduzca cantidad a retirar")
        quant = int (input ("|:"))
        print (Costumer.retirar(quant)) 

    if comm == "Comprobar" or comm == "3":
        print(Costumer.cantidad())
    
    if comm == "Salir":
        print ("Que tengaun buen dia")
        break