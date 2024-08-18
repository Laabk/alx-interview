#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       this acts to rotates 2D matrix 90 degrees clockwise
       Matrix is edited in-place"""
    left, right = 0, len(matrix) - 1

    while left < right:
        for d in range(right - left):
            top, bottom = left, right
            # this save topleft  value
            topLeft = matrix[top][left + d]
            # this move bottom left to top left
            matrix[top][left + d] = matrix[bottom - d][left]
            # this move bottom right to bottom left
            matrix[bottom - d][left] = matrix[bottom][right - d]
            # tis move top right to bottom right
            matrix[bottom][right - d] = matrix[top + d][right]
            # this move top left to top right
            matrix[top + d][right] = topLeft
        right -= 1
        left += 1
