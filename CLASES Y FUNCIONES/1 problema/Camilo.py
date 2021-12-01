class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        if nota >= 3:
            print(f"has aprobado, felicidades tu nota es: {nota} !!")
            if nota == 5:
                print("tu calificacion es excelente")
            else:
                pass
        elif nota < 3 and nota > 0 :
            print("Lastima no aprobaste...")
        elif nota == 0:
            print("no tienes calificacion")
        else:
            pass

alumno_camilo = Estudiante(input("Digite el nombre del estudiante: "), int(input("Digite la nota del estudiante: ")))