#!/usr/bin/python3

"""
5-main
"""


def island_perimeter(grid):
    """a function to calculate the perimeter of the island."""
    horizontal_perimeter = 0
    counter = 0
    semi_counter = 0
    counted = 0
    sum_counted = 0
    vertical_perimeter = 0
    len_grid = len(grid)

    """if the length of grid is 0"""
    if len_grid == 0:
        return 0

    """if the grid has only one row"""
    if len_grid == 1:
        perimter += sum(item for item in grid[0])
        return perimter

    """if the grid has multicple rows"""
    for item in grid:
        """for each row"""
        semi_counter = 0
        for element in item:
            """for each element in a row"""
            if counter == 0:
                """dealing with the first row"""
                if element == 1 and grid[1][semi_counter] == 1:
                    horizontal_perimeter += 1
                if element == 1 and grid[1][semi_counter] == 0:
                    horizontal_perimeter += 2

            if counter == len_grid - 1:
                """dealing with the last row"""
                if element == 1 and grid[len_grid - 2][semi_counter] == 1:
                    horizontal_perimeter += 1
                if element == 1 and grid[len_grid - 2][semi_counter] == 0:
                    horizontal_perimeter += 2

            if 0 < counter < len_grid - 1:
                """dealing with all rows in between"""
                if (
                    element == 1
                    and grid[counter - 1][semi_counter] == 1
                    and grid[counter + 1][semi_counter] == 0
                ):
                    """When a 1 has a 1 above and a 0 below"""
                    horizontal_perimeter += 1
                if (
                    element == 1
                    and grid[counter - 1][semi_counter] == 0
                    and grid[counter + 1][semi_counter] == 1
                ):
                    """When a 1 has a 0 above and a 1 below"""
                    horizontal_perimeter += 1
                if (
                    element == 1
                    and grid[counter - 1][semi_counter] == 0
                    and grid[counter + 1][semi_counter] == 0
                ):
                    """When a 1 has a 0 below and above"""
                    horizontal_perimeter += 2

            semi_counter += 1
        counter += 1
        vertical_perimeter += vertical_calculator(item)
    return horizontal_perimeter + vertical_perimeter


def vertical_calculator(array):
    """Calculates the vertical perimeter of any row"""
    power_of_array = 0
    helper = 0

    """When the array is of length 1"""
    if len(array) == 1:
        return array[0]

    """When the array is composed of ones only"""
    if all(element == 1 for element in array):
        return 2

    """When the array is a usual array"""
    for item in array:
        if helper == 0 and item == 1 and array[1] == 0:
            """When the first 1 is followed by a 1"""
            power_of_array += 2
        if helper == 0 and item == 1 and array[1] == 1:
            """When the first 1 is followed by a 0"""
            power_of_array += 1
        if helper == len(array) - 1 and item == 1 and array[helper - 1] == 0:
            """When the last 1 is preceeded by a 0"""
            power_of_array += 2
        if helper == len(array) - 1 and item == 1 and array[helper - 1] == 1:
            """When the last 1 is preceeded by a 1"""
            power_of_array += 1
        if (
            0 < helper < len(array) - 1
            and item == 1
            and array[helper - 1] == 0
            and array[helper + 1] == 0
        ):
            """when the 1 is surrounded by 0's"""
            power_of_array += 2
        if (
            0 < helper < len(array) - 1
            and item == 1
            and array[helper - 1] == 1
            and array[helper + 1] == 0
        ):
            """When the 1 is preceeded by a 1 and followed by a 0"""
            power_of_array += 1
        if (
            0 < helper < len(array) - 1
            and item == 1
            and array[helper - 1] == 0
            and array[helper + 1] == 1
        ):
            """When the 1 is preceeded by a 0 and followed by a 1"""
            power_of_array += 1
        helper += 1
    return power_of_array
