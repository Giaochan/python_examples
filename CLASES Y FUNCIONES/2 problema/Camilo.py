class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.detector(self)
    
    def detector(self):
        if self.edad >= 18:
            print("es mayor de edad")
        else:
            print("no es mayor de edad")
            
persona1 = Persona(input("Digite el nombre : "), int(input("Digite la edad: ")))