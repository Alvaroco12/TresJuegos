import random

class Caballo:

    def __init__(self, tablero=None, posicion=None):
        self.tablero = tablero if tablero else self.crearTableroVacio()
        self.posicion = posicion if posicion else self.generarCaballo()
        self.movimientos_posibles = []
        self.contador_movimientos = 1
        self.casillas_visitadas = set()
        self.casillas_visitadas.add(self.posicion)
        self.tablero[self.posicion[0]][self.posicion[1]] = self.contador_movimientos

        # Ruta precalculada (basada en la imagen proporcionada)
        self.ruta_precalculada = [
            (0, 0), (2, 1), (4, 0), (6, 1), (7, 3), (5, 4), (3, 5), (1, 6),
            (0, 4), (2, 3), (4, 2), (6, 3), (7, 5), (5, 6), (3, 7), (1, 5),
            (0, 7), (2, 6), (4, 7), (6, 6), (7, 4), (5, 3), (3, 2), (1, 1),
            (0, 3), (2, 4), (4, 5), (6, 4), (7, 2), (5, 1), (3, 0), (1, 2),
            (0, 0), (2, 1), (4, 0), (6, 1), (7, 3), (5, 4), (3, 5), (1, 6),
            (0, 4), (2, 3), (4, 2), (6, 3), (7, 5), (5, 6), (3, 7), (1, 5),
            (0, 7), (2, 6), (4, 7), (6, 6), (7, 4), (5, 3), (3, 2), (1, 1),
            (0, 3), (2, 4), (4, 5), (6, 4), (7, 2), (5, 1), (3, 0), (1, 2)
        ]

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
        posibles = []

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in self.casillas_visitadas:
                posibles.append((nx, ny))

        return posibles

    def moverCaballo(self, nueva_posicion):
        # Mueve el caballo a la siguiente posición en la ruta precalculada
        if nueva_posicion:
            self.posicion = nueva_posicion
            self.contador_movimientos += 1
            self.casillas_visitadas.add(nueva_posicion)
            self.tablero[self.posicion[0]][self.posicion[1]] = self.contador_movimientos
        else:
            raise ValueError("Movimiento no válido")

    def resolverRecorrido(self):
        # Reiniciamos el tablero y comenzamos desde la posición inicial
        self.tablero = self.crearTableroVacio()
        self.casillas_visitadas = set()
        self.casillas_visitadas.add(self.posicion)
        self.tablero[self.posicion[0]][self.posicion[1]] = 1
        self.contador_movimientos = 1

        if self._resolverRecorridoBacktracking(self.posicion[0], self.posicion[1], 1):
            return True
        else:
            return False

    def _resolverRecorridoBacktracking(self, x, y, movimiento_actual):
        if movimiento_actual == 64:  # Si se han visitado todas las casillas
            return True

        movimientos = self.calcularMovimientosPosibles()
        movimientos.sort(key=lambda pos: len(self.calcularMovimientosDesde(pos)))  # Ordenar por Warnsdorff

        for nx, ny in movimientos:
            self.tablero[nx][ny] = movimiento_actual + 1
            self.casillas_visitadas.add((nx, ny))
            if self._resolverRecorridoBacktracking(nx, ny, movimiento_actual + 1):
                return True
            # Backtracking
            self.tablero[nx][ny] = 0
            self.casillas_visitadas.remove((nx, ny))

        return False

    def calcularMovimientosDesde(self, posicion):
        # Calcula los movimientos posibles desde una posición específica
        movimientos = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        x, y = posicion
        posibles = []

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in self.casillas_visitadas:
                posibles.append((nx, ny))

        return posibles

    def obtenerSiguienteMovimiento(self):
        # Encuentra el siguiente movimiento en la ruta precalculada
        if self.contador_movimientos <= len(self.ruta_precalculada):
            siguiente_movimiento = self.ruta_precalculada[self.contador_movimientos - 1]
            print(f"Movimiento {self.contador_movimientos}: {siguiente_movimiento}")
            return siguiente_movimiento
        print("No hay más movimientos en la ruta precalculada.")
        return None
