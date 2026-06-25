"""U-GRID-01: 4×4 격자 표시 (grid_g1 SSOT)."""

import pytest

from src.entity.constants import GRID_SIZE

pytestmark = pytest.mark.boundary


def test_u_grid_01_displays_4x4_grid_g1(client_with_g1, grid_g1):
    # Given: grid_g1 — 4×4, 0이 정확히 2개, row-major
    # When: GET / (격자 페이지)
    response = client_with_g1.get("/")

    # Then: grid_g1 4×4 격자 16칸 표시
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    cell_count = 0
    for row in grid_g1:
        for cell in row:
            assert f'data-cell="{cell}"' in body
            cell_count += 1
    assert cell_count == GRID_SIZE * GRID_SIZE  # U-GRID-01
