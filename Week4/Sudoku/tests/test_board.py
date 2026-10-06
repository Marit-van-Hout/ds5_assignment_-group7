"""Unit tests for the SudokuBoard class."""

import unittest

from sudoku.board import SudokuBoard


class TestSudokuBoard(unittest.TestCase):
    """Check SudokuBoard values, rules, and solved-board detection."""

    def setUp(self) -> None:
        puzzle = [[0 for _ in range(9)] for _ in range(9)]
        puzzle[0][0] = 1
        puzzle[1][1] = 2
        puzzle[3][3] = 3
        self.board = SudokuBoard(puzzle)

    def test_can_set_a_valid_value(self) -> None:
        self.board.set_value(0, 1, 4)
        self.assertEqual(self.board.get_value(0, 1), 4)

    def test_rejects_values_outside_one_to_nine(self) -> None:
        with self.assertRaises(ValueError):
            self.board.set_value(0, 1, 10)

        with self.assertRaises(ValueError):
            self.board.set_value(0, 1, -1)

    def test_rejects_conflicting_values(self) -> None:
        with self.assertRaises(ValueError):
            self.board.set_value(0, 1, 1)  # Same row as 1.

        with self.assertRaises(ValueError):
            self.board.set_value(1, 0, 1)  # Same column as 1.

        with self.assertRaises(ValueError):
            self.board.set_value(2, 2, 1)  # Same 3x3 box as 1.

    def test_cannot_change_an_original_clue(self) -> None:
        with self.assertRaises(ValueError):
            self.board.set_value(0, 0, 4)

        self.assertEqual(self.board.get_value(0, 0), 1)
        self.assertTrue(self.board.is_clue(0, 0))

    def test_can_clear_an_entered_value(self) -> None:
        self.board.set_value(0, 1, 4)
        self.board.set_value(0, 1, 0)

        self.assertEqual(self.board.get_value(0, 1), 0)

    def test_detects_a_solved_board(self) -> None:
        solved_values = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
        ]
        solved_board = SudokuBoard(solved_values)

        self.assertTrue(solved_board.is_solved())

    def test_incomplete_board_is_not_solved(self) -> None:
        self.assertFalse(self.board.is_solved())


if __name__ == "__main__":
    unittest.main()