import random

class caballo:

    def __init__(self, tablero, posicion):
        self.tablero = tablero
        self.posicion = posicion
        self.movimientos = []
        self.movimientos_posibles = []

    tablero = [[0 for _ in range(8)] for _ in range(8)]

    def colocar_caballo_aleatorio(self):
        fila = random.randint(0, 7)
        columna = random.randint(0, 7)
        self.posicion = (fila, columna)
        self.tablero[fila][columna] = 1

    colocar_caballo_aleatorio(self)

    print("El caballo está en la posición: ", caballo)
