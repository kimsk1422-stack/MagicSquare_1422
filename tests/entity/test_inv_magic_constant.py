"""INV-005: 4×4·1~16 마방jin 목표 합(마법 상수)."""

import pytest

from src.magic_square import magic_constant

pytestmark = pytest.mark.entity


def test_magic_constant_for_4x4_is_34():
    # INV-005: (1+…+16)/4 = 34
    assert magic_constant(size=4) == 34
