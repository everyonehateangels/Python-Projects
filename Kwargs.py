def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")


    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15,50,100,200,300,400,x="uno",y="dos",z="tres")


# Práctica sobre Argumentos Indefinidos (**kwargs) 1
# Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan
# , y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    return len(kwargs)

print(cantidad_atributos(pito="x",ekide="wow"))

# Práctica sobre Argumentos Indefinidos (**kwargs) 2
# Crea una función llamada lista_atributos que devuelva en forma de lista los valores de
# los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir
# cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    lista = list(kwargs.values())
    return lista

print(lista_atributos(x=2))

# Práctica sobre Argumentos Indefinidos (**kwargs) 3
# Crea una función llamada describir_persona, que tome como parámetros su nombre y
# luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:
#
# Características de {nombre}:
# {nombre_argumento}: {valor_argumento}
# {nombre_argumento}: {valor_argumento}
# etc...
# Por ejemplo:
#
# describir_persona("María", color_ojos="azules", color_pelo="rubio")
#
# Mostrará en pantalla:
#
# Características de María:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(nombre, **kwargs):
    print(f"características de {nombre}:")
    for i, v in kwargs.items():
        print(f"{i}: {v}")


describir_persona("Tomás", color_ojos="azules", color_pelo="rubio")