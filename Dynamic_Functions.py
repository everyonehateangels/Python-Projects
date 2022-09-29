# def chequear_3_cifras(numero):
    #return numero in range(100,1000)

# suma = 450 + 570
# resultado = chequear_3_cifras(suma)

#print(resultado)


def chequear_3_cifras(lista):

    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras
resultado = chequear_3_cifras([55,99,6000])

print(resultado)

# Práctica Funciones Dinámicas 1
# Crea una función (todos_positivos) que reciba una lista de números como parámetro,
# y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo.
# Crea una lista llamada lista_numeros con valores positivos y negativos.
#
# No invoques la función, solo es necesario definirla.

lista_numeros = [1,-50,502,-5000,755,600,33,61]

def todos_positivos(lista_numeros):
    for value in lista_numeros:
        if value < 0:
            return False
        else:
            pass
    return True

# Práctica Funciones Dinámicas 2
# Crea una función (suma_menores) que sume los números de una lista
# (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000,
# y devuelva el resultado de dicha suma.

lista_numeros_2 = [1, 50, 500, 5000, 750]


def suma_menores(lista_numeros_2):
    suma = 0
    for value in lista_numeros_2:
        if value in range(1, 1000):
            suma += value
        else:
            pass
    return suma
# Práctica Funciones Dinámicas 3
# Crea una función (cantidad_pares)
# que cuente la cantidad de números pares que existen en una lista (lista_numeros),
# y devuelva el resultado de dicha cuenta.

lista_numeros_3 = [1, 2, 10, 15, 60, 70]


def cantidad_pares(lista_numeros_3):
    cuenta = 0
    for value in lista_numeros_3:
        if value % 2 == 0:
            cuenta += 1
        else:
            pass
    return cuenta
