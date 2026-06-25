"""E-002: 빈칸 개수 전제 — Boundary 입력 거절."""

import pytest

from src.boundary.gate import check_input

pytestmark = pytest.mark.boundary


def test_e_002_rejects_three_blanks():
    grid = [
        [0, 3, 2, 13],
        [5, 10, 11, 0],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
    result = check_input(grid)
    assert result.accepted is False
    assert result.code == "E-002"


def test_e_002_accepts_slide_partial_grid(grid_g1):
    result = check_input(grid_g1)
    assert result.accepted is True
    assert result.code is None
