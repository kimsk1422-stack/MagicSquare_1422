"""D-LOC-01: 빈칸 좌표 row-major (FR-LOC-01, INV-002)."""

import pytest

pytestmark = pytest.mark.entity


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출

    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    pytest.fail("RED: D-LOC-01 — 구현 없음, 의도적 실패")
