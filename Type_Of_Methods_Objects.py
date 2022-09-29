class Pajaro:

    alas = True
# This Atribute require an instance.
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")
# Class methods don't need an instance to be executed.
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)
# Static methods can access class methods and instance atributes.
    @staticmethod
    def mirar():
        print("El pajaro mira")


Pajaro.poner_huevos(3)


# Práctica Tipos de Métodos 1
# Crea un método estático respirar() para la clase Mascota.
# Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()

# Práctica Tipos de Métodos 2
# Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, es
# tableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

# Práctica Tipos de Métodos 3
# Crea un método de instancia lanzar_flecha() que reste en -1
# la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número,
# llamado cantidad_flechas.

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1