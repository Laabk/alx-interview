#!/usr/bin/python3
"""
   this Island Perimeter will return the perimeter of any
   island described in grid
"""


def island_perimeter(grid):
    """the sland perimenter function involved"""
    _perimeter = 0
    for d in range(len(grid)):
        for i in range(len(grid[d])):
            if grid[d][i] == 1:
                _perimeter += 4
                if d > 0 and grid[d-1][i] == 1:
                    _perimeter -= 2
                if i > 0 and grid[d][i-1] == 1:
                    _perimeter -= 2
    return _perimeter
