class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Digite un valor: "))
        self.valor2 = int(input("digite otro valor: "))
        Calculadora.suma(self)
        Calculadora.resta(self)
        Calculadora.multiplicacion(self)
        Calculadora.division(self)
    
    def suma(self):
        resultado_suma = self.valor1 + self.valor2
        print(f"la suma de los dos valores es: {resultado_suma} ")
    def resta(self):
        resultado_resta = self.valor1 - self.valor2
        print(f"la resta de los dos valores es: {resultado_resta} ")
    def multiplicacion(self):
        resultado_multiplicacion = self.valor1 * self.valor2
        print(f"la multiplicacion de los dos valores es: {resultado_multiplicacion} ")
    def division(self):
        resultado_division = self.valor1 / self.valor2
        print(f"la division de los dos valores es: {resultado_division} ")    
        
Calculadora()       