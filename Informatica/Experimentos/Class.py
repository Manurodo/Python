class Person: 
    def _init_(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = []
    def introduce(self):
        return f"Wenas gente, me llamo {self.name} y tengo {self.age} años."
    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
        return f"{self.name} añadió {hobby} como un nuevo hobby"
    