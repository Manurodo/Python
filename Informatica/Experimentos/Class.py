from datetime import datetime, date

class confirmar_fecha:
    def __init__(self,name, age_cadena):

        self.age_cadena = age_cadena
        self.name = name

    def confirmar_fecha(self):
        try:
            age = datetime.strptime(self.age_cadena, "%Y-%m-%d").date()
            if age > date.today():
                return False  # La fecha es futura
            return True  # La fecha es válida y no es futura
        except ValueError:
            return None  # La fecha no es válida

class Compañero: 

    aula = "A404"

    def __init__(self, name, age, sex, telf):
        self.name = name
        self.age = age
        self.sex = sex
        self.telf = telf
        self.hobbies = []
        self.notes = []
        self.friends = []
        self.date_birth = ()

    def introducir(self):
        return f"Wenas gente, me llamo {self.name} y tengo {self.age} años."
    
    def añadir_hobby(self, hobby):
        self.hobbies.append(hobby)
        return f"{self.name} añadió {hobby} como un nuevo hobby"
    
    def mostrar_hobbies(self):
        if self.hobbies:
            return f"Los pasatiempos de {self.name} son: {','.join(self.hobbies)}"
        else:
            return f"{self.name} no tiene pasatiempos aún."
        
    def realizar_cumpleaños(self):
        self.age += 1
        return f"{self.name} acaba de tener un cumpleaños, ahora tiene {self.age} años"
    
    def añadir_nota(self, note):
        self.notes.append(note)
        return f"{self.name} añadio una nueva nota"
    
    def añadir_amigo(self, friend):
        self.friends.append(friend)
        return f"{self.name} es ahora amigo de {friend}"
    
    def info(self):
        return print(f"{self.name}, {self.age}, {self.sex}, {self.telf}, {self.hobbies}, {self.friends}, {self.notes}") 
    
    def introducir_cumple(self, confirmar_fecha):
        return 

class Bank_account:
    def __init__ (self, account):
        self.account_number = account
