import pygame
from caballos import Caballo

class Aplicacion:
    def __init__(self):
        pygame.init()
        self.ancho_ventana = 400
        self.alto_ventana = 400
        self.tamano_casilla = 50
        self.ventana = pygame.display.set_mode((self.ancho_ventana, self.alto_ventana))
        pygame.display.set_caption("Recorrido del Caballo")
        self.reloj = pygame.time.Clock()

        # Crear la instancia del caballo
        self.caballo = Caballo()

        # Colores
        self.color_blanco = (255, 255, 255)
        self.color_negro = (0, 0, 0)
        self.color_linea = (0, 255, 0)  # Verde para la línea

        # Cargar la imagen del caballo
        self.imagen_caballo = pygame.image.load("caballo.png")
        self.imagen_caballo = pygame.transform.scale(self.imagen_caballo, (self.tamano_casilla, self.tamano_casilla))

        # Historial de posiciones visitadas
        self.posiciones_visitadas = [self.caballo.posicion]

        self.ejecutando = True

    def dibujar_tablero(self):
        """Dibuja el tablero con los movimientos del caballo"""
        self.ventana.fill(self.color_blanco)  # Limpiar la ventana
        for i in range(8):
            for j in range(8):
                x0, y0 = j * self.tamano_casilla, i * self.tamano_casilla
                color = self.color_blanco if (i + j) % 2 == 0 else self.color_negro
                pygame.draw.rect(self.ventana, color, (x0, y0, self.tamano_casilla, self.tamano_casilla))

        # Dibujar la línea que conecta las casillas visitadas
        if len(self.posiciones_visitadas) > 1:
            puntos = [
                (y * self.tamano_casilla + self.tamano_casilla // 2,
                 x * self.tamano_casilla + self.tamano_casilla // 2)
                for x, y in self.posiciones_visitadas
            ]
            pygame.draw.lines(self.ventana, self.color_linea, False, puntos, 3)

        # Dibujar la silueta del caballo en la posición actual
        x_caballo, y_caballo = self.caballo.posicion
        x0 = y_caballo * self.tamano_casilla
        y0 = x_caballo * self.tamano_casilla
        self.ventana.blit(self.imagen_caballo, (x0, y0))

    def iniciar_recorrido(self):
        """Inicia el recorrido del caballo"""
        while self.ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.ejecutando = False

            # Obtener el siguiente movimiento en la ruta precalculada
            nueva_posicion = self.caballo.obtenerSiguienteMovimiento()
            if nueva_posicion:
                self.caballo.moverCaballo(nueva_posicion)
                self.posiciones_visitadas.append(nueva_posicion)
                self.dibujar_tablero()
            else:
                print("Recorrido completo.")
                self.ejecutando = False

            pygame.display.flip()  # Actualizar la pantalla
            self.reloj.tick(10)  # Aumentar la velocidad (10 FPS)

        pygame.quit()

def main():
    app = Aplicacion()
    app.dibujar_tablero()
    pygame.display.flip()  # Mostrar el tablero inicial
    app.iniciar_recorrido()

if __name__ == "__main__":
    main()