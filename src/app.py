"""Boundary Flask 앱 — GridUI · ResultDisplay 진입점."""

from flask import Flask, render_template_string

from src.boundary.grid_ui import GridUI
from src.boundary.grids import g1_grid
from src.boundary.result_display import ResultDisplay
from src.validate_lines import validate_lines

_PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<body>
{{ grid_html | safe }}
<form action="/validate" method="post">
  <button type="submit">검증</button>
</form>
{{ result_html | safe }}
</body>
</html>
"""


def create_app(initial_grid=None, validate_fn=None):
    app = Flask(__name__)
    grid_ui = GridUI()
    result_display = ResultDisplay()
    app.config["GRID"] = initial_grid if initial_grid is not None else g1_grid()
    app.config["VALIDATE_FN"] = validate_fn

    @app.get("/")
    def index():
        grid = app.config["GRID"]
        return render_template_string(
            _PAGE_TEMPLATE,
            grid_html=grid_ui.render(grid),
            result_html="",
        )

    @app.post("/validate")
    def validate_route():
        grid = app.config["GRID"]
        fn = app.config.get("VALIDATE_FN") or validate_lines
        result = fn(grid)  # U-VAL-01 · E-017: 미완성 검증 → incomplete
        return render_template_string(
            _PAGE_TEMPLATE,
            grid_html=grid_ui.render(grid),
            result_html=result_display.render(result),
        )

    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
