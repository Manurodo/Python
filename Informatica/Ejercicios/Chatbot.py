import random
from datetime import *
class confirmar_fecha:
    def __init__(self,name, age_cadena):

        self.age_cadena = age_cadena
        self.name = name

    def confirmar_fecha(self):
        try:
            age = datetime.strptime(self.age_cadena, "%Y-%m-%d").date()
            if age > date.today():
                return False  # La fecha es futura
            return True  # La fecha es válida y no es futura
        except ValueError:
            return None  # La fecha no es válida


#Objetivo:Encontrar edad y nombre de una persona
n_scam = random.randint(20, 99999)

name = input ("Wenas, encantado men. Me llamo Manuel, como te llamas tu? ")
print ("Encantado tio, como sea, lo siento por preguntar pero es que necesito tu fecha de nacimiento. Ya es tarde y solo he robado datos de ",n_scam, "personas" )
age = input ("Cual es tu fecha de nacimiento? AAAA-MM-DD ")
scam = confirmar_fecha(name, age)

while True:
    if scam.confirmar_fecha() is None:
        print("Creo que la fecha que pusiste no existe o no es válida. No pasa nada, todo el mundo se equivoca. Pero como te decía, tengo prisa, así que me puedes decir una fecha válida, por favor.")

    elif not scam.confirmar_fecha():
        print("¡Ostia chaval! ¡Un viajero del tiempo! Pero no, en serio, por favor, necesito tu fecha de nacimiento.")

    elif scam.confirmar_fecha() is str("underage"):
        print("Ufff, meterme con los datos de un menor puede ponerme en problemas, mejor dejamos la fecha sin registrar")
        und = 1
        break
    else:
        und = 0
        break  

    age = input("Venga, de nuevo, el formato era AAAA-MM-DD, por si acaso tenías dificultades de aprendizaje: ")
    scam.age_cadena = age




