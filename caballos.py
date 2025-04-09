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
                # Cuenta los movimientos futuros posibles desde esta casilla
                count = 0
                for ddx, ddy in movimientos:
                    nnx, nny = nx + ddx, ny + ddy
                    if 0 <= nnx < 8 and 0 <= nny < 8 and (nnx, nny) not in self.casillas_visitadas:
                        count += 1
                posibles.append(((nx, ny), count))

        # Ordenar los movimientos por la cantidad de opciones futuras (Warnsdorff)
        posibles.sort(key=lambda x: x[1])
        self.movimientos_posibles = [pos[0] for pos in posibles]
        return self.movimientos_posibles

    def moverCaballo(self, nueva_posicion):
        # Mueve el caballo a una nueva posición y actualiza el contador
        if nueva_posicion in self.movimientos_posibles:
            self.posicion = nueva_posicion
            self.contador_movimientos += 1
            self.casillas_visitadas.add(nueva_posicion)
            self.tablero[self.posicion[0]][self.posicion[1]] = self.contador_movimientos
        else:
            raise ValueError("Movimiento no válido")

    def resolverRecorrido(self):
        # Reiniciamos el tablero y comenzamos desde la posición inicial
        self.tablero = self.crearTableroVacio()
        x, y = self.posicion
        self.tablero[x][y] = 1
        if self._resolverRecorridoBacktracking(x, y, 1):
            return True
        else:
            print("No se encontró una solución")
            return False

    def _resolverRecorridoBacktracking(self, x, y, movimiento_actual):
        if movimiento_actual == 64:
            return True

        movimientos = self.calcularMovimientosPosibles()
        for nx, ny in movimientos:
            self.tablero[nx][ny] = movimiento_actual + 1
            if self._resolverRecorridoBacktracking(nx, ny, movimiento_actual + 1):
                return True
            self.tablero[nx][ny] = 0  # backtrack

        return False
