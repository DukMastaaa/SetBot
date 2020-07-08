"""Represents a tile in the game."""

import constants as const


class Tile(object):
    def __init__(self, colour: int, shape: int, shading: int, number: int):
        self.colour = colour
        self.shape = shape
        self.shading = shading
        self.number = number

    @staticmethod
    def is_a_set(tile1: "Tile", tile2: "Tile", tile3: "Tile") -> bool:
        """Returns whether the three tiles make a set."""
        for attribute in const.PROPERTIES:
            first = getattr(tile1, attribute)
            second = getattr(tile2, attribute)
            third = getattr(tile3, attribute)

            if (first == second and second == third) or \
                    (first != second and second != third and first != third):
                pass
            else:
                return False
        return True

    def __eq__(self, other) -> bool:
        """Required for == and != comparison."""
        if not isinstance(other, Tile):
            return NotImplemented
        for attribute in const.PROPERTIES:
            if getattr(self, attribute) != getattr(other, attribute):
                return False
        return True

    def __repr__(self) -> str:
        return f"Tile({self.colour}, {self.shape}, {self.shading}, {self.number})"

    def __str__(self) -> str:
        return f"Tile({const.DESCRIPTION[self.colour]}, " \
               f"{const.DESCRIPTION[self.shape]}, " \
               f"{const.DESCRIPTION[self.shading]}, " \
               f"{const.DESCRIPTION[self.number]})"
