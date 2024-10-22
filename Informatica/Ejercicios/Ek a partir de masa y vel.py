#Inputar masa en kg
mass = float(input("enter the positive mass in kg: "))

while mass < 0: #Funcion para evitar que se inpute valores negativos de masa
    mass = float(input("se necesitan inputar valores positivos, enter the positive mass in kg: "))
else:
    velocity = float(input("enter the velocity in m/s: ")) #Inputo de velocidad 
    KE = (1/2 * mass * velocity**2) #Calculo de Energia cinetica
    print ("La energia cinetica es:", KE, "N") #Output de energia cinetica