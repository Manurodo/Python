mass = int (input("Indicar la masa en kg: "))
while mass < 0:
    print ("La masa tiene que ser un valor positivo")
    mass = int (input("Indicar la masa en kg: "))
else :
    velocity = int (input("Indicar la velocidad en m/s: "))
    EK = 1/2 * mass * velocity ** 2
print ("La energia cinetica resultante es:", EK, " J")
