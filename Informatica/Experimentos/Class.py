class Person: 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []
        self.notes = []

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
        return f"{self.name} tiene {self.age} años"
    
    def añadir_nota(self, note):
        self.notes.append(note)
        return f"{self.name} añadio una nueva nota"

yo = Person("Manuel", 17)
print 
