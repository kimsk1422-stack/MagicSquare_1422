"""부분 격자 풀이 — D-SOL (INV-010~011)."""

from dataclasses import dataclass
from itertools import permutations

from src.entity.constants import (
    BLANK_CELL,
    CELL_MAX,
    CELL_MIN,
    GRID_SIZE,
)
from src.entity.lines import all_ten_lines_match


@dataclass(frozen=True)
class SolveResult:
    grid: list[list[int]]
    filled: tuple[tuple[int, int, int], ...]


def solve(grid):
    working = [row[:] for row in grid]
    blanks = []
    used = set()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = working[row][col]
            if value == BLANK_CELL:
                blanks.append((row, col))
            else:
                used.add(value)

    unused = [n for n in range(CELL_MIN, CELL_MAX + 1) if n not in used]
    (row_a, col_a), (row_b, col_b) = blanks

    for value_a, value_b in permutations(unused, 2):
        trial = [row[:] for row in working]
        trial[row_a][col_a] = value_a
        trial[row_b][col_b] = value_b
        if all_ten_lines_match(trial):
            return SolveResult(
                grid=trial,
                filled=((row_a, col_a, value_a), (row_b, col_b, value_b)),
            )  # INV-010: 고정값 보존 · INV-011: 제약 기반 유도

    raise ValueError("no solution")
