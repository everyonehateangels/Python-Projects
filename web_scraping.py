import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")


sopa = bs4.BeautifulSoup(resultado.text, "lxml")



imagenes = sopa.select("img")[0]["src"]

print(imagenes)


imagenes_escuela = requests.get(imagenes)


f = open("mi_imagen.jpg", "wb")

f.write(imagenes_escuela.content)

f.close()


