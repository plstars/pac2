#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# GLOBAL CONSTANTS

# @ -> our hero
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G...@.|.|",
    "|........|",
    "|--------|"
]


def check_map(map):
    """Checks the map for validity

    Args:
        map (list): the map to check

    Returns:
        bool: True if the map is valid, False otherwise
    """

    def first_last_valid(row):
        # Checks if the first and last characters of a row are valid
        return row[0] == '|' and row[-1] == '|'

    def is_valid(map, x, y):
        # Checks if a position in the map is valid
        return map[x][y] in ['|', '-', '.', 'G', 'P', '@']

    def first_last_row_valid(row):
        # Checks if the first and last rows of the map are valid
        return row[0] == '|' and row[-1] == '|' and row[1:-1].count('-') == len(row[1:-1])

    number_of_rows = len(map)
    number_of_columns = len(map[0])
    for x in range(number_of_rows):
        if len(map[x]) != number_of_columns:
            return False
        for y in range(number_of_columns):
            if not is_valid(map, x, y):
                return False

    if not first_last_row_valid(map[0]):
        return False
    if not first_last_row_valid(map[-1]):
        return False

    return True
