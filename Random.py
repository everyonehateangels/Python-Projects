# Example 1

# Uses a random integer
from random import *

aleatorio = randint(1,50)

print(aleatorio)

# Example 2
# Uses a random float but gives too many numbers so we use the function round() to make the number smaller.
# We can put how many amont of numbers we want next to the .

aleatorio_2 = round(uniform(1,5),1)

# Example 3
# This value must have nothing inside the fuction (0 to 1) useful for "fracciones"
aleatorio_3 = random()


# Example 4
# Chooses a random item from an array

colores = ["azul","rojo","verde","amarillo"]
aleatorio_4 = choice(colores)

print(aleatorio_4)


# Example 5
# You can't storage in an array. (Obviusly you can't use it in strings)
# All the index of the array changes randomly.
numeros = list(range(5,50,5))
shuffle(numeros)

print(numeros)

# Práctica Random 1
# Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena
# dicho valor en una variable llamada aleatorio

aleatorio = randint(1,10)

print(aleatorio)

# Práctica Random 2
# Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1,
# y almacena dicho valor en una variable llamada aleatorio

aleatorio = random()

print(aleatorio)

# Práctica Random 3
# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a
# continuación,
# y almacena el nombre escogido en una variable llamada sorteo.
#
# nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

sorteo = choice(nombres)

print(sorteo)
