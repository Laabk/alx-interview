#!/usr/bin/python3
"""This func solves the N-queens puzzle.
and determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard."""


import sys


def generate_solutions(row, column):
    solutn = [[]]
    for queen in range(row):
        solutn = place_queen(queen, column, solutn)
    return solutn


def place_queen(queen, column, prv_solutn):
    safe_position = []
    for array in prv_solutn:
        for x in range(column):
            if is_safe(queen, d, array):
                safe_position.append(array + [d])
    return safe_position


def is_safe(q, d, array):
    if d in array:
        return (False)
    else:
        return all(abs(array[column] - d) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    solutns = generate_solutns(n, n)
    for array in solutns:
        clean = []
        for q, d in enumerate(array):
            clean.append([q, d])
        print(clean)


if __name__ == '__main__':
    n_queens()
