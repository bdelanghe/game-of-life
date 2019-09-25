""""CONWAY GAME OF LIFE"""

from cmd import Cmd
from typing import List, Optional, Dict
from random import sample
from itertools import product



class Play(Cmd):
    """printing"""

    ruler = '='
    lastcmd = ''
    intro = "hello"
    doc_leader = ""
    doc_header = "Documented commands (type help <topic>):"
    misc_header = "Miscellaneous help topics:"
    undoc_header = "Undocumented commands:"
    nohelp = "*** No help on %s"
    use_rawinput = 1

    def __init__(self) -> None:
        super().__init__()


class Session:
    """session  object to """

    def __init__(self) -> None:
        pass


class World:
    """the current state of the game"""

    def __init__(self, size):
        self.size: int = size
        self.rules: object = Rules()
        self._grid: Optional[Dict[tuple, int]] = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @property
    def grid(self) -> Optional[Dict[tuple, int]]:
        return self._grid

    @grid.setter
    def grid(self, value: Optional[int]):
        g = {}
        for cord in list(product(range(self.size),range(self.size))):
            g[cord] = 0
        if value is not None:
            live = sample(g.keys(), value)
            for cord in live:
                g[cord] = 1
        self._grid = g

    def update_grid(self, cell: tuple, value: int) -> None:
        self.grid[cell] = value

    def __str__(self):
        output = ""
        for i, v in enumerate(list(self.grid.values())):
            if i % self.size == 0:
                output +="\n"
            output += str(v) + " "
        return output


class Rules:
    """Rules object to """

    def __init__(self) -> None:
        pass


world = World(4)
world.grid = 5
print(world)
# print(world.grid)



