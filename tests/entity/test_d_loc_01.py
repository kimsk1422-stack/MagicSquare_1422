"""D-LOC-01: 빈칸 좌표 row-major (FR-LOC-01, INV-002)."""

import pytest

from src.entity.loc import find_blank_coords

pytestmark = pytest.mark.entity


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    result = find_blank_coords(grid_g1)

    # Then: [(2,4),(3,3)] 반환 (1-index, row-major)
    assert result == [(2, 4), (3, 3)]  # D-LOC-01
