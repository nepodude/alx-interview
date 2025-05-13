#!/usr/bin/python3
"""
0-pascal_triangle.py
Generate Pascal’s Triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Return a list of lists representing the first n rows
    of Pascal’s Triangle. If n <= 0, returns [].
    """
    if n <= 0:
        return []

    triangle = [[1]]               # Row 0

    for row_idx in range(1, n):
        prev = triangle[-1]
        # Build the new row:
        #   - start with 1
        #   - each interior element is sum of two elements above
        #   - end with 1
        row = [1] + [prev[i - 1] + prev[i] for i in range(1, row_idx)] + [1]
        triangle.append(row)

    return triangle
