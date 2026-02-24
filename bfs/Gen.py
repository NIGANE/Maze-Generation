from typing import List, Tuple
from bfs.Cell import Cell
from bfs.helpers import indexof


class Gen:
    def __init__(s, w: int, h: int, en: Tuple[int, int], ex: Tuple[int, int]
                 ) -> None:
        s.width: int = w
        s.height: int = h
        s.maze: List[List[Cell]] = [
            [Cell(x, y) for x in range(s.width)] for y in range(s.height)
            ]
        s.entry: Cell = s.maze[en[0]][en[1]]
        s.exit: Cell = s.maze[ex[0]][ex[1]]
        s.entry.entry = True
        s.exit.exit = True
        s.all: List[Cell]
        for line in s.maze:
            for cell in line:
                s.conf_nighbours(cell)

    def get_map(s) -> List[List[Cell]]:
        return s.maze

    def get_rand_choice(s, all: List[Cell]) -> Cell:
        return all[len(all) - 1]

    def break_wall(s, main_cell: Cell, target: Cell) -> None:
        pass

    def conf_nighbours(s, c: Cell) -> None:
        if c.x != 0 and c.x < s.width - 1:
            # add s.x - 1 and s.x + 1
            c.neigbours.append(c.before(s.maze)) if not c.before(s.maze).visited else None
            c.neigbours.append(c.after(s.maze)) if not c.after(s.maze).visited else None
        elif c.x > 0:
            # add s.x - 1
            c.neigbours.append(c.before(s.maze)) if not c.before(s.maze).visited else None
        elif c.x < s.width - 1:
            # add s.x + 1
            c.neigbours.append(c.after(s.maze)) if not c.after(s.maze).visited else None

        if c.y != 0 and c.y < s.height - 1:
            # add c.y - 1 and c.y + 1
            c.neigbours.append(c.abbove(s.maze)) if not c.abbove(s.maze).visited else None
            c.neigbours.append(c.under(s.maze)) if not c.under(s.maze).visited else None
        elif c.y > 0:
            # add c.y - 1
            c.neigbours.append(c.abbove(s.maze)) if not c.abbove(s.maze).visited else None
        elif c.y < s.height - 1:
            # add s.y + 1
            c.neigbours.append(c.under(s.maze)) if not c.under(s.maze).visited else None

    def roll(s) -> None:
        s.all = s.get_valid_neighbours(s.entry)
        main_cell: Cell = s.entry
        while (len(s.all) > 0):
            for target in s.all:
                s.break_wall(main_cell, target)
                s.all = [*s.all, *s.get_valid_neighbours(target)]
                s.all.pop(indexof(s.all, target))

    def get_valid_neighbours(s, cell: Cell) -> List[Cell]:
        return cell.neigbours
