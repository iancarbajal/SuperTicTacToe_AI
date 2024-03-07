# -*- coding: utf-8 -*-
# ------------------------------------------------------
# Yohaly Lorena Mondragón Sandoval
# Aldo Soria Varela
# Ian Oswaldo Carbajal Aldana
# Jorge Antonio Joseph Fernández
# ------------------------------------------------------
from math import inf
from collections import Counter
import itertools


# Función para calcular el índice de un movimiento en la cadena de estado del juego
def indice(x, y):
    x -= 1
    y -= 1
    return ((x//3)*27) + ((x % 3)*3) + ((y//3)*9) + (y % 3)
#Los valores de posicion de la input (x,y en el rango de 1 a 9) se vuelven un entero (en range(80))
#para decidir que posicion de caislla es la jugada

# Función para calcular el tablero a la que pertenece un movimiento
def tablero(x, y):
    return indice(x, y) // 9
#El entero de indice es evauado para dar el tablero actual (entero en range(8))

# Función para calcular el siguiente tablero a jugar
def siguiente_tablero(i):
    return i % 9
#El entero de indice es evauado para dar el siguiente tablero a jugar (entero en range(8))

# Función para obtener los índices de los movimientos en un tablero específico
def indices_de_tablero(b):
    return list(range(b*9, b*9 + 9))
#Dado el tablero elegido acota los valores de casillas que pueden ser tomados

#Para estos fines el tablero se ve como
# 0 1 2
# 3 4 5
# 6 7 8
#Donde cada subtablero es igual pero sumado en 9*b donde b es el índice del subtablero
#Ese valor da el índice de la casilla en range(80)
#  0  1  2    9 10 11  18 19 20
#  3  4  5   12 13 14  21 22 23
#  6  7  8   15 16 17  24 25 26
#
# 27 28 29
# 30 31 32
# 33 34 35
#Y así continua

# Función para imprimir el tablero de juego
def imprimir_tablero(estado):
    print("   1 2 3   4 5 6   7 8 9")
    for fila in range(1, 10):
        row_str = [str(fila) + "|"]
        for columna in range(1, 10):
            row_str += [estado[indice(fila, columna)]]
            if (columna) % 3 == 0:
                row_str += ["|"]
        if (fila-1) % 3 == 0:
            print("-" * 26)
        print(" ".join(row_str))
    print("-" * 26)
#Esta funcion imprime la situación gráfica del juego
#para que el usuario la interprete
#Un ejemplo es:
#    1 2 3   4 5 6   7 8 9
#--------------------------
#1| . . . | . . . | . . . |
#2| . . . | . . . | . . . |
#3| . . . | . . . | . . . |
#--------------------------
#4| . . . | . . . | . . . |
#5| . . . | . . . | . . . |
#6| . . . | . . . | . . . |
#--------------------------
#7| . . . | . . . | . . . |
#8| . . . | . . . | . . . |
#9| . . . | . . . | . . . |
#--------------------------
    
# Función para agregar una pieza al estado del juego
def agregar_pieza(estado, movimiento, jugador):
    if not isinstance(movimiento, int):
        movimiento = indice(movimiento[0], movimiento[1])
    return estado[: movimiento] + jugador + estado[movimiento+1:]
#El estado es una string que contiene todo el tablero (81 char), el movimiento es la posicion como un par ordenado (ver indice)
#Y jugador es "X" o "O" según quien realiza la jugada. Esta funcion actualiza la string del tablero 

# Función para actualizar el estado de los tableros ganados
def actualizar_tablero_ganado(estado):
    temp_tablero_ganado = ["."] * 9
    for b in range(9):
        idxs_tablero = indices_de_tablero(b)
        tablero_str = estado[idxs_tablero[0]: idxs_tablero[-1]+1]
        temp_tablero_ganado[b] = verificar_tablero_pequeno(tablero_str)
    return temp_tablero_ganado
#Esta funcion evalua que subtableros lleva ganados cada jugador (a partir del estado) y lo devuelve como str

# Función para verificar si un tablero pequeño ha sido ganado por un jugador
def verificar_tablero_pequeno(tablero_str):
    global objetivos_posibles
    for idxs in objetivos_posibles:
        (x, y, z) = idxs
        if (tablero_str[x] == tablero_str[y] == tablero_str[z]) and tablero_str[x] != ".":
            return tablero_str[x]
    return "."
#Esta funcion hace la evaluacion de cada subtablero en la funcion anterios, y da el caracter del jugador
#que haya ganado el subtablero si el caso es pertinente, si no regresa el . que significa vacío

# Función para obtener los movimientos posibles en el próximo tablero a jugar
def movimientos_posibles(ultimo_movimiento):
    global tablero_ganado
    if not isinstance(ultimo_movimiento, int):
        ultimo_movimiento = indice(ultimo_movimiento[0], ultimo_movimiento[1])
    tablero_a_jugar = siguiente_tablero(ultimo_movimiento)
    idxs = indices_de_tablero(tablero_a_jugar)
    if tablero_ganado[tablero_a_jugar] != ".":
        pi_2d = [indices_de_tablero(b) for b in range(9) if tablero_ganado[b] == "."]
        indices_posibles = list(itertools.chain.from_iterable(pi_2d))
    else:
        indices_posibles = idxs
    return indices_posibles
#Condiciona la lista de jugadas posibles (como índices) a partir de siguiente tablero,
#así acotando a los espacios vacíos de ese subtablero o a todos los vacíos
#si el subtablero ya está ganado

# Función para generar los sucesores de un estado dado
def sucesores(estado, jugador, ultimo_movimiento):
    succ = []
    indices_movimientos = []
    indices_posibles = movimientos_posibles(ultimo_movimiento)
    for idx in indices_posibles:
        if estado[idx] == ".":
            indices_movimientos.append(idx)
            succ.append(agregar_pieza(estado, idx, jugador))
    return zip(succ, indices_movimientos)
#Esta funcion permite construir las condiciones de un movimiento porsterior
#como un conjunto de tuplas que estan dadas por el estado alcanzado y el índice del caso

# Función para imprimir los sucesores de un estado dado
def imprimir_sucesores(estado, jugador, ultimo_movimiento):
    for st in sucesores(estado, jugador, ultimo_movimiento):
        imprimir_tablero(st[0])
#Imprime las str de estados futuros

# Función para obtener el jugador opuesto
def oponente(jugador):
    return "O" if jugador == "X" else "X"
#Cambia de jugador por su caracter

# Función para evaluar un tablero pequeño del juego
def evaluar_tablero_pequeno(tablero_str, jugador):
    global objetivos_posibles
    puntaje = 0
    tres = Counter(jugador * 3)
    dos = Counter(jugador * 2 + ".")
    uno = Counter(jugador * 1 + "." * 2)
    tres_oponente = Counter(oponente(jugador) * 3)
    dos_oponente = Counter(oponente(jugador) * 2 + ".")
    uno_oponente = Counter(oponente(jugador) * 1 + "." * 2)

    for idxs in objetivos_posibles:
        (x, y, z) = idxs
        actual = Counter([tablero_str[x], tablero_str[y], tablero_str[z]])

        if actual == tres:
            puntaje += 245
        elif actual == dos:
            puntaje += 45
        elif actual == uno:
            puntaje += 1
        elif actual == tres_oponente:
            puntaje -= 245
            return puntaje
        elif actual == dos_oponente:
            puntaje -= 45
        elif actual == uno_oponente:
            puntaje -= 1

    return puntaje
#Dado el subtablero que se está jugando se puntua según que tan avanzadas
#estan las condiciones de victoria de cada jugador otorgando un entero
#para hacer la comparacion usa el jugador actual

# Función para evaluar el estado completo del juego
def evaluar(estado, ultimo_movimiento, jugador):
    global tablero_ganado
    puntaje = 0
    puntaje += evaluar_tablero_pequeno(tablero_ganado, jugador) * 200
    for b in range(9):
        idxs = indices_de_tablero(b)
        tablero_str = estado[idxs[0]: idxs[-1]+1]
        puntaje += evaluar_tablero_pequeno(tablero_str, jugador)
    return puntaje
#Usando el estado y la jugada anterior puntua la situación actual del juego,
#llamando a evaluar_tablero_pequeno y sumando condiciones del tablero mayor

# Función para el algoritmo Minimax
def minimax(estado, ultimo_movimiento, jugador, profundidad):
    succ = sucesores(estado, jugador, ultimo_movimiento)
    mejor_movimiento = (-inf, None)
    for s in succ:
        val = turno_min(s[0], s[1], oponente(jugador), profundidad-1,
                       -inf, inf)
        if val > mejor_movimiento[0]:
            mejor_movimiento = (val, s)
    return mejor_movimiento[1]
#A partir de los datos de tablero (estado) y situación (que tablero se juega por ult mov y el jugador)
#Se realiza una iteracion de tantos niveles como profundidad para generar el arbol de movimientos
#(por medio de varias llamadas a la funcion de sucesion en cada escenario)
#Se elige el mejor por minmax con Alpha Beta prunning y genera un movimiento

# Función para el turno del jugador que minimiza el puntaje
def turno_min(estado, ultimo_movimiento, jugador, profundidad, alfa, beta):
    global tablero_ganado
    if profundidad <= 0 or verificar_tablero_pequeno(tablero_ganado) != ".":
        return evaluar(estado, ultimo_movimiento, oponente(jugador))
    succ = sucesores(estado, jugador, ultimo_movimiento)
    for s in succ:
        val = turno_max(s[0], s[1], oponente(jugador), profundidad-1,
                       alfa, beta)
        if val < beta:
            beta = val
        if alfa >= beta:
            break
    return beta
#Sub funcion para la iteracion de minmax, ocupa los turnos a maximizar usando
#alfa y beta como índices de puntaje en el arbol segun las reglas de ABP

# Función para el turno del jugador que maximiza el puntaje
def turno_max(estado, ultimo_movimiento, jugador, profundidad, alfa, beta):
    global tablero_ganado
    if profundidad <= 0 or verificar_tablero_pequeno(tablero_ganado) != ".":
        return evaluar(estado, ultimo_movimiento, jugador)
    succ = sucesores(estado, jugador, ultimo_movimiento)
    for s in succ:
        val = turno_min(s[0], s[1], oponente(jugador), profundidad-1,
                       alfa, beta)
        if alfa < val:
            alfa = val
        if alfa >= beta:
            break
    return alfa
#Sub funcion para la iteracion de minmax, ocupa los turnos a maximizar usando
#alfa y beta como índices de puntaje en el arbol segun las reglas de ABP

# Función para validar una entrada de usuario
def entrada_valida(estado, movimiento):
    global tablero_ganado
    if not (0 < movimiento[0] < 10 and 0 < movimiento[1] < 10):
        return False
    if tablero_ganado[tablero(movimiento[0], movimiento[1])] != ".":
        return False
    if estado[indice(movimiento[0], movimiento[1])] != ".":
        return False
    return True
#Funcion de seguridad para la input, compara que la solicitud del usuario esté en las jugadas posibles

# Función para solicitar una entrada de usuario
def tomar_entrada(estado, movimiento_bot):
    print("-" * 40)
    todas_abiertas = False
    if movimiento_bot == -1 or len(movimientos_posibles(movimiento_bot)) > 9:
        todas_abiertas = True
    if todas_abiertas:
        print("¡Juega donde quieras!")
    else:
        diccionario_tablero = {0: "Superior Izquierda", 1: "Superior Centro", 2: "Superior Derecha",
                    3: "Centro Izquierda", 4: "Centro", 5: "Centro Derecha",
                    6: "Inferior Izquierda", 7: "Inferior Centro", 8: "Inferior Derecha"}
        print("¿Dónde te gustaría colocar 'X' en el tablero de "
              + diccionario_tablero[siguiente_tablero(movimiento_bot)] + "?")
    x = int(input("Fila = "))
    if x == -1:
        raise SystemExit
    y = int(input("Columna = "))
    print("")
    if movimiento_bot != -1 and indice(x, y) not in movimientos_posibles(movimiento_bot):
        raise ValueError
    if not entrada_valida(estado, (x, y)):
        raise ValueError
    return (x, y)
#Funcion de solicitud de llamada, genera los textos de instrucciones dado el último movimiento de la maquina

# Función principal del juego
def juego(estado="." * 81, profundidad=20):
    global tablero_ganado, objetivos_posibles
    objetivos_posibles = [(0, 4, 8), (2, 4, 6)]
    objetivos_posibles += [(i, i+3, i+6) for i in range(3)]
    objetivos_posibles += [(3*i, 3*i+1, 3*i+2) for i in range(3)]
    #Genera las 8 condiciones de victoria del gato clásico como comparación
    tablero_ganado = actualizar_tablero_ganado(estado)
    imprimir_tablero(estado)
    movimiento_bot = -1
    #Genera el estado base (vacío)
    
    turno = None
    
    # Elegir el primer turno
    while not turno:
      try:
        eleccion = input("¿Deseas jugar primero (X) o que juegue el bot primero (O)?").upper()
        if eleccion not in ("X", "O"):
          raise ValueError
        turno = eleccion
      except ValueError:
        print("¡Entrada inválida! Elige X o O.")
    #El usuario siempre juega con X, pero permite elegir O para que la maquina haga el primer turno
    
    if turno == "O":
        
      print("El bot está pensando...")
      estado_bot, movimiento_bot = minimax(estado, -1, "O", profundidad)

      print("-" * 40)
      print("El bot colocó 'O' en", movimiento_bot, "\n")
      imprimir_tablero(estado_bot)
      estado = estado_bot
      tablero_ganado = actualizar_tablero_ganado(estado)
      juego_ganado = verificar_tablero_pequeno(tablero_ganado)
     #Usa el caracter del jugador como estatus de turno para realizar los outputs
      
      
    while True:
        try:
            movimiento_usuario = tomar_entrada(estado, movimiento_bot)
        except ValueError:
            print("¡Entrada inválida o movimiento no posible!")
            imprimir_tablero(estado)
            continue
        except SystemError:
            print("¡Juego detenido!")
            break

        estado_usuario = agregar_pieza(estado, movimiento_usuario, "X")
        imprimir_tablero(estado_usuario)
        tablero_ganado = actualizar_tablero_ganado(estado_usuario)

        juego_ganado = verificar_tablero_pequeno(tablero_ganado)
        if juego_ganado != ".":
            estado = estado_usuario
            break
    #Se hace la input del turno del usuario y se actualizan a este los parámetros

        print("El bot está pensando...")
        estado_bot, movimiento_bot = minimax(estado_usuario, movimiento_usuario, "O", profundidad)

        print("-" * 40)
        print("El bot colocó 'O' en", movimiento_bot, "\n")
        imprimir_tablero(estado_bot)
        estado = estado_bot
        tablero_ganado = actualizar_tablero_ganado(estado)
        juego_ganado = verificar_tablero_pequeno(tablero_ganado)
        if juego_ganado != ".":
            break
    #Se hace la simulacion del turno de la máquina y se actualizan a este los parámetros

    if juego_ganado == "X":
        print("¡GANASTE!")
    else:
        print("¡PERDISTE!")
    #Mensaje de victoria, la variable se evalua cuando la wincon del tablero principal se cumple para algun jugador

    return estado

if __name__ == "__main__":
    
    ESTADO_INICIAL = "." * 81
    estado_final = juego(ESTADO_INICIAL, profundidad=5)

