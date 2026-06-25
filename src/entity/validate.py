"""격자 검증 — INV-001~009."""

from dataclasses import dataclass
from enum import Enum

from src.entity.constants import BLANK_CELL, CELL_MAX, CELL_MIN, GRID_SIZE, MAGIC_CONSTANT
from src.entity.lines import line_sums


class ValidationStatus(Enum):
    ACCEPTABLE_PARTIAL = "acceptable_partial"
    VALID = "valid"
    INVALID = "invalid"
    INCOMPLETE = "incomplete"


@dataclass(frozen=True)
class ValidationResult:
    status: ValidationStatus
    violations: tuple[str, ...] = ()


def magic_constant(size=GRID_SIZE):
    return size * (size * size + 1) // 2  # INV-005: (1+…+n²)/n


def validate_partial(grid):
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return ValidationResult(ValidationStatus.INVALID, ("not 4x4",))  # INV-001

    seen = set()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = grid[row][col]
            if value == BLANK_CELL:
                continue
            if value < CELL_MIN or value > CELL_MAX:
                return ValidationResult(ValidationStatus.INVALID, ("out of range",))  # INV-003
            if value in seen:
                return ValidationResult(ValidationStatus.INVALID, ("duplicate",))  # INV-004
            seen.add(value)

    return ValidationResult(ValidationStatus.ACCEPTABLE_PARTIAL, ())


def validate_complete(grid):
    if any(grid[row][col] == BLANK_CELL for row in range(GRID_SIZE) for col in range(GRID_SIZE)):
        return ValidationResult(ValidationStatus.INCOMPLETE, ("blank cells remain",))

    violations = []
    sums = line_sums(grid)
    for row in range(GRID_SIZE):
        if sums[row] != MAGIC_CONSTANT:
            violations.append(f"row {row} sum != {MAGIC_CONSTANT}")  # INV-006

    for col in range(GRID_SIZE):
        if sums[GRID_SIZE + col] != MAGIC_CONSTANT:
            violations.append(f"col {col} sum != {MAGIC_CONSTANT}")

    if sums[GRID_SIZE * 2] != MAGIC_CONSTANT:
        violations.append(f"diagonal D1 sum != {MAGIC_CONSTANT}")

    if sums[GRID_SIZE * 2 + 1] != MAGIC_CONSTANT:
        violations.append(f"diagonal D2 sum != {MAGIC_CONSTANT}")

    flat = [grid[row][col] for row in range(GRID_SIZE) for col in range(GRID_SIZE)]
    if sorted(flat) != list(range(CELL_MIN, CELL_MAX + 1)):
        violations.append("duplicate or missing values in 1..16")  # INV-007

    if violations:
        return ValidationResult(ValidationStatus.INVALID, tuple(violations))
    return ValidationResult(ValidationStatus.VALID, ())
