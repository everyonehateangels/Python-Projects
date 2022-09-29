name = "Carina"
name.replace()


# Práctica Propiedades de Strings 1
# Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son
# multiplicables y puedes realizar esta actividad de forma simple y elegante
texto = "Repetición"

print(texto*15)

# Práctica Propiedades de Strings 2
# Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#
# Tierra mojada,
#
# mis recuerdos de viaje
#
# entre las lluvias

poema = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in poema)


# Práctica Propiedades de Strings 3
# Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista

length = len("electroencefalografista")
print(length)