"""10선 합산 — 행·열·대각선 (INV-006)."""

from src.entity.constants import GRID_SIZE, MAGIC_CONSTANT


def line_sums(grid):
    sums = []
    for row in range(GRID_SIZE):
        sums.append(sum(grid[row][col] for col in range(GRID_SIZE)))
    for col in range(GRID_SIZE):
        sums.append(sum(grid[row][col] for row in range(GRID_SIZE)))
    sums.append(sum(grid[index][index] for index in range(GRID_SIZE)))
    sums.append(
        sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE))
    )
    return sums


def all_ten_lines_match(grid):
    return all(total == MAGIC_CONSTANT for total in line_sums(grid))
