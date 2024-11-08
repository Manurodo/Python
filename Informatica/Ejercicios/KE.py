mass = int (input("Indicar la masa en kg: "))
while mass < 0: #Crear bucle mientras la masa sea negativa
    print ("La masa tiene que ser un valor positivo")
    mass = int (input("Indicar la masa en kg: "))
else : #Si la masa no es negativa, csalcular la energia cinetica
    velocity = int (input("Indicar la velocidad en m/s: "))
    EK = 1/2 * mass * velocity ** 2
print ("La energia cinetica resultante es:", EK, " J")
