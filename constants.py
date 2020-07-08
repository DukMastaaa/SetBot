"""Constants used throughout the files."""

GREEN = 1
ORANGE = 2
MAGENTA = 3
COLOURS = {GREEN, ORANGE, MAGENTA}

OVAL = 4
SQUIGGLE = 5
DIAMOND = 6
SHAPES = {OVAL, SQUIGGLE, DIAMOND}

HOLLOW = 7
STRIPED = 8
FILLED = 9
SHADINGS = {HOLLOW, STRIPED, FILLED}

ONE = 10
TWO = 11
THREE = 12
NUMBERS = {ONE, TWO, THREE}

PROPERTIES = ["colour", "shape", "shading", "number"]
DESCRIPTION = {
    GREEN: "green",
    ORANGE: "orange",
    MAGENTA: "magenta",
    OVAL: "oval",
    SQUIGGLE: "squiggle",
    DIAMOND: "diamond",
    HOLLOW: "hollow",
    STRIPED: "striped",
    FILLED: "filled",
    ONE: "one",
    TWO: "two",
    THREE: "three"
}

KEYS = "123qweasdzxcrtyfghvbn"

# These are highly specific to your monitor and computer configuration.
# The below are just what work for mine.
UL_CORNER_X = 585  # Top left tile - x coord
UL_CORNER_Y = 196  # Top left tile - y coord
TILE_WIDTH = 246   # Width of one tile (this includes within the empty spaces between the tiles)
TILE_HEIGHT = 154  # Height of one tile (as above)
SUB_CROP = 10      # Estimated thickness of tile border (used for cropping)

SLEEP_TIME = 0.5   # Time between each attempted input

# This is the maximum amount of rows/cols.
ROWS = 5
COLS = 3

# Specific to dark mode.
BGRS = {
    (3, 184, 0): GREEN,
    (71, 176, 255): ORANGE,
    (255, 71, 255): MAGENTA
}
