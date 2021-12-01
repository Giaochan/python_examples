class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        if edad >= 18:
            print("es mayor de edad")
        else:
            print("no es mayor de edad")
            
persona1 = Persona(input("Digite el nombre : "), int(input("Digite la edad: ")))