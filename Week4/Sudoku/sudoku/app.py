"""Start the Sudoku application."""

import os
import sys
import tkinter as tk

if __package__:
    from .gui import SudokuApp
else:
    # Allow this file to run directly as ``python app.py``.
    package_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, package_parent)
    from sudoku.gui import SudokuApp


def main() -> None:
    """Create the root window and start the Sudoku application."""
    root = tk.Tk()
    SudokuApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()