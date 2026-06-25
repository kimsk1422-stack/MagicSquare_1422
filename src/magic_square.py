"""Entity API — PRD §6.6 (Boundary import 금지)."""

from src.entity.sol import SolveResult, solve
from src.entity.validate import (
    ValidationResult,
    ValidationStatus,
    line_sums,
    magic_constant,
    validate_complete,
    validate_partial,
)

__all__ = [
    "SolveResult",
    "ValidationResult",
    "ValidationStatus",
    "line_sums",
    "magic_constant",
    "solve",
    "validate_complete",
    "validate_partial",
]
