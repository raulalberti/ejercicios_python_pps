#EJERCICIO 2.6

cadena = 'estoy probando'
def funcion_inversa(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

print(funcion_inversa(cadena))

