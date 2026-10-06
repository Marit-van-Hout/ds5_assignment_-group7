"""A simple backtracking solver for standard 9x9 Sudoku puzzles."""

from typing import Optional, Union

from .board import BoardValues, SudokuBoard


def _can_place(values: BoardValues, row: int, column: int, number: int) -> bool:
    """Return whether a number can be placed without breaking Sudoku rules."""
    for other_column in range(9):
        if other_column != column and values[row][other_column] == number:
            return False

    for other_row in range(9):
        if other_row != row and values[other_row][column] == number:
            return False

    first_box_row = (row // 3) * 3
    first_box_column = (column // 3) * 3
    for box_row in range(first_box_row, first_box_row + 3):
        for box_column in range(first_box_column, first_box_column + 3):
            if (box_row, box_column) != (row, column):
                if values[box_row][box_column] == number:
                    return False

    return True


def _has_valid_clues(values: BoardValues) -> bool:
    """Return whether the already-filled cells follow Sudoku rules."""
    for row in range(9):
        for column in range(9):
            number = values[row][column]
            if number != 0 and not _can_place(values, row, column, number):
                return False

    return True


def _solve(values: BoardValues) -> bool:
    """Fill the first empty cell, trying each number until one works."""
    for row in range(9):
        for column in range(9):
            if values[row][column] == 0:
                for number in range(1, 10):
                    if _can_place(values, row, column, number):
                        values[row][column] = number
                        if _solve(values):
                            return True
                        values[row][column] = 0

                return False

    return True


def solve_sudoku(
    board: Union[SudokuBoard, BoardValues],
) -> Optional[BoardValues]:
    """Return a solved copy of a board, or None when it has no solution.

    The input may be a SudokuBoard or a list of nine rows of nine integers.
    Invalid shapes or values raise ValueError, as they do in SudokuBoard.
    """
    if isinstance(board, SudokuBoard):
        values = board.values
    else:
        values = SudokuBoard(board).values

    if not _has_valid_clues(values):
        return None

    if not _solve(values):
        return None

    return values