from pathlib import Path

folder = Path("C:\Users\angel\PycharmProjects\PrimerPrograma\Calculator\prueba1.txt")

if not folder.exists():
    print("No existe el archivo, estamos?")
else:
    print("Em si, vale, existe.")