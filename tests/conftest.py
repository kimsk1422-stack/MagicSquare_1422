"""Track 공통 픽스처 — PRD §3.2 슬라이드 예시 (G1)."""

import pytest

# G1: 빈칸(0) 정확히 2개, row-major 4×4
G1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 0],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]


@pytest.fixture
def grid_g1():
    return [row[:] for row in G1_GRID]
