dic = {"clave 1":100, "clave 2":500}

a = dic.popitem()
print(a)
print(dic)


# Práctica Métodos y Ayuda 1
# Remueve los caracteres a la izquierda de nuestro texto principal:
#
# ,
#
# :
#
# %
#
# _
#
# #
#
# Utiliza el método lstrip(). Imprime el resultado en pantalla:
#

# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa.
# Puedes utilizar variables intermedias si las necesitas.

string = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
method_lstrip = string.lstrip(", : % _ #")


print(method_lstrip)


# Práctica Métodos y Ayuda 2
# Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
#
# el método insert():
#
#
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa
# y cómo es su funcionamiento.


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
insertado = frutas.insert(3,"naranja")

print(insertado)

# Práctica Métodos y Ayuda 3
# Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común),
# utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa
# y cómo es su funcionamiento.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)

print(conjuntos_aislados)