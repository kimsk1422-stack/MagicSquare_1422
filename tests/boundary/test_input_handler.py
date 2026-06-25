"""InputHandler — check_input → validate_lines 순서."""

import pytest

from src.boundary.input_handler import InputHandler
from src.boundary.grids import G1_GRID

pytestmark = pytest.mark.boundary

SOLVED_G1 = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]


def test_input_handler_validate_g1_incomplete(grid_g1):
    handler = InputHandler()
    outcome = handler.validate(grid_g1)
    assert outcome.accepted is True
    assert outcome.status == "incomplete"
    assert outcome.failed_lines == ()


def test_input_handler_validate_g1_solved_passes():
    handler = InputHandler()
    outcome = handler.validate([row[:] for row in SOLVED_G1])
    assert outcome.accepted is True
    assert outcome.status == "pass"
    assert outcome.failed_lines == ()


def test_input_handler_cells_to_grid_empty_blanks():
    handler = InputHandler()
    raw = [[str(cell) if cell else "" for cell in row] for row in G1_GRID]
    grid = handler.cells_to_grid(raw)
    assert grid == G1_GRID
