pregunta = str (input("Choose between C anf F: "))
if pregunta == ("C"):
    Celsius = int (input ("Por favor, introduce tu temp en Cº: "))
    Fahrenheit = Celsius * (9/5) + 32
    print ("La temperatura es ",Fahrenheit, " Fº")
else :
    Fahrenheit = int (input ("Por favor, introduce tu temp en Fº: "))
    Celsius = (Fahrenheit - 32) / (9/5)
    print ("La temperatura es ",Celsius, " Cº")