"""Unit tests for the Sudoku solver."""

import unittest

from sudoku.board import SudokuBoard
from sudoku.puzzles import get_puzzle
from sudoku.solver import solve_sudoku


class TestSudokuSolver(unittest.TestCase):
    """Check that the solver handles the bundled puzzles and invalid clues."""

    def test_solves_grid_01(self) -> None:
        self.assert_puzzle_is_solved("Grid 01")

    def test_solves_grid_02(self) -> None:
        self.assert_puzzle_is_solved("Grid 02")

    def assert_puzzle_is_solved(self, puzzle_id: str) -> None:
        """Check that the result is valid and preserves all original clues."""
        puzzle = get_puzzle(puzzle_id)["grid"]
        solution = solve_sudoku(puzzle)

        self.assertIsNotNone(solution)
        solved_board = SudokuBoard(solution)
        self.assertTrue(solved_board.is_solved())

        for row in range(9):
            for column in range(9):
                original_value = puzzle[row][column]
                if original_value != 0:
                    self.assertEqual(
                        solution[row][column],
                        original_value,
                    )

    def test_returns_none_for_invalid_puzzle(self) -> None:
        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        puzzle[0][0] = 5
        puzzle[0][1] = 5

        self.assertIsNone(solve_sudoku(puzzle))


if __name__ == "__main__":
    unittest.main()