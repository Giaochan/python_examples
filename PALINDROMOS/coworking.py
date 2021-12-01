'''
Escribí una función que reciba un string y retorne True si es un palíndromo (esto es, si se lee igual de izquierda a derecha o de derecha a izquierda), False en caso contrario. Utilizar esta función en un programa que permita al usuario ingresar palabras hasta que ingrese la palabra “fin” (suponer que todas las palabras son en minúsculas o todas en mayúsculas, de forma consistente). Al finalizar, mostrar la cantidad de palíndromos ingresados.
'''

def inverse(palabra):
    reverse_palabra = palabra[::-1]
    return reverse_palabra

def check_palindromos(palabras):
    palindromos = []
    for i in palabras:
        data_word = i.lower()
        if (data_word == inverse(data_word)):
            palindromos.append(i)
    return palindromos
    
def ingresar_palabras():
    palabras = []
    lista_palindromos = []
    
    while True:
        palabra = input("Escribe una palabra que sea palindromo o cualquier otra: ")
        palabras.append(palabra)
        if  palabra.lower() == "fin":
            lista_palindromos = check_palindromos(palabras)
            break
        else:
            continue
    print(f"Hay {lista_palindromos.length} palindromos")
   
ingresar_palabras()
    
