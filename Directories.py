import os
from pathlib import Path
ruta = os.getcwd()



folder = Path('/Users/Win10/Desktop/Alternativo')

file = folder / 'otro_archivo.txt'


my_file = open(file)
print(my_file.read())