pregunta = str (input("Choose between C anf F: "))
if pregunta == ("C"): #Elige uno de los metodos C o F para calcular Cº o Fº respectivamente
    Celsius = int (input ("Por favor, introduce tu temp en Cº: "))
    Fahrenheit = Celsius * (9/5) + 32 #Calcula Cº
    print ("La temperatura es ",Fahrenheit, " Fº")
else :
    Fahrenheit = int (input ("Por favor, introduce tu temp en Fº: "))
    Celsius = (Fahrenheit - 32) / (9/5)#Calcula Fº
    print ("La temperatura es ",Celsius, " Cº")