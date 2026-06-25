from src.validate_lines import validate_lines


def test_t2_fail_r2_c2_sum_35():
  # T2: 완성 격자에서 (2,2)=6 → 7, R2·C2 합 35
  # Arrange
  grid = [
    [1, 15, 14, 4],
    [12, 7, 7, 9],
    [8, 10, 11, 5],
    [13, 3, 2, 16],
  ]
  # Act
  result = validate_lines(grid)
  # Assert
  assert result["status"] == "fail"
  assert "R2" in result["failed_lines"]
  assert "C2" in result["failed_lines"]
