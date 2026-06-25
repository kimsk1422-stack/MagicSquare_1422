"""INV-006~009: 완성 격자 10선·1~16·판정 결정성."""

import pytest

from src.magic_square import ValidationStatus, line_sums, validate_complete

from .conftest import BAD_DUPLICATE_GRID, BAD_ROW_SUM_GRID, SOLVED_GRID

pytestmark = pytest.mark.entity


def test_inv_006_all_ten_lines_sum_to_34(solved_grid):
    # INV-006: 4행·4열·2대각선 각 합 = 34
    sums = line_sums(solved_grid)
    assert len(sums) == 10
    assert all(total == 34 for total in sums)


def test_inv_007_complete_grid_uses_1_through_16_once(solved_grid):
    # INV-007: 1~16 각각 정확히 1번
    flat = sorted(cell for row in solved_grid for cell in row)
    assert flat == list(range(1, 17))


def test_validate_complete_accepts_solved_slide(solved_grid):
    result = validate_complete(solved_grid)
    assert result.status == ValidationStatus.VALID
    assert result.violations == ()


def test_inv_009_valid_implies_ten_lines_and_full_set(solved_grid):
    # INV-009: VALID ⇒ INV-006·007 동시 만족
    result = validate_complete(solved_grid)
    assert result.status == ValidationStatus.VALID
    assert all(total == 34 for total in line_sums(solved_grid))
    assert sorted(cell for row in solved_grid for cell in row) == list(range(1, 17))


def test_validate_complete_rejects_bad_row_sum():
    result = validate_complete(BAD_ROW_SUM_GRID)
    assert result.status == ValidationStatus.INVALID
    assert any("row" in v for v in result.violations)


def test_validate_complete_rejects_duplicate():
    result = validate_complete(BAD_DUPLICATE_GRID)
    assert result.status == ValidationStatus.INVALID
    assert any("duplicate" in v or "1..16" in v for v in result.violations)


def test_inv_008_validation_is_deterministic(solved_grid):
    # INV-008: 같은 입력 → 같은 판정 (SC-2)
    first = validate_complete(solved_grid)
    second = validate_complete(solved_grid)
    assert first == second
