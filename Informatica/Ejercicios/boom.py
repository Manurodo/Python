import time
import datetime as dt
import random
n = random.randint(0,20) # Creo un int aleatorio
while n>0: # Mientras ese int no sea >=0 
    print (n) # 
    n=n-1 # Reducir el int por 1
    time.sleep(1) # Esperar 1 seg para la siguiente iteracion
print ("¡¡¡¡BOOM!!!!") # Al terminar la cuenta atras, output str de boom

