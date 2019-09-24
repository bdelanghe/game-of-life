""""CONWAY GAME OF LIFE"""

from cmd import Cmd
from typing import List


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

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def make_grid(self) -> List[list]:
        line = [0 for _ in range(self.size)]
        return [list(line) for _ in range(self.size)]

    def update_grid(self) -> int:
        pass

    def get_world(self):
        pass

class Rules:




world = World(3)

print(world.grid)


