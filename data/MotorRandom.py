import random
from data.Minijuegis import minijuegoA
from data.Minijuegis import minijuegoB
from data.Minijuegis import minijuegoC
from data.Minijuegis import minijuegoD
from data.AhorradorDePaginas import cargarVerbos
from data.AhorradorDePaginas import getA
from data.AhorradorDePaginas import getB
from data.AhorradorDePaginas import getC
from data.AhorradorDePaginas import getD

# Datos
cargarVerbos(1)
columnaA = getA()
columnaB = getB()
columnaC = getC()
columnaD = getD()

juegos = [
    (minijuegoA, columnaA),
    (minijuegoB, columnaB),
    (minijuegoC, columnaC),
    (minijuegoD, columnaD)
]

puntos = 0

# Principal
def jugarRandom(i):

    juego, columna = random.choice(juegos)

    respuesta = juego(columnaA, columnaB, columnaC, columnaD, i)

    resultadoEspecifico(columna, respuesta, i)

# Resultados
def resultado(maxPuntos):
    global puntos
    print("Resultado final:", puntos, "/", maxPuntos, "\n")
    puntos = 0

def resultadoEspecifico(columna, respuesta, i):

    global puntos

    if respuesta.lower() == columna[i].lower():
        print("✔ Correcto\n")
        puntos += 1
    if respuesta.lower() == "x":
        volver_menu()
    else:
        print("✘ Incorrecto. La respuesta era:", columna[i], "\n")
        
def volver_menu():
    from data.Proceso import iniciarMinijuego
    iniciarMinijuego()