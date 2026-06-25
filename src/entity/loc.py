"""빈칸 위치 탐색 — D-LOC (FR-LOC-01, INV-002)."""

from src.entity.constants import BLANK_CELL, COORD_INDEX_ORIGIN, GRID_SIZE


def find_blank_coords(grid):
    coords = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL:  # INV-002: 0인 칸 열거
                coords.append(
                    (row + COORD_INDEX_ORIGIN, col + COORD_INDEX_ORIGIN)
                )  # D-LOC-01: row-major, 1-index (row, col)
    return coords
