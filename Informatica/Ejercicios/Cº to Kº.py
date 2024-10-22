print ("Este es un programa que convierte de grados Cº a grados Fº y viceversa.")
type = str (input("Si quiere convertir Cº a Fº pulse C en caso contrario pulse F: "))
if type == ("C"):
    Cº = float (input("Introduzca grados Cº: "))
    Fº = (Cº * 9/5) + 32
    print (Cº, " grados centigrados es igual a ", Fº, "grados farenheit")
if type == ("F"):
    Fº = float (input("Introduzca grados Fº: "))
    Cº = (Fº - 32) * 5/9
    print (Fº, " grados farenheit es igual a ",Cº, " grados centigrados")




