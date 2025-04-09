import random

class Caballo:

    def __init__(self, tablero=None, posicion=None):
        self.tablero = tablero if tablero else self.crearTableroVacio()
        self.posicion = posicion if posicion else self.generarCaballo()
        self.movimientos_posibles = []
        self.contador_movimientos = 0
        self.casillas_visitadas = set()
        self.casillas_visitadas.add(self.posicion)

    def __str__(self):
        return f"Caballo en la posición: {self.posicion}, Movimientos realizados: {self.contador_movimientos}, Casillas visitadas: {len(self.casillas_visitadas)}"
    
    def crearTableroVacio(self):
        return [[0 for _ in range(8)] for _ in range(8)]
    
    def generarCaballo(self):
        # Genera una posición aleatoria para el caballo
        return (random.randint(0, 7), random.randint(0, 7))

    def calcularMovimientosPosibles(self):
        # Calcula los movimientos posibles del caballo
        movimientos = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        x, y = self.posicion
        self.movimientos_posibles = [
            (x + dx, y + dy) for dx, dy in movimientos
            if 0 <= x + dx < 8 and 0 <= y + dy < 8 and (x + dx, y + dy) not in self.casillas_visitadas
        ]
        return self.movimientos_posibles

    def moverCaballo(self, nueva_posicion):
        # Mueve el caballo a una nueva posición y actualiza el contador
        if nueva_posicion in self.movimientos_posibles:
            self.posicion = nueva_posicion
            self.contador_movimientos += 1
            self.casillas_visitadas.add(nueva_posicion)
        else:
            raise ValueError("Movimiento no válido")