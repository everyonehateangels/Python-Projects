# Práctica Archivos y Funciones 1
# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido
# (read).


def abrir_leer(archivo):
    file = open(archivo, "r")
    leer = file.read()
    return leer


print(abrir_leer("ejemplo.txt"))


# Práctica Archivos y Funciones 2
# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro,
# y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    file = open(archivo, "w")
    new_content = file.write("contenido eliminado")
    return new_content


print(sobrescribir("ejemplo.txt"))

# Práctica Archivos y Funciones 3
# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro,
# y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución".
# Finalmente, debe cerrar el archivo abierto.

def registro_error(archivo):
    file = open(archivo, "a")
    new_content = file.write("se ha registrado un error de ejecución")
    file.close()

registro_error("log_errores.txt")