# 1 Práctica Métodos de String
# Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
lista_palabras = ["La","legibilidad","cuenta."]


unido = " ".join(["La","legibilidad","cuenta."])

print(unido)


# Práctica Métodos de String 2
# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
phrase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
phrase_facil = phrase.replace("difícil", "fácil")
phrase_finish = phrase_facil.replace("mala", "buena")

print(phrase_finish)



# Práctica Métodos de String 3
# Reemplaza en la siguiente frase:
#
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
#
# los siguientes pares de palabras:
#
# "difícil" --> "fácil"
#
# "mala" --> "buena"
#
# y muestra en pantalla la frase con ambas palabras modificadas.

phrase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
phrase_facil = phrase.replace("difícil", "fácil")
phrase_finish = phrase_facil.replace("mala", "buena")

print(phrase_finish)
