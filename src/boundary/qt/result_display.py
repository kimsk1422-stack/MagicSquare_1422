"""PyQt6 ResultDisplay — 검증 결과 표시 (Boundary)."""

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.boundary.input_handler import ValidationOutcome


class ResultDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self._status_label = QLabel("status: —", self)
        self._failed_label = QLabel("failed_lines: —", self)
        layout.addWidget(self._status_label)
        layout.addWidget(self._failed_label)

    def show_outcome(self, outcome: ValidationOutcome) -> None:
        if not outcome.accepted:
            self._status_label.setText(f"status: rejected ({outcome.code})")
            self._failed_label.setText("failed_lines: —")
            return
        self._status_label.setText(f"status: {outcome.status}")
        if outcome.failed_lines:
            lines_text = ", ".join(outcome.failed_lines)
            self._failed_label.setText(f"failed_lines: {lines_text}")
        else:
            self._failed_label.setText("failed_lines: (없음)")
