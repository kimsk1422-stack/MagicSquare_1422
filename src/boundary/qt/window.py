"""PyQt6 메인 윈도우 — GridUI · InputHandler · ResultDisplay."""

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget

from src.boundary.grids import g1_grid
from src.boundary.input_handler import InputHandler
from src.boundary.qt.grid_ui import GridUI
from src.boundary.qt.result_display import ResultDisplay


class MagicSquareWindow(QMainWindow):
    def __init__(self, handler: InputHandler | None = None):
        super().__init__()
        self.setWindowTitle("MagicSquare_1422 — 검증")
        self._handler = handler or InputHandler()

        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self._grid_ui = GridUI(self)
        self._grid_ui.set_grid(g1_grid())
        layout.addWidget(self._grid_ui)

        validate_button = QPushButton("검증", self)
        validate_button.clicked.connect(self._on_validate)
        layout.addWidget(validate_button)

        self._result_display = ResultDisplay(self)
        layout.addWidget(self._result_display)

    def _on_validate(self) -> None:
        try:
            grid = self._handler.cells_to_grid(self._grid_ui.raw_cells())
        except ValueError as error:
            QMessageBox.warning(self, "입력 오류", str(error))
            return
        outcome = self._handler.validate(grid)
        self._result_display.show_outcome(outcome)
