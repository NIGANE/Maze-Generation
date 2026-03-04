from bfs.Gen import Gen
import curses
from bfs.visualization import run_visualizer


def print_maze(generated: Gen) -> None:
    maze = generated.get_map()
    for line in maze:
        for cell in line:
            print(cell.val, end=' ')
        print()


data: dict = {
    'entry': (0, 0),
    'exit': (10, 10),
    'h': 11,
    'w': 11
}


def main() -> None:
    gen = Gen(data['w'], data['h'], data['entry'], data['exit'])
    curses.wrapper(run_visualizer, gen)


main() if __name__ == "__main__" else None
