from enum import Enum
import random

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

    def get_unvisited_neighbors(self, x: int, y: int):
        neighbors = self.get_neighbors(x, y)
        return [(direction, nx, ny) for direction, nx, ny in neighbors
                if not self.get_cell(nx, ny).visited]

    def remove_wall(self, x, y, nx, ny, direction: Direction):
        self.grid[y][x].walls[direction] = False
        self.grid[ny][nx].walls[OPPOSITE[direction]] = False

    def get_cell(self, x, y):
        return self.grid[y][x]

    def generate(self):
        stack = []
        # i = 0
        x, y = 0, 0
        self.get_cell(x, y).visited = True
        stack.append((x, y))

        while stack: # i != 5
            print(stack)
            x, y = stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)

            if neighbors:
                direction, nx, ny = random.choice(neighbors)
                self.remove_wall(x, y, nx, ny, direction)
            
                self.get_cell(nx, ny).visited = True
                stack.append((nx, ny))
            else:
                stack.pop()
            # i += 1
        return stack
    
    def display(self):
        print("█" + "████" * self.width)

        for y in range(self.height):
            line1 = "█"
            line2 = "█"

            for x in range(self.width):
                cell = self.get_cell(x, y)
                line1 += "   "
                if cell.walls[Direction.E]:
                    line1 += "█"
                else:
                    line1 += " "
                if cell.walls[Direction.S]:
                    line2 += "████"
                else:
                    line2 += "   █"

            print(line1)
            print(line2)


def main():
    maze = MazeGenerator(10, 5)

    print(maze.width, maze.height)
    maze.display()
    stack = maze.generate()
    for row in maze.grid:
        for cell in row:
            print("█", end="")
        print()
    print(stack)
    maze.display()
    print("SIU")


if __name__ == "__main__":
    main()
