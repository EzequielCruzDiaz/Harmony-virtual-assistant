Descripción del Proyecto
Bienvenido al repositorio de Harmony, tu asistente virtual desarrollado en Python. Harmony es más que un simple programa; es tu compañero virtual diseñado para hacerte la vida más fácil y divertida. Este asistente multifuncional puede realizar diversas tareas, desde proporcionar información sobre el clima y noticias hasta abrir aplicaciones y enviar mensajes de WhatsApp.

Funcionalidades Destacadas

Reconocimiento de Voz: Harmony utiliza la biblioteca SpeechRecognition para entender y procesar comandos de voz en español.
Interacción con Aplicaciones: Puede abrir aplicaciones en tu sistema, proporcionándote un acceso rápido a tus herramientas favoritas.
Consulta de Información: Harmony puede buscar en Wikipedia, proporcionar la fecha y hora actual, e incluso obtener datos sobre acciones en tiempo real.
Entretenimiento: ¿Necesitas una pausa? Harmony puede reproducir chistes divertidos gracias a la integración con PyJokes.
Código Destacado
python
# Inicialización de Harmony
def pedir_cosas():
    saludo_inicial()

    comenzar = True
    while comenzar:
        pedido = transformar_audio_texto().lower()

        # ... (Funciones de procesamiento de comandos)
pedir_cosas()

Requisitos y Dependencias
Para ejecutar Harmony, asegúrate de tener instaladas las siguientes bibliotecas:

pyjokes
keyboard
pyttsx3
pywhatkit
wikipedia-api
speech_recognition
yfinance
subprocess
pyautogui
pygame
requests

Cómo Usar Harmony
Clona este repositorio en tu máquina local.
Asegúrate de tener todas las dependencias instaladas.
Ejecuta el script principal (harmony.py).
¡Disfruta de la interacción con Harmony!
Este proyecto es una creación de Ezequiel Junior Cruz Diaz. Si tienes sugerencias, problemas o contribuciones, no dudes en ponerte en contacto.
