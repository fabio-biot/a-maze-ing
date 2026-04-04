path_test = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (2, 6)]

def output_generator(path: list[tuple]):
    cell = self.maze[y][x]
    val = 0
    if getattr(cell, "is_wall_north", False) or y == 0:
        val |= 1 << 0
    if getattr(cell, "is_wall_east", False) or x == self.width * 2:
        val |= 1 << 1
    if getattr(cell, "is_wall_south", False) or y == self.height * 2:
        val |= 1 << 2
    if getattr(cell, "is_wall_west", False) or x == 0:
        val |= 1 << 3
    return hex(val)[2:].upper()