from random import *



input("¡Bienvenido al juego del ahorcado!, pulsa enter para continuar")

lista_random = ["rotulador","movil","telefono","cargador","aire"]

eleccion = choice(lista_random)


def pedir_letra(letra):
    print(len(eleccion))
    input_user = input("Introduce una letra")
    if letra != str:
        print("")