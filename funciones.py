import random
import variables as va
import variables as fu

# Función para crear el tablero de 10x10
def crear_tablero():
    tablero = []
    for _ in range(10):
        fila = ["-"] * 10  
        tablero.append(fila)
    return tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función para colocar los barcos en el tablero
def colocar_barcos(tablero, barcos):
    for barco in barcos:
        for coordenada in barco:
            fila, columna = coordenada
            tablero[fila][columna] = "O"  

# Función para realizar un disparo
def disparar(tablero, fila, columna):
    if tablero[fila][columna] == "O":
        tablero[fila][columna] = "X"  
        return "Tocado"
    elif tablero[fila][columna] == "X":
        return "Repetido"
    else:
        tablero[fila][columna] = "-"  
        return "Agua"

# Función principal del juego
def jugar_hundir_la_flota():
    tablero_jugador = crear_tablero()

    barcos_jugador = [
        [(0,1), (1,1)],
        [(1,3), (1,4), (1,5), (1,6)],
        [(7,9)],
        [(8,1), (8,2), (8,3)],
        [(5,5), (5,6)],
        [(4,3),(4,4)],
        [(3,1), (3,2),(3,3)],
        [(9,8)],
        [(2,7)],
        [(6,7)]
    ]

    colocar_barcos(tablero_jugador, barcos_jugador)

    jugador_turno = True
    disparos_jugador = 0
    disparos_maquina = 0

    while True:
        if jugador_turno:
            print("\nTablero del Jugador:")
            imprimir_tablero(tablero_jugador)
            
            coord_x = int(input('Introduzca coordenada x:'))
            coord_y = int(input('Introduzca coordenada y:'))

            resultado_jugador = disparar(tablero_jugador, coord_x, coord_y)
            if resultado_jugador == "Tocado":
                print("¡Has acertado!")

                for barco in barcos_jugador:
                    if all(tablero_jugador[fila][columna] == "X" for fila, columna in barco):
                        print(f"\n¡Has hundido un barco de la máquina!")
                        barcos_jugador.remove(barco)
                        print("¡Barco hundido!")

            elif resultado_jugador == "Agua":
                print("Has fallado!")

            elif resultado_jugador == "Repetido":
                print("¡Ya habías disparado en esa coordenada!")

            disparos_jugador += 1
        else:
           
            while True:
                fila_maquina = random.randint(0, 9)
                columna_maquina = random.randint(0, 9)
                resultado_maquina = disparar(tablero_jugador, fila_maquina, columna_maquina)
                if resultado_maquina == "Agua":
                    break

            if resultado_maquina == "Tocado":
                print("¡La máquina acertó!")

                for barco in barcos_jugador:
                    if all(tablero_jugador[fila][columna] == "X" for fila, columna in barco):
                        print(f"\n¡La máquina ha hundido uno de tus barcos!")
                        barcos_jugador.remove(barco)
                        print("¡Tu barco ha sido hundido!")

            elif resultado_maquina == "Agua":
                print("La máquina ha fallado!")

            disparos_maquina += 1

        if not barcos_jugador:
            print("\n¡La máquina ha hundido todos tus barcos. ¡Perdiste!")
            break

        if disparos_jugador >= 20:
            print("\n¡Te has quedado sin disparos! ¡El juego ha terminado sin ganador!")
            break

        if jugador_turno:
            jugador_turno = False
        else:
            jugador_turno = True

if __name__ == "__main__":
    print("¡Bienvenido a Hundir la Flota!")
    jugar_hundir_la_flota()
