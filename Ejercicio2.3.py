#EJERCICIO 2.3

mi_lista = ['pepe','juan','manuela','sara','sandra','javi']

def longitud(mi_lista):
    cuenta = 0
    for nombres in mi_lista:
        cuenta += 1
    return cuenta

print('La longitud de la lista es: '+ str(longitud(mi_lista)))