import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import subprocess
from pathlib import Path

voz = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0"


# escuchar nuestro micro y devolver el audio como texto
def transformar_audio_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el micro
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # imformar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo escuchado como auido
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-mx")

            # prueba de que puso ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Uis... No entendi")
            hablar("Disculpa, no te he entendido")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Uis... No hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Uis... Algo salio mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", voz)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.datetime.today()
    print(dia)

    # crear una variable para el dia de semana
    dia_semana = dia.weekday()
    mes_actual = dia.month
    print(dia_semana)

    # diccionario con nombres de dias y meses
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    meses = {1: "Enero",
             2: "Febrero",
             3: "Marzo",
             4: "Abril",
             5: "Mayo",
             6: "Junio",
             7: "Julio",
             8: "Agosto",
             9: "Septiembre",
             10: "Octubre",
             11: "Noviembre",
             12: "Diciembre"}

    # decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]} {dia.day} de {meses[mes_actual]}")


# informar que hora es
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f" En este momento son las {hora.hour} horas con {hora.minute} minutos"
    print(hora)

    # decir hora
    hablar(hora)


# funcion saludo
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 12:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    # decir el saludo
    hablar(f"{momento}, dime en que te puedo ayudar")


# funcion abrir apps
def pedir_aplicacion():

    lista_rutas = []
    lista_nombres = []
    ruta = Path("C:/ProgramData")

    for app in ruta.glob("**/*.lnk"):
        lista_rutas.append(app)
        lista_nombres.append(app.stem.lower())

    return lista_nombres, lista_rutas


def abrir_aplicacion(pedido, nombres, rutas):

    correcto = False
    indice_ruta_seleccionada = nombres.index(pedido)

    while not correcto:

        if pedido in nombres:

            aplicacion = rutas[indice_ruta_seleccionada]
            subprocess.Popen(fr'{aplicacion}', shell=True)
            correcto = True

        else:
            hablar('No he encontrado esa aplicación. Inténtalo otra vez')


def abrir_navegador(pedido):

    subprocess.Popen(fr'start chrome {pedido}', shell=True)


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_texto().lower()

        if "abre el navegador" in pedido:
            hablar("Qué página deseas abrir?")
            nuevo_pedido = transformar_audio_texto()
            hablar("Estoy en eso...")
            abrir_navegador(nuevo_pedido)
            continue

        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue

        elif "qué hora es" in pedido:
            pedir_hora()
            continue

        elif "busca en wikipedia" in pedido:
            hablar("Buscando en wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice los siguiente:")
            hablar(resultado)
            continue

        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif "reproduce" in pedido:
            pywhatkit.playonyt(pedido)
            continue

        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue

        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "APPL",
                       "amazon": "AMZN",
                       "google": "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                continue

            except:
                hablar("Perdón pero no la he encontrado")

        elif "eso es todo" in pedido:
            hablar("Claro, ya sabes donde encontrarme")
            break

        elif "mensaje a ezequiel" in pedido:
            hablar("Enviando el mensaje")
            mensaje = pedido.split("diga")[-1].strip()
            pywhatkit.sendwhatmsg_instantly("+18294014743", mensaje)
            time.sleep(5)
            pyautogui.press("enter")
            continue

        elif "abre una aplicación" in pedido:
            nombres, rutas = pedir_aplicacion()
            hablar("Muy bien, qué aplicación deseas abrir?")
            nuevo_pedido = transformar_audio_texto().lower()
            hablar(f"Abriendo {nuevo_pedido}")
            abrir_aplicacion(nuevo_pedido, nombres, rutas)
            continue


pedir_cosas()
