

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super(Cliente, self).__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}. \nNumero de cuenta: {self.numero_cuenta}.\nTu balance act" \
               f"ual es de: {self.balance}"


    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print(f"Has añadido {monto_deposito} satisfactoriamente, tu balance ahora es de {self.balance}.")




    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print(f"Has retirado {monto_retiro}, satisfactoriamente.Tu balance actual es de {self.balance}")
        else:
            print("El monto utilizado no existe.")


def crear_cliente():
    nombre_cliente = input("Introduce tu nombre: ")
    apellido_cliente = input("Introduce tu apellido: ")
    numero_de_cuenta = input("Introduce tu numero de cuenta: ")
    cliente = Cliente(nombre_cliente, apellido_cliente, numero_de_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    menu = 0
    while menu != "S":
        print("Elige una de las siguientes opciones:\n"
              "[D] Depositar"
              "[R] Retirar"
              "[S] Salir del Programa")
        menu = input().upper()
        if menu == "D":
            monto_depositar = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_depositar)
        elif menu == "R":
            monto_sacar = int(input("Monto a retirar"))
            mi_cliente.retirar(monto_sacar)
        print(mi_cliente)
    print("Gracias por la confianza")


inicio()