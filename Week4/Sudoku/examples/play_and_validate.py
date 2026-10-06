"""Play one move on Grid 01 and see how SudokuBoard checks it."""

from sudoku.board import SudokuBoard
from sudoku.puzzles import get_puzzle


def print_board(board: SudokuBoard) -> None:
    """Print the board, using a dot to show each empty cell."""
    for row in board.values:
        print(" ".join(str(value) if value != 0 else "." for value in row))


def main() -> None:
    """Load Grid 01, make a valid move, and demonstrate a rejected move."""
    puzzle = get_puzzle("Grid 01")
    board = SudokuBoard(puzzle["grid"])

    print("Grid 01 - initial board:")
    print_board(board)

    # Row 1, column 1 is empty; 4 does not conflict with its row, column, or box.
    board.set_value(0, 0, 4)
    print("\nAfter placing 4 in row 1, column 1:")
    print_board(board)

    # The same row already contains a 3, so this move must be rejected.
    try:
        board.set_value(0, 0, 3)
    except ValueError as error:
        print("\nInvalid move rejected: {0}".format(error))


if __name__ == "__main__":
    main()