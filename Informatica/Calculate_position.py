#Create a Python program that analyzes the motion of an object based on user input. 
#The program will calculate the final position (x), velocity (v), and acceleration (a) of the object
print("En este programa se calculará la posición de una partícula suponiendo un movimiento uniformemente acelerado")
x0 = float(input("Introduzca la posición inicial en metros: "))
v0 = float(input("Introduzca la velocidad inicial en metros por segundo: "))
a = float(input("Introduzca la aceleración en metros por segundo al cuadrado: "))
t = float(input("Introduzca el tiempo en segundos: "))

x = x0 + v0*t + (0.5*a*(t**2))
v = v0 + a*t

print("La posición de la partícula tras", t, "s es:", x, "m")
print("La velocidad de la partícula es", v, "m/s")
print("La aceleración es constante, por lo que", a, "sigue siendo la aceleración")