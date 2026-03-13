from data.MotorRandom import jugarRandom
from data.MotorRandom import resultado
from data.MotorRandom import volver_menu
import os

# Datos
facil = 2
medio = 5
total = 49
MODO = "Desactivado"
primeraVez = True

# Funciones
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Inicio
def iniciarMinijuego():
    global primeraVez
    
    limpiarPantalla()
    if primeraVez:
        print("\nPor: Juan Felipe Sierra Castillo")
        print("\Escribe 'x'para salir del Quiz en cualquier momento o ir al menu.\n")
        print("\nQUIZ DE VERBOS EN INGLES\n")
        print("Pon 1 para el modo facil")
        print("Pon 2 para el modo medio")
        print("Pon 3 para el modo dificil")
        print("Pon 4 para resolver todo")
        print("Pon 5 para ver ajustes")
        primeraVez = False
    else:
        print("\nPor: Juan Felipe Sierra Castillo")
        print("\nQUIZ DE VERBOS EN INGLES\n")
        print("Pon 1 para el modo facil")
        print("Pon 2 para el modo medio")
        print("Pon 3 para el modo dificil (en progreso)")
        print("Pon 4 para resolver todo")
        print("Pon 5 para ver ajustes")
    start = input("> ")

    if start == "1":
        modoFacil()
    elif start == "2":
        modoMedio()
    elif start == "2":
        modoMedio()
    elif start == "4":
        modoTotal()
    elif start == "5":
        modoAjustes()
    elif start == "x":
        volver_menu()
    if start not in ["1","2","3","4","5","x"]:
        iniciarMinijuego()


def repetirMinijuego(minijuego):
    print("\n¿Repetir Minijuego?\n")
    print("Pon 1 para Si")
    print("Pon 2 para No\n")
    respuesta = input("> ")
    if respuesta == "1":
        limpiarPantalla()
        if minijuego == "facil":
            modoFacil()
        if minijuego == "Total":
            modoTotal()
    elif respuesta == "2":
        limpiarPantalla()
        iniciarMinijuego()


# Modos
def modoFacil():
    print("\nCompleta de acuerdo a las columnas:\n")
    print("| INFINITIVO | PASADO SIMPLE | PARTICIPIO PASADO | ESPAÑOL |\n")
    for i in range(facil):
        jugar = jugarRandom(i)

    resultado(facil)
    repetirMinijuego("facil")

def modoMedio():
    print("\nCompleta de acuerdo a las columnas:\n")
    print("| INFINITIVO | PASADO SIMPLE | PARTICIPIO PASADO | ESPAÑOL |\n")
    for i in range(medio):
        jugar = jugarRandom(i)

    resultado(medio)
    repetirMinijuego("medio")

def modoTotal():
    print("\nCompleta de acuerdo a las columnas:\n")
    print("| INFINITIVO | PASADO SIMPLE | PARTICIPIO PASADO | ESPAÑOL |\n")
    for i in range(total):
        jugar = jugarRandom(i)

    resultado(total)
    repetirMinijuego("total")

def modoAjustes():
    limpiarPantalla()
    print("\n AJUSTES \n")
    print(f"1. Modificar minijuegos\n2. Modificar pagina\n3. Ver los verbos (depende de la pagina actual)\n4. Activar sonidos {MODO}\n5. Ver creditos\n6. Retroceder")
    respuesta = input("> ")
    if respuesta == "1":
        modoAjustes()
        print("\nIncompleto\n")
    if respuesta == "2":
        print("Incompleto")
        modoAjustes()
    if respuesta == "3":
        print("Incompleto")
        modoAjustes()
    if respuesta == "4":
        print("Incompleto")
        modoAjustes()
    if respuesta == "5":
        print("Incompleto")
        modoAjustes()
    if respuesta == "6":
        iniciarMinijuego()
