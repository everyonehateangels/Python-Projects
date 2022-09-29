# Enumerate index the elements.
lista = ["a","b","c"]

for indice,item in enumerate(range(50,55)):
    print(indice,item)


# Assign a list a tuple index.


mi_tuples = list(enumerate(lista))
print(mi_tuples)

# Práctica Enumerador 1
# Imprime en pantalla frases como la siguiente:
#
# '{nombre} se encuentra en el índice {indice}'
#
# Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().
#
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#
# Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.
#
# Tip: utiliza loops!

for indice,nombres in enumerate(lista_nombres):
    print(f"{nombres} se encuentra en el índice {indice}")
# Práctica Enumerador 2
# Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".
#
# Llama a la lista obtenida con el nombre de variable lista_indices .

string = "Python"

lista_indices = list(enumerate(string))

print(lista_indices)
# Práctica Enumerador 3
# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
#
#
# Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:
#
# Loops
#
# Condicionales if
#
# El método enumerate()
#
# Métodos de strings o indexado

lista_nombres2 = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]


for indice,name in enumerate(lista_nombres2):
    if name.startswith("M"):
        print(indice)
    else:
        continue
