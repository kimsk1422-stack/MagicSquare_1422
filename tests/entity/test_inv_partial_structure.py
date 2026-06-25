"""INV-001~004: 부분 격자 입력 전제 (형태·빈칸·범위·초기 중복)."""

import pytest

from src.magic_square import ValidationStatus, validate_partial

pytestmark = pytest.mark.entity


def test_inv_001_partial_grid_is_4x4(partial_grid):
    # INV-001: 4×4 정수 격자
    assert len(partial_grid) == 4
    assert all(len(row) == 4 for row in partial_grid)


def test_inv_002_partial_grid_has_exactly_two_blanks(partial_grid):
    # INV-002: 0인 칸은 정확히 2개
    blanks = sum(cell == 0 for row in partial_grid for cell in row)
    assert blanks == 2


def test_validate_partial_accepts_slide_example(partial_grid):
    # INV-001~004: 슬라이드 예시는 부분 입력 전제를 만족
    result = validate_partial(partial_grid)
    assert result.status == ValidationStatus.ACCEPTABLE_PARTIAL


def test_inv_003_rejects_out_of_range_non_blank():
    # INV-003: 0이 아닌 칸은 1~16
    grid = [
        [16, 3, 2, 13],
        [5, 10, 11, 0],
        [9, 6, 0, 12],
        [4, 15, 14, 17],
    ]
    result = validate_partial(grid)
    assert result.status == ValidationStatus.INVALID


def test_inv_004_rejects_initial_duplicate():
    # INV-004: 주어진 14칸에 중복 없음 — 3이 두 번
    grid = [
        [16, 3, 2, 13],
        [5, 10, 11, 0],
        [9, 3, 0, 12],
        [4, 15, 14, 1],
    ]
    result = validate_partial(grid)
    assert result.status == ValidationStatus.INVALID
