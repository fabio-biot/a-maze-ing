from enum import Enum

line1 = "█"
print(line1)

class Direction(Enum):
    N = (0, -1)
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)


OPPOSITE = {
    Direction.N: Direction.S,
    Direction.S: Direction.N,
    Direction.E: Direction.W,
    Direction.W: Direction.E,
}


class Cell:
    def __init__(self):
        self.walls = {
            Direction.N: True,
            Direction.E: True,
            Direction.S: True,
            Direction.W: True
        }
        self.visited = False


class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = self._create_grid()

    def _create_grid(self):
        return [[Cell() for _ in range(self.width)]
                for _ in range(self.height)]

    def get_neighbors(self, x: int, y: int):
        neighbors = []

        for direction in Direction:
            dx, dy = direction.value
            nx, ny = x + dx, y + dy

            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbors.append((direction, nx, ny))

        return neighbors

    def remove_wall(self, x, y, nx, ny, direction: Direction):
        self.grid[y][x].walls[direction] = False
        self.grid[ny][nx].walls[OPPOSITE[direction]] = False

    def get_cell(self, x, y):
        return self.grid[y][x]


def main():
    maze = MazeGenerator(10, 5)

    print(maze.width, maze.height)

    for row in maze.grid:
        for cell in row:
            print("█", end="")
        print()


if __name__ == "__main__":
    main()
