from typing import List, Optional, Set, Tuple


BoardValues = List[List[int]]
CellPosition = Tuple[int, int]


class SudokuBoard:
    """Store a Sudoku board and check its rules."""

    SIZE = 9

    def __init__(self, values: Optional[BoardValues] = None) -> None:
        if values is None:
            values = []
            while len(values) < self.SIZE:
                values.append([0] * self.SIZE)

        if len(values) != self.SIZE:
            raise ValueError("A Sudoku board must have exactly 9 rows.")

        self._values = []
        self._clues: Set[CellPosition] = set()

        for row_index, row_values in enumerate(values):
            if len(row_values) != self.SIZE:
                raise ValueError("Each Sudoku row must have exactly 9 values.")

            copied_row = []
            for column_index, value in enumerate(row_values):
                if type(value) is not int or not 0 <= value <= self.SIZE:
                    raise ValueError("Board values must be integers from 0 to 9.")

                copied_row.append(value)
                if value != 0:
                    self._clues.add((row_index, column_index))

            self._values.append(copied_row)

    @property
    def values(self) -> BoardValues:
        """Return a copy of the current board values."""
        return [row_values[:] for row_values in self._values]

    @property
    def clues(self) -> Set[CellPosition]:
        """Return the positions that were filled in the original puzzle."""
        return self._clues.copy()

    def get_value(self, row_index: int, column_index: int) -> int:
        """Return the value in one cell."""
        self._check_position(row_index, column_index)
        return self._values[row_index][column_index]

    def is_clue(self, row_index: int, column_index: int) -> bool:
        """Return whether a cell was filled in the original puzzle."""
        self._check_position(row_index, column_index)
        return (row_index, column_index) in self._clues

    def can_place(self, row_index: int, column_index: int, value: int) -> bool:
        """Return whether a value can be placed without breaking Sudoku rules."""
        self._check_position(row_index, column_index)

        if type(value) is not int or not 1 <= value <= self.SIZE:
            return False
        if self.is_clue(row_index, column_index):
            return False

        for other_column in range(self.SIZE):
            if (other_column != column_index
                    and self._values[row_index][other_column] == value):
                return False

        for other_row in range(self.SIZE):
            if (other_row != row_index
                    and self._values[other_row][column_index] == value):
                return False

        first_box_row = (row_index // 3) * 3
        first_box_column = (column_index // 3) * 3
        for box_row in range(first_box_row, first_box_row + 3):
            for box_column in range(first_box_column, first_box_column + 3):
                if ((box_row, box_column) != (row_index, column_index)
                        and self._values[box_row][box_column] == value):
                    return False

        return True

    def set_value(self, row_index: int, column_index: int, value: int) -> None:
        """Set an editable cell to 0 through 9, rejecting invalid moves."""
        self._check_position(row_index, column_index)

        if (type(value) is not int or not 0 <= value <= self.SIZE):
            raise ValueError("Cell values must be integers from 0 to 9.")
        if self.is_clue(row_index, column_index):
            raise ValueError("Original puzzle clues cannot be changed.")
        if value != 0 and not self.can_place(row_index, column_index, value):
            raise ValueError("That value conflicts with the row, column, or box.")

        self._values[row_index][column_index] = value

    def is_solved(self) -> bool:
        """Return whether every row, column, and 3x3 box contains 1 through 9."""
        expected_values = set(range(1, self.SIZE + 1))

        for row_index in range(self.SIZE):
            if set(self._values[row_index]) != expected_values:
                return False

            column_values = {
                self._values[other_row][row_index]
                for other_row in range(self.SIZE)
            }
            if column_values != expected_values:
                return False

        for first_box_row in range(0, self.SIZE, 3):
            for first_box_column in range(0, self.SIZE, 3):
                box_values = {
                    self._values[row_index][column_index]
                    for row_index in range(first_box_row, first_box_row + 3)
                    for column_index in range(first_box_column, first_box_column + 3)
                }
                if box_values != expected_values:
                    return False

        return True

    def _check_position(self, row_index: int, column_index: int) -> None:
        if (type(row_index) is not int or type(column_index) is not int
                or not 0 <= row_index < self.SIZE
                or not 0 <= column_index < self.SIZE):
            raise IndexError("Cell positions must be row and column indexes from 0 to 8.")
