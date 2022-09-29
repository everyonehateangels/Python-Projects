# Ejercicio 1
# *-----------------------------------------------------------*
# |Crea una función llamada devolver_distintos() que reciba 3 |
# | integers como parámetros.                                 |
# |Si la suma de los 3 numeros es mayor a 15, va a devolver el|
# | número mayor.                                             |
# |Si la suma de los 3 numeros es menor a 10, va a devolver el|
# |número menor.                                              |
# | Si la suma de los 3 números es un valor entre 10 y 15     |
# | (incluidos) va a devolver el número de valorintermedio.   |
# *-----------------------------------------------------------*


def devolver_distintos(int_1, int_2, int_3):
    suma = int_1 + int_2 + int_3
    integers_list = [int_1, int_2, int_3]
    mayor = max(integers_list)
    menor = min(integers_list)
    intermedio = integers_list[1]
    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    elif suma in range(10, 16):
        return intermedio

print(devolver_distintos(2,4,6))

# Ejercicio 2
# Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido"
# debería devolver ['d',"e","i","n","o","r","t"]

def funcion_letras(palabra):
    palabra_separada = list(palabra)
    set_nuevo = set(palabra_separada)
    palabras_ordenadas = sorted(set_nuevo)
    return palabras_ordenadas

print(funcion_letras("Okaybro"))

# Ejercicio 3
# Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def consecutivo(*args):
    for value in args:
        if args[value] == args[value + 1]: # While indexing we add a "1" for the next value and if still the same,
            # returns True.
            return True
        else:
            continue
    return False

print(consecutivo(1,0,0,5,5,6,0))

# Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números
# primos hay en el rango que va desde cero hasta ese número
# incluido, y va a devolverla cantidad de números primos que
# encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos


def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)