import speech_recognition as sr
import pyttsx3
import os
import time
from datetime import datetime

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

def hablar(texto):
    """Convierte texto a voz."""
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    """Captura y reconoce la voz del usuario."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5)
            comando = recognizer.recognize_google(audio, language="es-ES")
            comando = comando.lower().strip()
            print(f"Tú dijiste: {comando}")
            return comando
        except sr.WaitTimeoutError:
            print("No detecté ninguna palabra.")
            return None
        except sr.UnknownValueError:
            print("No entendí lo que dijiste.")
            return None
        except sr.RequestError:
            print("No se pudo conectar al servicio de reconocimiento.")
            return None

def ejecutar_comando(comando):
    """Procesa el comando del usuario."""
    if "hola" in comando:
        hablar("Hola, ¿en qué puedo ayudarte?")
    elif "hora" in comando:
        hora_actual = datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora_actual}")
    elif "navegador" in comando:
        hablar("Enseguida.")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe") 
    elif "salir" in comando:
        hablar("Adiós, hasta luego.")
        exit()
    else:
        hablar("No entiendo ese comando.")

# Ciclo principal del asistente
if __name__ == "__main__":
    hablar("Hola, ¿En qué puedo ayudarte?")
    tiempo_inicio = time.time()
    tiempo_inactividad = 10  # Tiempo máximo de inactividad en segundos
    
    while True:
        comando = escuchar()
        
        if comando:
            ejecutar_comando(comando)
            tiempo_inicio = time.time()  # Reinicia el temporizador si se detecta un comando
        else:
            tiempo_actual = time.time()
            if tiempo_actual - tiempo_inicio > tiempo_inactividad:  # Si se supera el tiempo de inactividad
                hablar("Cerrándo...") 
                print("cerrándo...")
                break
