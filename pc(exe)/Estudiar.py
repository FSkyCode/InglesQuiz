import os
import sys

# añadir la carpeta raíz del proyecto
base = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base)

from data.Proceso import iniciarMinijuego

def ruta_base():
    if hasattr(sys, "_MEIPASS"):
        return sys._MEIPASS
    return os.path.abspath(".")

# Inicio
iniciarMinijuego()
