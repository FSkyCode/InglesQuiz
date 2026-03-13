columnaA = []
columnaB = []
columnaC = []
columnaD = []

# Escoger cual hoja escanear
numeroDeHoja = 1  # predeterminado

def cargarVerbos(numeroDeHoja):
    with open(f"verbos{numeroDeHoja}.txt", "r") as archivo:
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