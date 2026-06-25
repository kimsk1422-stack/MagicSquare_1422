"""D-SOL-01: G1 슬라이드 step A 풀이 성공 (INV-011)."""

import pytest

from src.entity.sol import solve
from tests._approval import assert_matches_golden, format_solve_result

pytestmark = pytest.mark.entity


def test_d_sol_01_step_a_success(grid_g1):
    # Given: G1 격자 (0이 2개, PRD §3.2)
    # When: solve(grid_g1) 호출
    result = solve(grid_g1)

    # Then: OK 2 4 8 3 3 7 (1-index, golden)
    actual = format_solve_result(result)
    assert_matches_golden(test_id="d_sol_01_g1_step_a", actual=actual)
