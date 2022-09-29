from random import *



input("¡Bienvenido al juego del ahorcado!, pulsa enter para continuar: ")

lista_random = ["rotulador","movil","telefono","cargador","aire"]

eleccion = choice(lista_random)
lista_eleccion = list(eleccion)
print(lista_eleccion)
string = "abcdefghijklmnñopqrstuvwxyz"
list_string = list(string)


def hangman():
    lista_letras = []
    lista_letras_incorrectas = []
    vidas = 7
    guiones = list(len(eleccion) * "-")
    while vidas > 0:
        input_user = input("Introduce una letra: ").lower()
        # integer = len(eleccion)
        while input_user not in list_string:
            input_user = input("Introduce una letra valida: ").lower()
            if input_user in list_string:
                lista_letras.append(input_user)
                break
        if input_user not in eleccion:
            lista_letras_incorrectas.append(input_user)
            vidas -= 1
            print(f"Letra incorrecta, {lista_letras_incorrectas} Te quedan {vidas} vidas.")
        # This doesn't work
        elif input_user in lista_eleccion:
            lista_oculta = []
            for value in lista_eleccion:
                if value == input_user:
                    lista_oculta.append(input_user)
                else:
                    index = lista_eleccion.index(input_user)
                    guiones[index] = input_user
            print(" ".join(lista_oculta))
        # Till here
        elif input_user == eleccion:
            print(f"Enhorabuena has ganado el juego y la palabra correcta era {eleccion}, has ganado el juego con {vidas}"
                  f"restantes")
            break
    if vidas == 0:
        print("Lo siento, has perdido el juego.")
hangman()


# Teacher's version
# from random import choice
#
# palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
# letras_correctas = []
# letras_incorrectas = []
# intentos = 6
# aciertos = 0
# juego_terminado = False
#
#
# def elegir_palbra(lista_palabras):
#     palabra_elegida = choice(lista_palabras)
#     letras_unicas = len(set(palabra_elegida))
#
#     return palabra_elegida, letras_unicas
#
#
# def pedir_letra():
#     letra_elegida = ''
#     es_valida = False
#     abecedario = 'abcdefghijklmnñopqrstuvwxyz'
#
#     while not es_valida:
#         letra_elegida = input("Elige una letra: ")
#         if letra_elegida in abecedario and len(letra_elegida) == 1:
#             es_valida = True
#         else:
#             print("No has elegido una letra correcta")
#
#     return letra_elegida
#
#
# def mostrar_nuevo_tablero(palabra_elegida):
#
#     lista_oculta = []
#
#     for l in palabra_elegida:
#         if l in letras_correctas:
#             lista_oculta.append(l)
#         else:
#             lista_oculta.append('-')
#
#     print(' '.join(lista_oculta))
#
#
# def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
#
#     fin = False
#
#     if letra_elegida in palabra_oculta:
#         letras_correctas.append(letra_elegida)
#         coincidencias += 1
#     else:
#         letras_incorrectas.append(letra_elegida)
#         vidas -= 1
#
#     if vidas == 0:
#         fin = perder()
#     elif coincidencias == letras_unicas:
#         fin = ganar(palabra_oculta)
#
#     return vidas, fin, coincidencias
#
#
# def perder():
#     print("Te has quedado sin vidas")
#     print("La palabra oculta era " + palabra)
#
#     return True
#
#
# def ganar(palabra_descubierta):
#     mostrar_nuevo_tablero(palabra_descubierta)
#     print("Felicitaciones, has encontrado la palabra!!!")
#
#     return True
#
#
# palabra, letras_unicas = elegir_palbra(palabras)
#
# while not juego_terminado:
#     print('\n' + '*' * 20 + '\n')
#     mostrar_nuevo_tablero(palabra)
#     print('\n')
#     print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
#     print(f'Vidas: {intentos}')
#     print('\n' + '*' * 20 + '\n')
#     letra = pedir_letra()
#
#     intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)
#
#     juego_terminado = terminado

