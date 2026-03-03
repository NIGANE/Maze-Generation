from bfs.Gen import Gen


def print_maze(generated: Gen) -> None:
    maze = generated.get_map()
    for line in maze:
        for cell in line:
            print(cell.val, end=' ')
        print()


data: dict = {
    'entry': (0, 0),
    'exit': (3, 3),
    'h': 4,
    'w': 4
}


def main() -> None:
    gen = Gen(data['w'], data['h'], data['entry'], data['exit'])
    print_maze(gen)
    gen.gen_dfs()
    print_maze(gen)


main() if __name__ == "__main__" else None
