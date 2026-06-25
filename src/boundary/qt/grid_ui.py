"""PyQt6 GridUI — 4×4 격자 입력 위젯 (Boundary)."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLineEdit, QWidget

from src.entity.constants import BLANK_CELL, GRID_SIZE


class GridUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._cells: list[list[QLineEdit]] = []
        layout = QGridLayout(self)
        for row in range(GRID_SIZE):
            row_cells: list[QLineEdit] = []
            for col in range(GRID_SIZE):
                cell = QLineEdit(self)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setMaximumWidth(56)
                layout.addWidget(cell, row, col)
                row_cells.append(cell)
            self._cells.append(row_cells)

    def set_grid(self, grid: list[list[int]]) -> None:
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = grid[row][col]
                self._cells[row][col].setText("" if value == BLANK_CELL else str(value))

    def raw_cells(self) -> list[list[str]]:
        return [[self._cells[row][col].text() for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
