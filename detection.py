"""Provides colour, shape, shading and number detection capability for one tile."""

from typing import Tuple

import cv2
import numpy

import constants as const

tiles = {}
for shape_code in range(4, 7):
    for shading_code in range(7, 10):
        for number_code in range(10, 13):
            tile_code = f"{shape_code}_{shading_code}_{number_code}"
            filename = f"tiles/{tile_code}.png"
            temp_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            tiles[tile_code] = temp_image


def get_colour(image: numpy.ndarray) -> int:
    """Returns the colour of the tile. Each pixel is matched against BGR values in `const.BGRS`."""
    for pixel_row in image:
        for pixel in pixel_row:
            bgr = tuple(pixel[:3])
            if bgr in const.BGRS:
                return const.BGRS[bgr]
    return 0  # no colour


def get_shape_shading_number(image: numpy.ndarray) -> Tuple[int, ...]:
    """Returns the shape, shading and number of the tile from the image."""
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(grayscale, 70, 255, cv2.THRESH_BINARY)
    lowest_difference = 0
    lowest_code = ""
    for code in tiles:
        difference = numpy.abs(
            threshold[1].astype(numpy.int16) - tiles[code].astype(numpy.int16)
        ).sum()
        if difference < lowest_difference or lowest_difference == 0:
            lowest_difference = difference
            lowest_code = code

    shape, maybe_shading, number = (int(value) for value in lowest_code.split("_"))
    shading = confirm_shading(threshold[1])  # if tile is striped, maybe_shading is inaccurate.

    return shape, shading, number


def confirm_shading(image: numpy.ndarray) -> int:
    """Returns the shading of a tile from the image.

    This is a separate function from `get_shape_shading_number` since
    the shading value returned is inconsistent if the tile is striped.

    Code adapted from cortex#9689 uwu
    """
    # Turns black/white image into True/False array
    bool_image = image > 127

    # Removes outside border
    whites = numpy.where(bool_image)
    bool_image = bool_image[min(whites[0]) + const.SUB_CROP:max(whites[0]) - const.SUB_CROP,
                            min(whites[1]) + const.SUB_CROP:max(whites[1]) - const.SUB_CROP]

    # Isolates shape
    whites = numpy.where(bool_image)  # todo: change both sections into 1 - performance?
    bool_image = bool_image[min(whites[0]):max(whites[0]), min(whites[1]):max(whites[1])]

    intersect_match = numpy.sum(
        bool_image[:(-1 if bool_image.shape[0] % 2 else None): 2] ^  # XOR is True if different
        bool_image[1::2]
    ) / (bool_image.shape[0] * bool_image.shape[1])  # divided by bbox area

    if intersect_match > 0.065:
        return const.STRIPED
    else:
        # Create new array with two more elements for width/height than image
        image_2 = numpy.zeros((bool_image.shape[0] + 2, bool_image.shape[1] + 2), numpy.uint8)
        # Put image in so there is 1px border of 0
        image_2[1:-1:, 1:-1:] = bool_image.astype('uint8') * 255
        # Fill the outside of the shapes with white pixels.
        # Now, *only* the inside of the shapes will be black if they are hollow.
        cv2.floodFill(image_2, None, (0, 0), 255)

        white_ratio = numpy.sum(image_2 > 127) / (image_2.shape[0] * image_2.shape[1])
        if white_ratio > 0.9:
            return const.FILLED
        else:
            return const.HOLLOW
