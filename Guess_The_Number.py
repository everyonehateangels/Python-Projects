from random import *

name = input("¡Hola! Dime tu nombre: ")

question = print(f"{name} piensa un numero del 1 al 100 y tienes solo 8 intentos para adivinarlo! ¿Qué número será?.")


numero_secreto = randint(1,101)
# Range() starts with 0.

for value in range(8):
    print(f"Intento numero {value}")
    numero = int(input("Inserta un numero: "))
    value += 0
    if value == 7:
        print(f"Has perdido el juego con {value} intentos, el numero secreto era {numero_secreto}")
        break
    elif numero < 1 or numero > 100:
     print(f"No está permitido ese numero {value + 1} (-1 intento)\n")
    elif numero < numero_secreto:
     print(f"Respuesta Incorrecta. Has elegido un número menor al numero secreto {value + 1} (-1 intentos)\n")
    elif numero > numero_secreto:
     print(f"Respuesta Incorrecta. Has elegido un número mayor al numero secreto {value + 1} (-1 intentos)\n")
    elif numero == numero_secreto:
        print(f"Has ganado el juego con {value} intentos \n")
        break