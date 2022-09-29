from pathlib import Path

base = Path.home()
guide = Path(Path.home(), "Europa")


for txt in Path(guide).glob("**/*.txt"):
    print(txt)

print(guide)


guide_new = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")

in_europe = guide_new.relative_to(Path("Europa"))
in_spain = guide_new.relative_to(Path("Europa", "España"))

print(in_europe)
print(in_spain)


# Práctica Path 1
# Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.
#
# Recuerda importar Path del módulo pathlib, y utilizar el método home()


ruta_base = Path.home()

# Practica Path 2
# Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py"
# a partir de la siguiente estructura de carpetas:
# . Curso Python
# . Día 6
# . practicas_path.py
# Almacena el directorio obtenido en la variable ruta. No olvides importar Path.

ruta = Path("Curso Python", "Día 6", "practicas_path.py")

print(ruta)

'''Práctica Path 3
Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente
 estructura de carpetas:
 - home
 - Curso python
 - Dia 6
 - practicas_path.py'''

ruta = Path(Path.home(), "Curso Python", "Día 6", "practicas_path.py")


print(ruta)