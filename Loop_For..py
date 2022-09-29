list = ["a","b","c"]

# We can use an inside variable inside of for loop

# Example 1
for letter in list:
   number_letter = list.index(letter) + 1
   print(f"Letra {number_letter}: {letter}")

# Example 2

lista = ["pablo", "laura", "fede", "luis", "julia"]

for nombre in lista:
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

# Example 3

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor)

# Example 4

palabra = "Python"

for letra in palabra:
    print(letra)

# Práctica Loop For 1
# Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.
#
# Por ejemplo: "Hola María"
#
# alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for nombre in alumnos_clase:
    print(f"Hola {nombre}")

# Práctica Loop For 2
# Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena
# el resultado de la suma en una variable llamada suma_numeros:
#
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_numeros = 0

for numeros in lista_numeros:
    suma_numeros = suma_numeros + numeros
# Práctica Loop For 3
# Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variable
# s suma_pares y suma_impares respectivamente:
#
# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#
# *Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par,
# y 1 cuando es impar
#
# num % 2 == 0 (valores pares)
#
# num % 2 == 1 (valores impares)
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numeros in lista_numeros:
    if numeros % 2 == 0:
        suma_pares = suma_pares + numeros
    elif numeros % 2 == 1:
        suma_impares = suma_impares + numeros