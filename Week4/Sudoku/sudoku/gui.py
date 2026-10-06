"""Tkinter interface for playing the bundled Sudoku puzzles."""

import tkinter as tk
from tkinter import ttk
from typing import Dict, Optional, Tuple

from .board import SudokuBoard
from .puzzles import get_available_puzzles, get_puzzle
from .solver import solve_sudoku


class SudokuApp:
    """Display and manage a playable Sudoku puzzle."""

    def __init__(self, root: Optional[tk.Tk] = None) -> None:
        self.root = root or tk.Tk()
        self.root.title("Sudoku")

        self._board = SudokuBoard()
        self._cell_entries: Dict[Tuple[int, int], tk.Entry] = {}
        self._cell_variables: Dict[Tuple[int, int], tk.StringVar] = {}

        self._build_controls()
        self._load_puzzle(get_available_puzzles()[0])

    def _build_controls(self) -> None:
        """Create the puzzle selector, grid, feedback, and action buttons."""
        controls = ttk.Frame(self.root, padding=10)
        controls.pack()

        ttk.Label(controls, text="Puzzle:").grid(row=0, column=0, padx=5)
        self._selected_puzzle = tk.StringVar()
        self._puzzle_selector = ttk.Combobox(
            controls,
            textvariable=self._selected_puzzle,
            values=get_available_puzzles(),
            state="readonly",
            width=12,
        )
        self._puzzle_selector.grid(row=0, column=1, padx=5)
        self._puzzle_selector.bind(
            "<<ComboboxSelected>>",
            self._on_puzzle_selected,
        )

        self._grid_frame = ttk.Frame(self.root, padding=8, relief="solid")
        self._grid_frame.pack(padx=10, pady=5)

        self._feedback = tk.StringVar()
        self._feedback_label = ttk.Label(
            self.root,
            textvariable=self._feedback,
            padding=5,
            foreground="#333333",
        )
        self._feedback_label.pack()

        buttons = ttk.Frame(self.root, padding=10)
        buttons.pack()
        ttk.Button(buttons, text="Hint", command=self._give_hint).grid(
            row=0, column=0, padx=5
        )
        ttk.Button(buttons, text="Solve", command=self._solve_puzzle).grid(
            row=0, column=1, padx=5
        )

    def _load_puzzle(self, puzzle_id: str) -> None:
        """Load a selected puzzle and draw clues and editable cells."""
        puzzle = get_puzzle(puzzle_id)
        self._board = SudokuBoard(puzzle["grid"])
        self._selected_puzzle.set(puzzle_id)
        self._feedback.set("")
        self._feedback_label.configure(foreground="#333333")
        self._cell_entries.clear()
        self._cell_variables.clear()

        for widget in self._grid_frame.winfo_children():
            widget.destroy()

        for row in range(9):
            for column in range(9):
                value = self._board.get_value(row, column)
                cell_padding = (
                    (2 if column % 3 == 0 else 1),
                    (2 if row % 3 == 0 else 1),
                )
                if self._board.is_clue(row, column):
                    cell = tk.Label(
                        self._grid_frame,
                        text=str(value),
                        width=2,
                        height=1,
                        font=("TkDefaultFont", 14, "bold"),
                        background="#e8e8e8",
                        relief="solid",
                        borderwidth=1,
                    )
                else:
                    variable = tk.StringVar()
                    entry = tk.Entry(
                        self._grid_frame,
                        textvariable=variable,
                        width=2,
                        justify="center",
                        font=("TkDefaultFont", 14),
                        validate="key",
                        validatecommand=(
                            self.root.register(self._validate_cell),
                            "%P",
                            str(row),
                            str(column),
                        ),
                    )
                    self._cell_entries[(row, column)] = entry
                    self._cell_variables[(row, column)] = variable
                    cell = entry

                cell.grid(
                    row=row,
                    column=column,
                    padx=cell_padding[0],
                    pady=cell_padding[1],
                    ipady=3,
                )

    def _validate_cell(self, proposed_value: str, row: str, column: str) -> bool:
        """Accept a cell edit only when SudokuBoard allows the move."""
        row_index = int(row)
        column_index = int(column)

        if proposed_value == "":
            self._board.set_value(row_index, column_index, 0)
            self._clear_feedback()
            return True

        if len(proposed_value) != 1 or proposed_value not in "123456789":
            self._show_error("Enter a digit from 1 to 9, or clear the cell.")
            return False

        try:
            self._board.set_value(row_index, column_index, int(proposed_value))
        except ValueError:
            self._show_error(
                "That move conflicts with a value in its row, column, or box."
            )
            return False

        self._clear_feedback()
        self._check_for_completion()
        return True

    def _on_puzzle_selected(self, _event: tk.Event) -> None:
        """Load the puzzle currently chosen in the selector."""
        self._load_puzzle(self._selected_puzzle.get())

    def _give_hint(self) -> None:
        """Fill the first empty editable cell with its solved value."""
        solution = solve_sudoku(self._board)
        if solution is None:
            self._show_error("This puzzle has no valid solution.")
            return

        for row in range(9):
            for column in range(9):
                if self._board.get_value(row, column) == 0:
                    self._set_cell(row, column, solution[row][column])
                    self._feedback_label.configure(foreground="#245c2a")
                    self._feedback.set(
                        "Hint: filled row {0}, column {1}.".format(
                            row + 1, column + 1
                        )
                    )
                    self._check_for_completion()
                    return

        self._show_success("The puzzle is already complete.")

    def _solve_puzzle(self) -> None:
        """Fill every empty cell when the current board has a solution."""
        solution = solve_sudoku(self._board)
        if solution is None:
            self._show_error("This puzzle has no valid solution.")
            return

        for row in range(9):
            for column in range(9):
                if self._board.get_value(row, column) == 0:
                    self._set_cell(row, column, solution[row][column])

        self._show_success("Solved! The puzzle is complete.")

    def _set_cell(self, row: int, column: int, value: int) -> None:
        """Update both the SudokuBoard and its editable cell."""
        self._board.set_value(row, column, value)
        self._cell_variables[(row, column)].set(str(value))

    def _check_for_completion(self) -> None:
        """Show success feedback when the board is correctly solved."""
        if self._board.is_solved():
            self._show_success("Congratulations! You solved the puzzle.")

    def _clear_feedback(self) -> None:
        self._feedback.set("")
        self._feedback_label.configure(foreground="#333333")

    def _show_error(self, message: str) -> None:
        self._feedback.set(message)
        self._feedback_label.configure(foreground="#a02020")

    def _show_success(self, message: str) -> None:
        self._feedback.set(message)
        self._feedback_label.configure(foreground="#245c2a")


def main() -> None:
    """Start the Sudoku application."""
    root = tk.Tk()
    SudokuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()