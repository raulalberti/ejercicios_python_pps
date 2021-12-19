#EJERCICIO 2.7

lista1 = [1,2,4,5,21,7]
lista2 = [0,15,6,9,32,26]

def superposicion(lista1,lista2):
    for valor1 in lista1:
        for valor2 in lista2:
            if valor1 == valor2:
                return True
    return False
print(superposicion(lista1,lista2))