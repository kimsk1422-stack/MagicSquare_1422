"""Boundary 계층 — Entity 호출·E-* emit (ECB)."""

from src.boundary.gate import check_complete, check_input
from src.boundary.input_handler import InputHandler, ValidationOutcome

__all__ = ["InputHandler", "ValidationOutcome", "check_complete", "check_input"]
