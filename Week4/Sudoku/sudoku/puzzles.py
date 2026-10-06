"""Puzzle data for the Sudoku application.

The grids are taken from the Project Euler Problem 96 dataset. A zero marks
an empty cell.
"""

SOURCE_NAME = "Project Euler Problem 96: Su Doku"
SOURCE_URL = "https://projecteuler.net/project/resources/p096_sudoku.txt"

PUZZLES = {
    "Grid 01": {
        "source_name": SOURCE_NAME,
        "source_url": SOURCE_URL,
        "dataset_record_id": "Grid 01",
        "grid": [
            [0, 0, 3, 0, 2, 0, 6, 0, 0],
            [9, 0, 0, 3, 0, 5, 0, 0, 1],
            [0, 0, 1, 8, 0, 6, 4, 0, 0],
            [0, 0, 8, 1, 0, 2, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 6, 7, 0, 8, 2, 0, 0],
            [0, 0, 2, 6, 0, 9, 5, 0, 0],
            [8, 0, 0, 2, 0, 3, 0, 0, 9],
            [0, 0, 5, 0, 1, 0, 3, 0, 0],
        ],
    },
    "Grid 02": {
        "source_name": SOURCE_NAME,
        "source_url": SOURCE_URL,
        "dataset_record_id": "Grid 02",
        "grid": [
            [2, 0, 0, 0, 8, 0, 3, 0, 0],
            [0, 6, 0, 0, 7, 0, 0, 8, 4],
            [0, 3, 0, 5, 0, 0, 2, 0, 9],
            [0, 0, 0, 1, 0, 5, 4, 0, 8],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 2, 7, 0, 6, 0, 0, 0],
            [3, 0, 1, 0, 0, 7, 0, 4, 0],
            [7, 2, 0, 0, 4, 0, 0, 6, 0],
            [0, 0, 4, 0, 1, 0, 0, 0, 3],
        ],
    },
}


def get_available_puzzles():
    """Return the identifiers of the puzzles included in this module."""
    return list(PUZZLES.keys())


def get_puzzle(puzzle_id):
    """Return a puzzle and its source details by dataset record identifier."""
    return PUZZLES[puzzle_id]