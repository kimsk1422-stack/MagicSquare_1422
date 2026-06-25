"""INV-010~011: 풀이 시 주어진 칸 보존·제약 기반 유도."""

import pytest

from src.magic_square import ValidationStatus, solve, validate_complete

from .conftest import PARTIAL_GRID, SOLVED_GRID

pytestmark = pytest.mark.entity


def test_inv_010_solve_preserves_given_cells(partial_grid):
    # INV-010: 14칸 고정값은 풀이 후에도 변경되지 않음
    result = solve(partial_grid)
    for r in range(4):
        for c in range(4):
            if partial_grid[r][c] != 0:
                assert result.grid[r][c] == partial_grid[r][c]


def test_inv_011_solve_fills_two_blanks_by_constraints(partial_grid):
    # INV-011: 빈칸 2값은 제약(34, 미사용 숫자)으로 유도 — (1,3)=8, (2,2)=7
    result = solve(partial_grid)
    assert result.grid[1][3] == 8
    assert result.grid[2][2] == 7
    assert result.filled == ((1, 3, 8), (2, 2, 7))


def test_solve_produces_valid_complete_grid(partial_grid):
    result = solve(partial_grid)
    validation = validate_complete(result.grid)
    assert validation.status == ValidationStatus.VALID
    assert result.grid == SOLVED_GRID
