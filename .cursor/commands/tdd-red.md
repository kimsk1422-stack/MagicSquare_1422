# tdd-red — validate_lines RED 단계 (`/tdd-red`)

`validate_lines` 로직 트랙 TDD **RED** 전용. 실패하는 테스트만 추가한다.

## 필수 선언 (응답 첫 줄)

```
Phase: red | Target: validate_lines | Track: logic
```

## 절차

1. **입력 `grid`와 기대 출력 확정** — `status`(`pass` | `fail` | `incomplete`)와 `failed_lines`를 명시한다.
2. **`tests/test_validate_lines.py`에 AAA 구조 테스트 추가** — Arrange / Act / Assert 주석으로 구분한다.
3. **`pytest`로 FAIL 확인** — 아래 명령으로 새 테스트가 실패하는지 검증한다.

## 실행 명령어

```bash
pytest tests/test_validate_lines.py -v
```

## 금지사항

- `src/` 수정 금지 (RED 단계는 `tests/` 만)
- assert 완화 금지 (`pytest.skip`, `xfail`, `assert True` 등 우회 금지)
- 한 번에 여러 케이스 진행 금지 (한 사이클 = 한 테스트 케이스)
