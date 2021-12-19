#ACTIVIDAD 1 PALINDROMO

def es_palindromo(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    if(palabra_invertida == palabra):
        return True
    else:
        return False

palabra = input("Escriba una palabra para evaluar si es un Palindromo: ")
print(es_palindromo(palabra))