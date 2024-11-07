class Animal:
    def __init__ (self, species):
        self.species = species
        self.stamina = 0

    def sleep (self):
        self.stamina += 100
    
    def info_stam (self):
        print (self.stamina)
    
    def speak(self):
        pass

class Persona(Animal):
    def speak(self):
        return "Hola"

class Perro(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self. breed = breed

    def speak(self):
        return "Guau"
    
    def sleep(self):
        return super().sleep()
    
a=Perro(Animal)
a.sleep ()
a.info_stam ()