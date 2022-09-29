import os
from pathlib import Path
from os import system

input()

path = Path(r"C:\Users\angel\Downloads\Recetas\Recetas")

categories = os.listdir(r"\Users\angel\Downloads\Recetas\Recetas")

lista = list(path.glob("**/*.txt"))

print(len(lista))