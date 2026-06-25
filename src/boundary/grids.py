"""Boundary 기본 격자 — PRD §3.2 슬라이드 예시 (G1)."""

G1_GRID = [
    [16, 3, 2, 13],
    [5, 10, 11, 0],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]


def g1_grid():
    return [row[:] for row in G1_GRID]
