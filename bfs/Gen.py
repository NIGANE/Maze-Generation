from typing import List, Tuple
from bfs.Cell import Cell
import random


class Gen:
    def __init__(s, w: int, h: int, en: Tuple[int, int], ex: Tuple[int, int]
                 ) -> None:
        s.width: int = w
        s.height: int = h
        s.maze: List[List[Cell]] = [
            [Cell(x, y) for x in range(s.width)] for y in range(s.height)
            ]
        s.entry: Cell = s.maze[en[1]][en[0]]
        s.exit: Cell = s.maze[ex[1]][ex[0]]
        s.entry.entry = True
        s.exit.exit = True
        s.nib: List[Cell] = []
        s.visited: list[Cell] = []
        s.broken_walls: int = 0
        for line in s.maze:
            for cell in line:
                s.conf_nighbours(cell)

    def get_map(s) -> List[List[Cell]]:
        return s.maze

    def get_rand_choice(s, all: List[Cell]) -> Cell:
        return random.choice(all)

    def break_wall(s, main_cell: Cell, target: Cell) -> None:
        main_cell.pt.append(target)
        s.broken_walls += 1
        if main_cell.y != 0:
            abbove: Cell = main_cell.abbove(s.maze)
            if abbove == target:
                main_cell.break_north()
                target.break_south()
                return
        if main_cell.y != s.height - 1:
            under: Cell = main_cell.under(s.maze)
            if under == target:
                main_cell.break_south()
                target.break_north()
                return
        if main_cell.x != 0:
            before: Cell = main_cell.before(s.maze)
            if before == target:
                main_cell.break_west()
                target.break_est()
                return
        if main_cell.x != s.width - 1:
            after: Cell = main_cell.after(s.maze)
            if after == target:
                main_cell.break_est()
                target.break_west()
                return

    def conf_nighbours(s, c: Cell) -> None:
        if c.x != 0 and c.x < s.width - 1:
            # add s.x - 1 and s.x + 1
            (c.neigbours.append(c.before(s.maze)))
            (c.neigbours.append(c.after(s.maze)))
        elif c.x > 0:
            # add s.x - 1
            (c.neigbours.append(c.before(s.maze)))
        elif c.x < s.width - 1:
            # add s.x + 1
            (c.neigbours.append(c.after(s.maze)))

        if c.y != 0 and c.y < s.height - 1:
            # add c.y - 1 and c.y + 1
            (c.neigbours.append(c.abbove(s.maze)))
            (c.neigbours.append(c.under(s.maze)))
        elif c.y > 0:
            # add c.y - 1
            (c.neigbours.append(c.abbove(s.maze)))
        elif c.y < s.height - 1:
            # add s.y + 1
            (c.neigbours.append(c.under(s.maze)))

    def gen_bfs(s) -> None:
        s.visited.append(s.entry)
        queue: List[Cell] = [s.entry]
        for ele in queue:
            nighbours = s.get_valid_neighbours(ele)
            random.shuffle(nighbours)
            for nib in nighbours:
                if nib not in s.visited:
                    s.visited.append(nib)
                    s.break_wall(ele, nib)
                    queue.append(nib)

    def gen_dfs(s) -> None:
        s.visited.append(s.entry)
        stack: List[Cell] = [s.entry]
        while s.broken_walls < (s.width * s.height) - 1:
            nighbours = s.get_valid_neighbours(stack[-1])
            if len(nighbours) == 0:
                stack.pop()
            else:
                target: Cell = random.choice(nighbours)
                s.visited.append(target)
                s.break_wall(stack[-1], target)
                stack.append(target)

    def solve_dfs(s) -> None:
        s.visited = [s.entry]
        stack: List[Cell] = [s.entry]

        while stack[-1] != s.exit:
            cur: Cell = stack[-1]
            if len(cur.pt) > 0:
                target: Cell = random.choice(cur.pt)
                s.visited.append(target)



    def get_valid_neighbours(s, cell: Cell) -> List[Cell]:
        return [cell for cell in cell.neigbours if cell not in s.visited]
