"Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."

class Alumno:
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota
        if (nota > 7):
            print("Has pasado la materia")
        else:
            print("No has pasado la materia")



            
alumno = Alumno("Camilo", 10)
print(alumno) 

