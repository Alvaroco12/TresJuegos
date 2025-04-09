from caballos import Caballo

# filepath: /Users/alvarocosta/Documents/programacion/TresJuegos/main.py

def main():
    # Crear una instancia de la clase Caballo
    caballo = Caballo()
    
    # Mostrar la posición inicial del caballo
    print(caballo)
    
    # Calcular movimientos posibles
    movimientos = caballo.calcularMovimientosPosibles()
    print("Movimientos posibles:", movimientos)
    
    # Mover el caballo si hay movimientos posibles
    if movimientos:
        caballo.moverCaballo(movimientos[0])  # Mover al primer movimiento posible
        print("Después de mover:")
        print(caballo)

if __name__ == "__main__":
    main()