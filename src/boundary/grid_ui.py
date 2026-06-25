"""GridUI — 4×4 격자 시각화 (Boundary)."""

from flask import render_template_string

from src.entity.constants import GRID_SIZE

_GRID_TEMPLATE = """
<table id="grid">
{% for row in grid %}
<tr>
{% for cell in row %}
<td data-cell="{{ cell }}">{{ cell }}</td>
{% endfor %}
</tr>
{% endfor %}
</table>
"""


class GridUI:
    def render(self, grid) -> str:
        if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
            raise ValueError("grid must be 4x4")  # U-GRID-01: 4×4 격자 표시
        return render_template_string(_GRID_TEMPLATE, grid=grid)
