# EJERCICIO 1.1

calificacion = ('A', 'B', 'C', 'D', 'F')

num = int(input("Escriba un numero de 0 a 10: "))

if(num >= 9):
    print("Su calificación es: A")
elif(num >= 8 and num < 9):
    print("Su calificacion es: B")
elif(num >= 7 and num < 8):
    print("Su calificacion es: C")
elif(num >= 6 and num < 7):
    print("Su calificacion es: D")
else:
    print("Su calificacion es: F")
