# import zipfile
import os
import datetime
import math
import time
import re
from pathlib import Path
inicio = time.time()
fecha_actual = datetime.date.today()
ruta = r"C:\Users\angel\PycharmProjects\PrimerPrograma\Calculator\Mi_Gran_Directorio"
numeros_encontrados = []
archivos_encontrados = []
patron = r"N\D{3}-\d{5}"


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, "r")
    texto = este_archivo.read()

    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != "":
                numeros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())

def mostar_todo():
    indice = 0
    print("-" * 27)
    print(f"Fecha de búsqueda: {fecha_actual.day}-{fecha_actual.month}-{fecha_actual.year}")
    print("ARCHIVO\t \t NRO. SERIE")
    print(len("ARCHIVO") * "-", "\t", len("NRO. SERIE") * "-")
    for a in archivos_encontrados:
        print(f"{a}\t{numeros_encontrados[indice]}")
        indice += 1
    print(f"Números encontrados: {len(numeros_encontrados)} encontrados")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 27)

crear_listas()
mostar_todo()


# zip_abierto = zipfile.ZipFile("proyectodia9.zip", "r")

# zip_abierto.extractall()

