import random
from datetime import *
from Class import fecha
from sympy import true


#Objetivo:Encontrar edad y nombre de una persona
n_scam = random.randint(20, 99999)
print (" ")
print ("Wenas, encantado men. Me llamo Manuel, como te llamas tu? ")
name = input ("/>")
print (" ")
print ("Encantado",name,", como sea, lo siento por preguntar pero es que necesito tu fecha de nacimiento. Ya es tarde y solo he robado datos de ",n_scam, "personas" )
print ("Cual es tu fecha de nacimiento? AAAA-MM-DD ")
age = input ("/>")
print (" ")
scam = fecha(age)

n = 1

while True:

    if scam.valid(age) is None:
        print (" ")
        print("Creo que la fecha que pusiste no existe o no es válida. No pasa nada, todo el mundo se equivoca. Pero como te decía, tengo prisa, así que me puedes decir una fecha válida, por favor.")
        x = x+1

    elif scam.valid(age) is False:
        print (" ")
        print("¡Ostia chaval! ¡Un viajero del tiempo! Pero no, en serio, por favor, necesito tu fecha de nacimiento.")
        x = x+1

    elif scam.underage() is True:
        print (" ")
        print("Ufff, meterme con los datos de un menor puede ponerme en problemas, mejor dejamos la fecha sin registrar")
        break
    elif x >= 3:
        print (" ")
        print ("Ok, im starting to think that you're kidding me, its the police on the line?")
        print ("Not that I care, im just a chatbot")
    elif x >= 5:
        print (" ")
        print ("oK, im done, bye")
        break
    else:
        print (" ")
        print ("gracias, shau")
        break  
    
    print (" ")
    print ("Venga, de nuevo, el formato era AAAA-MM-DD, por si acaso tenías dificultades de aprendizaje: ")
    age = input ("/>")
    scam.age_cadena = age
