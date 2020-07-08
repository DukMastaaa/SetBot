"""The main file used to run the program."""

import time

import keyboard
import mss
import numpy

import Grid
import Tile
import constants as const
import detection

grid = Grid.Grid()
time.sleep(2)  # Gives you some time to click off the terminal window and onto browser :)

with mss.mss() as screenshot:
    region = {"top": const.UL_CORNER_Y, "left": const.UL_CORNER_X,
              "width": const.TILE_WIDTH * const.COLS, "height": const.TILE_HEIGHT * const.ROWS}

    while True:
        image = numpy.array(screenshot.grab(region))
        for i in range(const.ROWS):
            for j in range(const.COLS):
                start_x = j * const.TILE_WIDTH
                end_x = start_x + const.TILE_WIDTH
                start_y = i * const.TILE_HEIGHT
                end_y = start_y + const.TILE_HEIGHT
                current_index = (j % const.COLS) + (i * const.COLS)

                crop = image[start_y:end_y, start_x:end_x]
                colour = detection.get_colour(crop)
                if colour == 0:
                    del grid[current_index:]
                    break  # only happens on the last row (if number of rows < 5)

                shape, shading, number = detection.get_shape_shading_number(crop)
                detected_tile = Tile.Tile(colour, shape, shading, number)

                if len(grid) < current_index + 1:
                    grid.append(detected_tile)
                else:
                    if grid[current_index] != detected_tile:
                        grid[current_index] = detected_tile

        time.sleep(const.SLEEP_TIME)
        solution = grid.find_first_set()
        print("solution: " + solution)
        if len(solution) == 3:
            keyboard.write(solution)
