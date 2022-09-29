import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro microfono y devolver el audio como texto

def transformar_audio_en_texto():

    # almacenar el recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")


        # guardar lo que escuche como audio
        audio = r.listen(origen)

    try:
        # buscar en google
        pedido = r.recognize_google(audio, language="es-es")

        # prueba que pudo ingresar
        print("Dijiste: " + pedido)

        # devolver pedido
        return pedido

    # En caso de error o que no comprenda el audio
    except sr.UnknownValueError:

        # Prueba de que no comprendio el audio
        print("Ups, no entiendo lo que has querido decir")

        # devolver error
        return "sigo esperando"

    # En caso de no poder resolver el pedido
    except sr.RequestError:

        # Prueba de que no comprendio el audio
        print("Ups, no hay sevicio")

        # devolver error
        return "sigo esperando"

    # Error inesperado
    except:
        # Prueba de que no comprendio el audio
        print("Ups, algo ha salido mal")

        # devolver error
        return "sigo esperando"



# Funcion para que el asistente pueda ser escuchado
id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)


    # Crear una variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miercoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}


    # decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")


# Informar que hora es

def pedir_hora():

    # crear una variable con datos de la hora actual
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora)


# funcion saludo inicial

def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    # decir el saludo
    hablar(f"{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar")




# Funcion central del asistente

def central_pedidos():

    # activar saludo incial
    saludo_inicial()

    # variable de corte
    comenzar = True


    # loop central

    while comenzar:
        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo YouTube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "abir el navegador" in pedido:
            hablar("Claro, estoy en ello. ")
            webbrowser.open("https://www.google.es/")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente: ")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("¡De acuerdo!, estoy en ello.")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precios de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "APPL",
                       "amazon": "AMZN",
                       "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon, no la he encontrado.")
                continue
        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


central_pedidos()
