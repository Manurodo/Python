#Create a Python program that analyzes the motion of an object based on user input. 
#The program will calculate the final position (x), velocity (v), and acceleration (a) of the object
print ("En este programa se calculara la posicion de una particula suponiendo un movimiento uniformemente acelerado con actualizacion de 1 segundo")
x0 = int(input ("introduzca la posicion en metros: "))
v0 = int(input ("introduzca la velocidad en metros por segundo: "))
a = int(input ("introduzca la aceleración en metros por segundo al cuadrado: "))
t = 1
x = x0 + v0*t + (0.5*a*(t**2))
v = v0 + a*t
print("la posicion de la particula es", x, "m")
print("la velocidad de la particula es", v, "m*s")
print("la aceleracion es constante por lo que", a ,"sigue siendo la aceleración")