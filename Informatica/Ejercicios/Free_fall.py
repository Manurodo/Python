from numpy import *
print ("input the initial height")
h = float(input ("|:"))
print ("input g")
g = float(input ("|:"))
t_l = linspace(1, 20, 10, True,) #Creo una lista de valores a partir de linspace
def calcular_altura(t_l):
    return [h - (1/2)*g*(t**2) for t in t_l] #Defino la funcion de calcular_altura como una que utiliza la ecuacion de caida libre
print ("Teniendo un tiempo", t_l,":")
y = calcular_altura(t_l) #Calculo la posicion vertical con la formula y la lista creada a partir de linspace
print ("La posicion vertical en el tiempo dado es", y)
d_fall = diff(y) #Calculo la diferencia entre el array de la altura
print ("La diferencia entre los valores de altura es:", d_fall)
avg = mean(d_fall) #Calculo la media de la distacia de caída
print ("La media de la distacia de caída es:", avg)