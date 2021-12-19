#EJERCICIO 2.4

def vocal(letra):
    if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        return True
    else:
        return False

letra = input('Escriba un carácter: ')
print(vocal(letra))