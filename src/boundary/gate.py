"""입력·완성 검증 게이트 — E-001~005, E-011~015."""

from dataclasses import dataclass

from src.entity.constants import BLANK_CELL, CELL_MAX, CELL_MIN, GRID_SIZE
from src.magic_square import ValidationStatus, validate_complete


@dataclass(frozen=True)
class BoundaryResult:
    accepted: bool
    code: str | None = None


def check_input(grid) -> BoundaryResult:
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return BoundaryResult(False, "E-001")  # E-001: 4×4 아님

    blank_count = sum(cell == BLANK_CELL for row in grid for cell in row)
    if blank_count != 2:
        return BoundaryResult(False, "E-002")  # E-002: 빈칸 ≠ 2개

    seen = set()
    for row in grid:
        for cell in row:
            if not isinstance(cell, int):
                return BoundaryResult(False, "E-005")  # E-005: 비정수
            if cell == BLANK_CELL:
                continue
            if cell < CELL_MIN or cell > CELL_MAX:
                return BoundaryResult(False, "E-003")  # E-003: 범위 밖
            if cell in seen:
                return BoundaryResult(False, "E-004")  # E-004: 초기 중복
            seen.add(cell)

    return BoundaryResult(True)


def check_filled_input(grid) -> BoundaryResult:
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return BoundaryResult(False, "E-001")  # E-001: 4×4 아님

    seen = set()
    for row in grid:
        for cell in row:
            if not isinstance(cell, int):
                return BoundaryResult(False, "E-005")  # E-005: 비정수
            if cell == BLANK_CELL:
                return BoundaryResult(False, "E-002")  # E-002: 빈칸 남음
            if cell < CELL_MIN or cell > CELL_MAX:
                return BoundaryResult(False, "E-003")  # E-003: 범위 밖
            if cell in seen:
                return BoundaryResult(False, "E-004")  # E-004: 중복
            seen.add(cell)

    return BoundaryResult(True)


def check_complete(grid) -> BoundaryResult:
    result = validate_complete(grid)
    if result.status == ValidationStatus.INCOMPLETE:
        return BoundaryResult(False, "E-015")  # E-015: 빈칸 미채움
    if result.status == ValidationStatus.INVALID:
        if any("duplicate" in violation or "1..16" in violation for violation in result.violations):
            return BoundaryResult(False, "E-014")  # E-014: 1~16 중복/누락
        if any("row" in violation for violation in result.violations):
            return BoundaryResult(False, "E-011")  # E-011: 행 합 ≠ 34
        if any("col" in violation for violation in result.violations):
            return BoundaryResult(False, "E-012")  # E-012: 열 합 ≠ 34
        if any("diagonal" in violation for violation in result.violations):
            return BoundaryResult(False, "E-013")  # E-013: 대각선 합 ≠ 34
        return BoundaryResult(False, "E-011")
    return BoundaryResult(True)
