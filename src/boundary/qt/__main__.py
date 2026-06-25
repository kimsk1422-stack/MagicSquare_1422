"""PyQt6 GUI 진입점 — python -m src.boundary.qt"""

import sys


def main() -> None:
    try:
        from PyQt6.QtWidgets import QApplication
    except ImportError as error:
        raise SystemExit(
            "PyQt6가 필요합니다. 설치: pip install -e \".[gui]\""
        ) from error

    from src.boundary.qt.window import MagicSquareWindow

    app = QApplication(sys.argv)
    window = MagicSquareWindow()
    window.show()
    raise SystemExit(app.exec())


if __name__ == "__main__":
    main()
