#EJERCICIO 2.5

lista_num = [1,2,3,4]

def sum(lista_num):
    resultado = 0
    for valor in lista_num:
        resultado += valor
    return resultado

def multip(lista_num):
    resultado = 1
    for valor in lista_num:
        resultado *= valor
    return resultado

print('El resultado de la suma: ' + str(sum(lista_num)))
print('El resultado de la multiplicación: ' + str(multip(lista_num)))