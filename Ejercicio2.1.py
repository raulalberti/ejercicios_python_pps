#EJERCICIO 2.1

numero1 = int(input('Escriba el primer numero: '))
numero2 = int(input('Escriba el segundo numero: '))

def max(numero1,numero2):
    if(numero1 > numero2):
        print('El numero mayor es: ' + str(numero1))
    else:
        print('El numero mayor es: ' + str(numero2))

max(numero1,numero2)