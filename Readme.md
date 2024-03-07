# Super Tic Tac Toe AI using Minimax

Welcome to the Super Tic Tac Toe AI! This Python program implements an AI player using the Minimax algorithm with Alpha-Beta Pruning to play Super Tic Tac Toe against a human opponent. The game supports a 3x3 grid of sub-boards, and the objective is to win by completing three sub-boards in a row, column, or diagonal.

## How to Play

1. Run the Python script in your preferred environment.
2. Choose whether you want to play first (X) or let the bot play first (O).
3. Enter your moves by specifying the row and column numbers (both ranging from 1 to 9).
4. The bot will calculate its move using the Minimax algorithm, and the game will continue until a winner is determined or the board is full.

## Game Board

The game board is displayed as a 3x3 grid of sub-boards, each with a 3x3 grid of cells. The coordinates for moves are entered in the format `row, column`, where both row and column values range from 1 to 9.

```plaintext
   1 2 3   4 5 6   7 8 9
--------------------------
1| . . . | . . . | . . . |
2| . . . | . . . | . . . |
3| . . . | . . . | . . . |
--------------------------
4| . . . | . . . | . . . |
5| . . . | . . . | . . . |
6| . . . | . . . | . . . |
--------------------------
7| . . . | . . . | . . . |
8| . . . | . . . | . . . |
9| . . . | . . . | . . . |
--------------------------
```

## AI Implementation

The AI uses the Minimax algorithm with Alpha-Beta Pruning to make strategic decisions. The depth of the search tree is controlled by the `profundidad` parameter in the `juego` function. Adjusting this parameter can impact the AI's level of difficulty.

## Code Structure Overview

Here's a brief overview of the key functions in the provided Python code:

### Board Representation Functions

- `indice(x, y)`: Calculates the index of a move in the game state string.
- `tablero(x, y)`: Determines the board to which a move belongs.
- `siguiente_tablero(i)`: Calculates the next board to play based on the last move.
- `indices_de_tablero(b)`: Returns the indices of moves in a specific board.
- `imprimir_tablero(estado)`: Prints the current game state in a visual format.
- `agregar_pieza(estado, movimiento, jugador)`: Adds a piece to the game state.

### Game Logic Functions

- `actualizar_tablero_ganado(estado)`: Updates the state of won sub-boards.
- `verificar_tablero_pequeno(tablero_str)`: Checks if a sub-board is won by a player.
- `movimientos_posibles(ultimo_movimiento)`: Returns possible moves in the next board.
- `sucesores(estado, jugador, ultimo_movimiento)`: Generates successors for a given state.
- `evaluar_tablero_pequeno(tablero_str, jugador)`: Evaluates a sub-board for a given player.
- `evaluar(estado, ultimo_movimiento, jugador)`: Evaluates the overall game state.
- `minimax(estado, ultimo_movimiento, jugador, profundidad)`: Minimax algorithm.
- `turno_min(estado, ultimo_movimiento, jugador, profundidad, alfa, beta)`: Minimizing player's turn.
- `turno_max(estado, ultimo_movimiento, jugador, profundidad, alfa, beta)`: Maximizing player's turn.
- `entrada_valida(estado, movimiento)`: Validates user input for a move.
- `tomar_entrada(estado, movimiento_bot)`: Handles user input and provides instructions.

### Main Game Loop

- `juego(estado="." * 81, profundidad=20)`: Main function to run the Super Tic Tac Toe game.

### Script Execution

The game is initialized with the `ESTADO_INICIAL` and runs through the `juego` function.

Feel free to explore and modify the code to enhance features or customize the gameplay experience. If you have any questions or need further clarification on specific parts of the code, feel free to ask!
