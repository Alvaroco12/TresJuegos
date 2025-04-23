# main sencillo

def main():
    print("El numero de reinas en el tablero sera el amaño del mismo")
    tam = input("De que tamaño quieres el tablero? ")
    while int(tam) > 10: tam = input("Elije otro tamaño, ese es muy grande (max -> 10) ")
    print("El tablero es de: " + tam)

    tablero = [[0 for _ in int(range(tam))] for _ in int(range(tam))]
    for f in tablero:
        print(f)



def creartablerovacio(x:int):
    tablero = [[0 for _ in range(x)] for _ in range(x)]
    for f in tablero:
        print(f)




if __name__ == "__main__":
    main()
