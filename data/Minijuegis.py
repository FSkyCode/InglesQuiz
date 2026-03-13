# Minijuegos XD
def minijuegoA(columnaA, columnaB, columnaC, columnaD, i):
    print("| _____ |", columnaB[i], "|", columnaC[i], "|", columnaD[i], "|")
    respuesta = input("Respuesta: ")
    return respuesta

def minijuegoB(columnaA, columnaB, columnaC, columnaD, i):
    print("|", columnaA[i], "| _____ |", columnaC[i], "|", columnaD[i], "|")
    respuesta = input("Respuesta: ")
    return respuesta


def minijuegoC(columnaA, columnaB, columnaC, columnaD, i):
    print("|", columnaA[i], "|", columnaB[i], "| _____ |", columnaD[i], "|")
    respuesta = input("Respuesta: ")
    return respuesta


def minijuegoD(columnaA, columnaB, columnaC, columnaD, i):
    print("|", columnaA[i], "|", columnaB[i], "|", columnaC[i], "| _____ |")
    respuesta = input("Respuesta: ")
    return respuesta