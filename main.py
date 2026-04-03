from generate_maze import MazeGenerator
from parsing import parse


def main():
    try:
        config = parse()
        width = int(config.get("width"))
        height = int(config.get("height"))
        print(f"Parsed config: width={width}, height={height}")
    except Exception as e:
        print(f"Error parsing config: {e}")
    
    maze = MazeGenerator(width, height)

    print(maze.width, maze.height)
    # maze.display()
    maze.generate()
    maze.display()

if __name__ == "__main__":
    main()
