"""ResultDisplay — validate_lines 결과 표시 (Boundary)."""

import json

from flask import render_template_string

_RESULT_TEMPLATE = """
<div id="result" data-status="{{ status }}" data-failed-lines='{{ failed_lines_json }}'>
  <p>status: {{ status }}</p>
  <p>failed_lines: {{ failed_lines_text }}</p>
</div>
"""


class ResultDisplay:
    def render(self, result: dict) -> str:
        status = result["status"]
        failed_lines = result["failed_lines"]
        return render_template_string(
            _RESULT_TEMPLATE,
            status=status,
            failed_lines_json=json.dumps(failed_lines),
            failed_lines_text=json.dumps(failed_lines),
        )  # U-VAL-01: status·failed_lines 표시 · E-017 → E-015
