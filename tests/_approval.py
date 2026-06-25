"""Golden Master approval helpers."""

import os
from pathlib import Path

from src.entity.constants import COORD_INDEX_ORIGIN
from src.entity.sol import SolveResult


def format_solve_result(result: SolveResult) -> str:
    parts = ["OK"]
    for row, col, value in result.filled:
        parts.append(str(row + COORD_INDEX_ORIGIN))
        parts.append(str(col + COORD_INDEX_ORIGIN))
        parts.append(str(value))
    return " ".join(parts)


def assert_matches_golden(
    *,
    test_id: str,
    actual: str,
    golden_dir: Path | None = None,
) -> None:
    root = golden_dir or Path(__file__).parent / "golden"
    golden_path = root / f"{test_id}.approved.txt"
    actual_stripped = actual.strip()

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual_stripped + "\n", encoding="utf-8")
        return

    if not golden_path.is_file():
        raise AssertionError(f"golden missing: {golden_path}")

    expected = golden_path.read_text(encoding="utf-8").strip()
    if expected != actual_stripped:
        raise AssertionError(
            f"golden mismatch for {test_id}:\n-expected: {expected}\n+actual: {actual_stripped}"
        )
