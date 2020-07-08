"""Represents the game grid."""

import constants as const
import Tile
from itertools import combinations


class Grid(list):
    """Represents the game grid. All items should be tiles."""
    def find_first_set(self) -> str:
        """Returns the keyboard inputs corresponding to the first set on the grid."""
        for combination in combinations(self, 3):
            first, second, third = combination
            if Tile.Tile.is_a_set(first, second, third):
                return "".join([const.KEYS[self.index(tile)] for tile in combination])
        return "Can't find a set!"
