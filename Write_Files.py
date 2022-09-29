archivo = open("prueba1.txt", "w")

lista = (["Hola","Mundo","Aqui","Estoy"])

for s in lista:
    archivo.writelines(s + "\n")
archivo.close()

archivo.write("Nuevo texto")

# Práctica Crear y Escribir Archivos 1
# Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

archivo_escritura = open("mi_archivo.txt", "w")

new_text = archivo_escritura.write("Nuevo texto")

archivo_escritura.close()

archivo_lectura = open("mi_archivo.txt", "r")

print(archivo_lectura.read())

archivo_lectura.close()

# Práctica Crear y Escribir Archivos 2
# Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
#
# Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
file = open("mi_archivo.txt","a")
added_content = file.write("Nuevo inicio de sesión")

file.close()

lectura = open("mi_archivo.txt", "r")
print(lectura.read())

lectura.close()

# Práctica Crear y Escribir Archivos 3
# Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" .
# Inserta un tabulador entre cada elemento de la lista para separarlos.
#
# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
#
# Imprime el contenido completo de "registro.txt" al finalizar.
#
# Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo
# en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
file = open("registro.txt", "w")

for value in registro_ultima_sesion:
    file.writelines(value + "\t")

file.close()

readable = open("registro.txt", "r")

print(readable.read())

readable.close()