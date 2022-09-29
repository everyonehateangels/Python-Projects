import os
from pathlib import Path
from os import system
contador = 0


my_path = Path(r"C:\Users\angel\Downloads\Recetas\Recetas")
stop_program = False

def welcome():
    system("cls")
    print("*" * 50)
    print("Bienvenido al recetario del xamu, pulsa enter para continuar")
    number_of_recipes = list(my_path.glob("**/*.txt"))
    print(f"Tus recetas estan en {my_path}, tienes {len(number_of_recipes)} recetas")
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion")
        print('''Elige las siguientes opciones:
           [1] Leer receta.
           [2] Crear receta.
           [3] Crear Categoria.
           [4] Eliminar Receta.
           [5] Eliminar categoria.
           [6] Finalizar programa.\n
           ''')
        eleccion_menu = input()
        return int(eleccion_menu)

def categoria(ruta):
    print("Categorias: ")
    categories = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in categories.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias
def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("Elige una categoria ")

    return lista[int(eleccion_correcta) - 1]


def mostar_receta(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for value in ruta_recetas.glob("*.txt"):
        receta = str(value.name)
        print(f"[{contador}] - {receta}")
        lista_recetas.append(value)
        contador += 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = "x"

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("Elige una categoria ")

    return lista[len(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))
# ------------------------------------------------------------------------------------------------------------------
def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def crear_receta(ruta):
    existe = False
    while not existe:
        print("El nombre de tu receta:")
        nombre_receta = input() + ".txt"
        print("Escribe el contenido de tu nueva receta")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta, ya existe")

def crear_categoria(ruta):
    existe = False
    while not existe:
        print("Escribe el nombre de tu categoria:")
        nombre_categoria = input()
        nueva_categoria = Path(ruta, nombre_categoria)
        if not os.path.exists(nueva_categoria):
            Path.mkdir(nueva_categoria)
            existe = True
        else:
            print("Lo siento, esa categoria ya existe.")
def volver_al_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\n Presione V para volver al menu")





# Menu del recetario
while not stop_program:
    menu_eleccion = welcome()
    if menu_eleccion == 1:
        mis_categorias = categoria(my_path)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostar_receta(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        lectura = leer_receta(mi_receta)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_al_inicio()
    elif menu_eleccion == 2:
        mis_categorias = categoria(my_path)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
    elif menu_eleccion == 3:
        creadas = crear_categoria(my_path)
        volver_al_inicio()

    elif menu_eleccion == 4:
        mis_categorias = categoria(my_path)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostar_receta(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar = eliminar_receta(mi_receta)
        volver_al_inicio()
    elif menu_eleccion == 5:
        mis_categorias = categoria(my_path)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_cat = eliminar_categoria(mi_categoria)
        volver_al_inicio()

    elif menu_eleccion == 6:
        stop_program = True