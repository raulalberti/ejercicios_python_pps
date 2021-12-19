#ACTIVIDAD 2 ADIVINAR NÚMERO DEL 1 AL 10

import random
numero = 0

def adivinar(numero):
    contador = 1
    num_aleatorio = random.randint(1, 10)
    while contador <= 10:
        numero = int(input('Escribe un numero del 1 al 10, y suerte!! =): '))
        if(num_aleatorio == numero):
            print('Enhorabuena has acertado el numero!! =)')
            break
        elif(contador == 10):
            print('Has llegado el máximo de intentos. Vuelve a ejecutarlo para volver a jugar')
            break
        else:
            print('Lo siento no es el correcto. Vuelve a intentarlo')
            contador += 1

print(adivinar(numero))