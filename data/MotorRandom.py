import random
from Minijuegis import minijuegoA
from Minijuegis import minijuegoB
from Minijuegis import minijuegoC
from Minijuegis import minijuegoD
from AhorradorDePaginas import cargarVerbos
from AhorradorDePaginas import getA
from AhorradorDePaginas import getB
from AhorradorDePaginas import getC
from AhorradorDePaginas import getD

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
    else:
        print("✘ Incorrecto. La respuesta era:", columna[i], "\n")