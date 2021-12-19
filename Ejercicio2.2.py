#EJERCICIO 2.2

numero1 = int(input('Escriba el primer numero: '))
numero2 = int(input('Escriba el segundo numero: '))
numero3 = int(input('Escriba el tercer numero: '))

def max_de_tres(numero1,numero2,numero3):
    if(numero1 > numero2 and numero1 > numero3):
        print('El ' + str(numero1) + ' es el numero mayor de los tres')
    elif(numero2 > numero1 and numero2 > numero3):
        print('El ' + str(numero2) + ' es el numero mayor de los tres')
    else:
        print('El ' + str(numero3) + ' es el numero mayor de los tres')

max_de_tres(numero1,numero2,numero3)
