

# Práctica Abrir y Manipular Archivos 1
# Abre el archivo texto.txt e imprime su contenido.
#
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open("prueba.txt")

print(mi_archivo.read())




# Práctica Abrir y Manipular Archivos 2
# Imprime la primera línea del archivo texto.txt
#
# No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.
#
# Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código

primera_linea = mi_archivo.readline()
print(primera_linea)

# Práctica Abrir y Manipular Archivos 3
# Abre el archivo texto.txt e imprime únicamente la segunda línea.
mi_archivo = open("texto.txt")

lineas = mi_archivo.readlines()

print(lineas[1])



mi_archivo.close()