from typing import List


class Cell:
    def __init__(s, x, y) -> None:
        s.visited = False
        s.north_wall = True
        s.south_wall = True
        s.east_wall = True
        s.west_wall = True
        s.entry = False
        s.exit = False
        s.neigbours: List['Cell'] = []
        s.x = x
        s.y = y
        s.val = 15

    def __str__(s) -> str:
        return f"cell({s.x}, {s.y})"

    def before(s, maze) -> 'Cell':
        return maze[s.x - 1][s.y]

    def after(s, maze) -> 'Cell':
        return maze[s.x + 1][s.y]

    def abbove(s, maze) -> 'Cell':
        return maze[s.x][s.y - 1]

    def under(s, maze) -> 'Cell':
        return maze[s.x][s.y + 1]

    # methods to overload [ == ]
