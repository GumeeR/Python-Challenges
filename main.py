import random

def generate_maze():
    maze = [['⬜️' for _ in range(6)] for _ in range(6)]
    for _ in range(10):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        if maze[x][y] == '⬜️':
            maze[x][y] = '⬛️'
    return maze

def place_elements(maze):
    empty_cells = [(i, j) for i in range(6) for j in range(6) if maze[i][j] == '⬜️']
    mickey_pos = random.choice(empty_cells)
    empty_cells.remove(mickey_pos)
    exit_pos = random.choice(empty_cells)

    maze[mickey_pos[0]][mickey_pos[1]] = '🐭'
    maze[exit_pos[0]][exit_pos[1]] = '🚪'

    return mickey_pos, exit_pos

def display_maze(maze):
    for row in maze:
        print(' '.join(row))
    print()

def move_mickey(maze, mickey_pos, direction):
    x, y = mickey_pos
    new_x, new_y = x, y

    if direction == 'arriba':
        new_x -= 1
    elif direction == 'abajo':
        new_x += 1
    elif direction == 'izquierda':
        new_y -= 1
    elif direction == 'derecha':
        new_y += 1
    else:
        print("Dirección no válida. Intenta 'arriba', 'abajo', 'izquierda' o 'derecha'.")
        return mickey_pos, False

    if new_x < 0 or new_x >= 6 or new_y < 0 or new_y >= 6:
        print("¡No puedes salirte del laberinto!")
        return mickey_pos, False

    if maze[new_x][new_y] == '⬛️':
        print("¡No puedes moverte hacia un obstáculo!")
        return mickey_pos, False

    if maze[new_x][new_y] == '🚪':
        maze[x][y] = '⬜️'
        mickey_pos = (new_x, new_y)
        maze[new_x][new_y] = '🐭'
        display_maze(maze)
        print("¡Mickey ha escapado del laberinto!")
        return mickey_pos, True

    maze[x][y] = '⬜️'
    mickey_pos = (new_x, new_y)
    maze[new_x][new_y] = '🐭'

    return mickey_pos, False

print("¡Ayuda a Mickey a escapar del laberinto!")
maze = generate_maze()
mickey_pos, _ = place_elements(maze)
display_maze(maze)

while True:
    direction = input("¿Hacia dónde quieres moverte? (arriba, abajo, izquierda, derecha): ").lower()
    mickey_pos, escaped = move_mickey(maze, mickey_pos, direction)
    if escaped:
        break
    display_maze(maze)

print("¡Felicidades! Mickey ha llegado a la salida.")
