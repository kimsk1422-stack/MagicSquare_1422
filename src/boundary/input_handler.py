"""InputHandler — UI 격자 → check_input → validate_lines (Boundary, Qt 없음)."""

from dataclasses import dataclass

from src.boundary.gate import BoundaryResult, check_filled_input, check_input
from src.entity.constants import BLANK_CELL, CELL_MAX, CELL_MIN, GRID_SIZE
from src.validate_lines import validate_lines


@dataclass(frozen=True)
class ValidationOutcome:
    accepted: bool
    code: str | None = None
    status: str | None = None
    failed_lines: tuple[str, ...] = ()


class InputHandler:
    def parse_cell(self, text: str) -> int:
        stripped = text.strip()
        if stripped == "" or stripped == "0":
            return BLANK_CELL
        value = int(stripped)
        if value < CELL_MIN or value > CELL_MAX:
            raise ValueError(f"out of range: {value}")
        return value

    def cells_to_grid(self, raw_cells: list[list[str]]) -> list[list[int]]:
        if len(raw_cells) != GRID_SIZE or any(len(row) != GRID_SIZE for row in raw_cells):
            raise ValueError("grid must be 4x4")
        return [[self.parse_cell(raw_cells[row][col]) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]

    def _gate_for_grid(self, grid: list[list[int]]) -> BoundaryResult:
        blank_count = sum(cell == BLANK_CELL for row in grid for cell in row)
        if blank_count == 0:
            return check_filled_input(grid)  # 완성 격자: E-002 생략
        if blank_count == 2:
            return check_input(grid)  # 부분 격자: 빈칸 2개 전제
        return BoundaryResult(False, "E-002")  # E-002: 빈칸 ≠ 2개

    def validate(self, grid: list[list[int]]) -> ValidationOutcome:
        gate = self._gate_for_grid(grid)  # E-001~005: 입력 전제 검사
        if not gate.accepted:
            return ValidationOutcome(accepted=False, code=gate.code)
        result = validate_lines(grid)  # 10선 pass/fail/incomplete
        return ValidationOutcome(
            accepted=True,
            status=result["status"],
            failed_lines=tuple(result["failed_lines"]),
        )
