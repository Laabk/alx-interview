#!/usr/bin/python3
"""this solves the N-queens puzzle involved.
d.
"""
import sys


def init_board(n):
    """this will initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Returning the deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """
    the lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """
    spots on a chessboard.
   """
    for d in range(col + 1, len(board)):
        board[row][d] = "x"
    for d in range(col - 1, -1, -1):
        board[row][d] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    d = col + 1
    for r in range(row + 1, len(board)):
        if d >= len(board):
            break
        board[r][d] = "x"
        d += 1
    d = col - 1
    for r in range(row - 1, -1, -1):
        if d < 0:
            break
        board[r][d]
        d -= 1
    d = col + 1
    for r in range(row - 1, -1, -1):
        if d >= len(board):
            break
        board[r][c] = "x"
        d += 1
    d = col - 1
    for r in range(row + 1, len(board)):
        if d < 0:
            break
        board[r][d] = "x"
        d -= 1


def recursive_solve(board, row, queens, solutions):
    """
    this Recursively solve an N-queens puzzle.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
