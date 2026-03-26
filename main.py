line1 = "█"
print(line1)


class Cell:
    def __init__(self):
        self.walls = {
            'N': True,
            'E': True,
            'S': True,
            'W': True
        }


grid = [print(line1) for _ in range(10)]

def display_game(game, grid_size):
    c = 65
    # Other rows
    for i in range(grid_size):
        for j in range(grid_size):
            print(f"| {game} ", end='')
        print("| ")
        print((grid_size*4+4)*"-")


display_game('█', 7)
