"""Entity 계층 — Boundary/Control import 금지 (ECB)."""

from src.entity.loc import find_blank_coords
from src.entity.sol import SolveResult, solve

__all__ = ["find_blank_coords", "SolveResult", "solve"]
