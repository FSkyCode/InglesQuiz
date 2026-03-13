import os

columnaA = []
columnaB = []
columnaC = []
columnaD = []
numeroDeHoja = 1  # predeterminado

base = os.path.dirname(os.path.dirname(__file__))
ruta = os.path.join(base, "assets", f"verbos{numeroDeHoja}.txt")

def cargarVerbos(numeroDeHoja):
    with open(ruta, "r") as archivo:
        for linea in archivo:
            a, b, c, d = [x.strip() for x in linea.split(",")]
            columnaA.append(a)
            columnaB.append(b)
            columnaC.append(c)
            columnaD.append(d)

def getA():
    return columnaA
def getB():
    return columnaB
def getC():
    return columnaC
def getD():
    return columnaD

cargarVerbos(1)

print(columnaA)
print(columnaB)
print(columnaC)
print(columnaD)