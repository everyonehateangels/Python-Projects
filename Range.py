# Práctica Rango 1
# Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista
# en la variable mi_lista.

# mi lista = list(range(2500,2586))

# Práctica Rango 2
# Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos
# de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.

mi_lista = list(range(3,301,3))

# Práctica Rango 3
# Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive).
# Almacena el resultado en una variable llamada suma_cuadrados.
#
# Para ello:
#
# Crea un rango de valores que puedas recorrer en un loop
#
# Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2).
# Puede que necesites crear variables intermedias (de manera opcional).
#
# Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
#

suma_cuadrados = 0

for n in range(1,16):
    print(n**2)
    suma_cuadrados += n**2