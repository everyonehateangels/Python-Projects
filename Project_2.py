
# Projecto 2 - Mi versión
# pregunta_1 = input("¿Como te llamas?: ")
# pregunta_2 = float(input("Monto exacto de las ventas :"))
# comision = pregunta_2 * 13/100


#print(f"Okay {pregunta_1}. Este mes ganaste {comision}$")

# Corrección
nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes"))
comision = round(ventas * 13 / 100,2)

print(f"Hola {nombre}, tus comisiones de este mes son {comision}$")