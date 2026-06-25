"""E-011: 완성 후 행 합 ≠ 34."""

import pytest

from src.boundary.gate import check_complete

pytestmark = pytest.mark.boundary

# 1~16 각 1회, 0행만 합 33 (나머지 10선 = 34)
E011_ROW_ONLY_GRID = [
    [1, 15, 14, 3],
    [8, 10, 11, 5],
    [12, 6, 7, 9],
    [13, 4, 2, 16],
]


def test_e_011_rejects_bad_row_sum():
    result = check_complete(E011_ROW_ONLY_GRID)
    assert result.accepted is False
    assert result.code == "E-011"
