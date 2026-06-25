"""U-VAL-01: [검증] 클릭 → validate_lines 결과 표시 (E-017 → E-015)."""

from unittest.mock import patch

import pytest

pytestmark = pytest.mark.boundary


def test_u_val_01_validate_shows_incomplete_status(client_with_g1, grid_g1):
    # Given: grid_g1 로드된 UI
    expected = {"status": "incomplete", "failed_lines": []}
    _ = grid_g1

    # When: [검증] 버튼 클릭
    with patch("src.app.validate_lines", return_value=expected):
        response = client_with_g1.post("/validate")

    # Then: status=incomplete, failed_lines=[] 표시
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert 'data-status="incomplete"' in body
    assert "failed_lines: []" in body  # U-VAL-01
