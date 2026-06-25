"""10선 합 검사 — 완성/미완성/실패 판정."""

from src.entity.constants import BLANK_CELL, GRID_SIZE, MAGIC_CONSTANT


def validate_lines(grid):
    has_blank = any(cell == BLANK_CELL for row in grid for cell in row)
    failed_lines = []

    for row in range(GRID_SIZE):
        if sum(grid[row][col] for col in range(GRID_SIZE)) != MAGIC_CONSTANT:
            failed_lines.append(f"R{row + 1}")

    for col in range(GRID_SIZE):
        if sum(grid[row][col] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            failed_lines.append(f"C{col + 1}")

    if sum(grid[index][index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        failed_lines.append("D1")

    if sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        failed_lines.append("D2")

    if has_blank:
        return {"status": "incomplete", "failed_lines": []}

    if failed_lines:
        return {"status": "fail", "failed_lines": failed_lines}

    return {"status": "pass", "failed_lines": []}
