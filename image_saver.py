"""This was used to generate the images in the `tiles` folder. Tiles were renamed manually."""

import cv2
import mss
import numpy

import Grid
import constants as const

grid = Grid.Grid()
testing = 0

with mss.mss() as screenshot:
    # Part of the screen to capture
    region = {"top": const.UL_CORNER_Y, "left": const.UL_CORNER_X,
              "width": const.TILE_WIDTH * const.COLS, "height": const.TILE_HEIGHT * const.ROWS}

    image = numpy.array(screenshot.grab(region))

    for i in range(const.ROWS):
        for j in range(const.COLS):
            start_x = j * const.TILE_WIDTH
            end_x = start_x + const.TILE_WIDTH
            start_y = i * const.TILE_HEIGHT
            end_y = start_y + const.TILE_HEIGHT
            crop = image[start_y:end_y, start_x:end_x]
            grayscale = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
            threshold = cv2.threshold(grayscale, 100, 255, cv2.THRESH_BINARY)

            # change this to your file name convention
            cv2.imwrite(f"tiles/{i}{j}.png", threshold[1])
