"""Show a hint and a complete solution for Grid 02."""

from sudoku.board import SudokuBoard
from sudoku.puzzles import get_puzzle
from sudoku.solver import solve_sudoku


def print_board(board: SudokuBoard) -> None:
    """Print the board, using a dot to show each empty cell."""
    for row in board.values:
        print(" ".join(str(value) if value != 0 else "." for value in row))


def main() -> None:
    """Print Grid 02, one hint, and then the fully solved board."""
    puzzle = get_puzzle("Grid 02")
    board = SudokuBoard(puzzle["grid"])
    solution = solve_sudoku(board)

    if solution is None:
        raise ValueError("Grid 02 does not have a valid solution.")

    print("Grid 02 - original puzzle:")
    print_board(board)

    hint_row = None
    hint_column = None
    for row in range(9):
        for column in range(9):
            if board.get_value(row, column) == 0:
                hint_row = row
                hint_column = column
                break
        if hint_row is not None:
            break

    if hint_row is not None and hint_column is not None:
        hint_value = solution[hint_row][hint_column]
        board.set_value(hint_row, hint_column, hint_value)
        print(
            "\nHint: row {0}, column {1} is {2}.".format(
                hint_row + 1, hint_column + 1, hint_value
            )
        )
        print_board(board)

    for row in range(9):
        for column in range(9):
            if board.get_value(row, column) == 0:
                board.set_value(row, column, solution[row][column])

    print("\nGrid 02 - fully solved:")
    print_board(board)


if __name__ == "__main__":
    main()