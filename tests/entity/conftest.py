"""Entity 트랙 공통 격자 — 슬라이드 예시 (docs/PRD.md §3.2)."""

import pytest

# 부분 입력: 빈칸 2개 (0). INV-001~004 전제를 만족.
PARTIAL_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 0],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]

# 풀이 완료: (1,3)=8, (2,2)=7
SOLVED_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# INV-006 위반: 1행 합 ≠ 34
BAD_ROW_SUM_GRID = [
    [16, 3, 2, 12],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1],
]

# INV-007 위반: 7 중복
BAD_DUPLICATE_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 7],
]


@pytest.fixture
def partial_grid():
    return [row[:] for row in PARTIAL_GRID]


@pytest.fixture
def solved_grid():
    return [row[:] for row in SOLVED_GRID]
