'''
Escribí una función que reciba un string y retorne True si es un palíndromo (esto es, si se lee igual de izquierda a derecha o de derecha a izquierda), False en caso contrario. Utilizar esta función en un programa que permita al usuario ingresar palabras hasta que ingrese la palabra “fin” (suponer que todas las palabras son en minúsculas o todas en mayúsculas, de forma consistente). Al finalizar, mostrar la cantidad de palíndromos ingresados.
'''

def voltear_palabra(palabra_para_voltear):
    palabra_volteada = palabra_para_voltear[::-1]
    return palabra_volteada

def check_palindromo(palabra_digitada, palabra_volteada):
    if palabra_digitada == palabra_volteada:
        return (1)
    else:
        return (0)

def pregunta():
    palabra_digitada = input("digite una palabra: ")
    return palabra_digitada

def ciclonador():
    palabra = pregunta()
    palabra_volteada = voltear_palabra(palabra)
    return {"is_palindromo" : check_palindromo(palabra, palabra_volteada), "palabra": palabra, "palabra_volteada" : palabra_volteada};

def contador():
    contador_palindromos = 0
    print("test1")
    while True:
        dictionario = {}
        dictionario = ciclonador()
        print("test2")
        if dictionario["palabra"] == "fin":
            print(contador_palindromos)
            break
        else:
            print("test else")
            if dictionario["is_palindromo"] == 1:
                contador_palindromos += 1 
            elif dictionario["is_palindromo"] == 0:
                print("no es un palindromo")

contador()

