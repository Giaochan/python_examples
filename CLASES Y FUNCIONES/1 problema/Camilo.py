class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        Estudiante.detector_calificacion(self)

    def detector_calificacion(self):
        if self.nota >= 3:
            print(f"has aprobado, felicidades tu nota es: {self.nota} !!")
            if self.nota == 5:
                print("tu calificacion es excelente")
            else:
                pass
        elif self.nota < 3 and self.nota > 0 :
            print("Lastima no aprobaste...")
        elif self.nota == 0:
            print("no tienes calificacion")
        else:
            pass

alumno_camilo = Estudiante(input("Digite el nombre del estudiante: "), int(input("Digite la nota del estudiante: ")))