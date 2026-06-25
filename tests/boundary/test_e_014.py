"""E-014: 완성 후 1~16 중복/누락."""

import pytest

from src.boundary.gate import check_complete

pytestmark = pytest.mark.boundary

# 7 중복·14 누락, 10선 합은 의도적으로 검사하지 않음(집합 위반만)
E014_DUPLICATE_ONLY_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 7, 1],
]


def test_e_014_rejects_duplicate_values():
    result = check_complete(E014_DUPLICATE_ONLY_GRID)
    assert result.accepted is False
    assert result.code == "E-014"
