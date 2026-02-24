from bfs.Gen import Gen


def print_maze(generated: Gen) -> None:
    maze = generated.get_map()
    for line in maze:
        for cell in line:
            print(cell.val, end=' ')
        print()


data: dict = {
    'entry': (0, 0),
    'exit': (4, 4),
    'h': 5,
    'w': 5
}


def main() -> None:
    gen = Gen(5, 5, data['entry'], data['exit'])
    print_maze(gen)
    maze = gen.get_map()
    cell = maze[0][0]
    print(cell.visited)



main() if __name__ == "__main__" else None
