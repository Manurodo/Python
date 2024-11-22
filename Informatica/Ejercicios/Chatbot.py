import random
from datetime import *
from Class import fecha

#Objetivo:Encontrar edad y nombre de una persona
n_scam = random.randint(20, 99999)

name = input ("Wenas, encantado men. Me llamo Manuel, como te llamas tu? ")
print ("Encantado tio, como sea, lo siento por preguntar pero es que necesito tu fecha de nacimiento. Ya es tarde y solo he robado datos de ",n_scam, "personas" )
print ("Cual es tu fecha de nacimiento? AAAA-MM-DD ")
age = input ("/>")

scam = fecha(name, age)


while True:
    if scam.confirmar_fecha() is None:
        print("Creo que la fecha que pusiste no existe o no es válida. No pasa nada, todo el mundo se equivoca. Pero como te decía, tengo prisa, así que me puedes decir una fecha válida, por favor.")

    elif scam.confirmar_fecha() is False:
        print("¡Ostia chaval! ¡Un viajero del tiempo! Pero no, en serio, por favor, necesito tu fecha de nacimiento.")

    elif scam.underage() is True:
        print("Ufff, meterme con los datos de un menor puede ponerme en problemas, mejor dejamos la fecha sin registrar")
        break
    else:
        break  

    age = input("Venga, de nuevo, el formato era AAAA-MM-DD, por si acaso tenías dificultades de aprendizaje: ")
    scam.age_cadena = age
print ("gracias, shau")