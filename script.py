import random
WIDTH, HEIGHT = 10, 10
maze = [['#'] * (2 * WIDTH + 1) for _ in range(2 * HEIGHT + 1)]
def generate_maze(x, y):
    """Recursive Backtracking algorithm."""
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < 2 * WIDTH and 0 < ny < 2 * HEIGHT and maze[ny][nx] == '#':
            maze[y + dy // 2][x + dx // 2] = ' '
            maze[ny][nx] = ' '
            generate_maze(nx, ny)

def print_maze():
    """Prints the maze."""
    for row in maze:
        print("".join(row))

def main():
    """Main function."""
    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '
    generate_maze(start_x, start_y)
    maze[1][0] = 'S'
    maze[-2][-1] = 'E'
    print_maze()

if __name__ == "__main__":
    main()
