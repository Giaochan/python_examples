'''Escribí un programa que solicite al usuario ingresar un número con decimales y
 almacenalo en una variable. A continuación, el programa debe solicitar al usuario
  que ingrese un número entero y guardarlo en otra variable. En una tercera variable
   se deberá guardar el resultado de la suma de los dos números ingresados por el usuario.
    Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, 
    donde “[suma]” se reemplazará por el resultado de la operación.'''

Decimal_de_usuario = input("Digite un numero Decimal: ")
Entero_de_usuario = input("Digite un numero Entero: ")

if Decimal_de_usuario == float:
    
    while Decimal_de_usuario == float:
        
        Decimal_de_usuario = input("Digite un numero Decimal: ")
        if Decimal_de_usuario == float:    
            break


if Entero_de_usuario == int:
    
    while Entero_de_usuario == int:
           
        Entero_de_usuario = input("Digite un numero Entero: ")
        if Decimal_de_usuario == int:    
            break

Entero_de_usuario = int(Entero_de_usuario)
Decimal_de_usuario = float(Decimal_de_usuario)
suma = Decimal_de_usuario + Entero_de_usuario
print(f"El resultado de la suma es: {suma}")

