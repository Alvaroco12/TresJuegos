from caballos import Caballo

def imprimir_tablero(tablero):
    print("\nTablero final:\n")
    for fila in tablero:
        print(" ".join(f"{celda:2}" for celda in fila))

def main():
    # Crear una instancia de la clase Caballo
    caballo = Caballo()
    
    # Mostrar la posición inicial del caballo
    print("Posición inicial del caballo:")
    print(caballo)
    
    # Intentar resolver el recorrido completo del caballo
    print("\nResolviendo el recorrido del caballo...")
    if caballo.resolverRecorrido():
        print("\n¡Recorrido completado con éxito!")
    else:
        print("\nNo se pudo completar el recorrido.")
    
    imprimir_tablero(caballo.tablero)


if __name__ == "__main__":
    main()