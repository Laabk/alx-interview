#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    this function will returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    d = []
    if n <= 0:
        return d
    d = [[1]]
    for it in range(1, n):
        temp = [1]
        for m in range(len(d[it - 1]) - 1):
            curren = d[it - 1]
            temp.append(d[it - 1][m] + d[it - 1][m + 1])
        temp.append(1)
        d.append(temp)
    return d
