# 1 Dic
# cliente = {"Nombre":"Juan", "Apellido":"Fuentes","Peso":88, "talla":1.64}
# consulta = cliente["talla"]
# print(consulta)


# 2 Dic & Arrays
# dic = {"c1":55, "c2":[10,20,30], "c3":{"s1":100,"s2":200}}
# print(dic["c2"][1])


# 3 Dic & Arrays to print a letter in Uppercase.

# dic = {"c1":["a", "b", "c"], "c2":["d", "e","f"]}
# print(dic["c2"][1].upper())

# 4 Add things to a Dictionary

# dic = {1:"a", 2:"b"}
# print(dic)

# dic[3] = "c" # How to add a key to a dictionary

# print(dic)

# dic[2] = "B" # How to overwrite an already created key.

# print(dic)

# print(dic.keys()) # Prints all the keys from a Dictionary

# print(dic.values()) # Prints all the values from a Dictionary

# print(dic.items()) # Prints everything of a Dictionary


# 1
# Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#
# nombre: Karen
#
# apellido: Jurgens
#
# edad: 35
#
# ocupacion: Periodista
#
# Los nombres de las claves y valores deben ser iguales a la consigna.

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])

# 2
# Práctica Listas 2
# Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#
# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#
# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas,
# para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)


# 3
# Actualiza la información de nuestro diccionario llamado mi_dic
# (reasignando nuevos valores a las claves según corresponda),
# y agrega una nueva clave llamada "pais" (sin tilde).


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["edad"]  = 36
mi_dic["ocupacion"] = "Editora"

mi_dic["pais"] = "Colombia"

print(mi_dic)