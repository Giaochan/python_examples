class Triangulos:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        Triangulos.detector_triangulo(self)
        
    def detector_mayor(self):   
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"el lado con el mayor tamaño es {self.lado1}")
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print(f"el lado con el mayor tamaño es {self.lado2}")
        elif self.lado3 > self.lado1 and self.lado3 > self.lado2:
            print(f"el lado con el mayor tamaño es {self.lado3}")
        else:
            pass
    
    def detector_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es un triangulo  Equilatero, todos sus lados son iguales por lo que no tiene un lado mas largo que otro.")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3:
            print("Es un triangulo Escaleno Ya que todos los lados son diferentes.")
            Triangulos.detector_mayor(self)
        else:
            print("Es un triangulo isoceles")
            Triangulos.detector_mayor(self)  
            
            
Triangulos(int(input("Digite el primer lado: ")), int(input("Digite el segundo lado: ")), int(input("Digite el tercer lado: ")))