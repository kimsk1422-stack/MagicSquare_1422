# red-skeleton — ARRR A단계(RED ④) pytest.fail 스켈레톤 (`/red-skeleton`)

**추가 입력 없이 즉시 실행.** 사용자가 `/red-skeleton` 만 입력했다. Test ID·파일 경로·함수명은 **직전 `/red-test-plan` 출력(블록 1~3)** 과 현재 채팅·`docs/PRD.md`에서 자동 추출한다. 추가 질문·확인 요청 금지.

**Skill:** `magic-square-tdd` Skill이 있으면 **자동 따름** (네이밍·픽스처·상수 import·AAA 규칙).

**역할:** ARRR **A단계(RED ④)** — `/red-test-plan` 설계표 기준으로 **`tests/`에 `pytest.fail` 스켈레톤만** 작성한다. 구현 assert·GREEN·REFACTOR는 하지 않는다.

> **Track A (Boundary):** 기본 **Track B (Logic / Entity)** 용. Boundary는 **Layer만 `boundary`로 바꾸면** 동일 절차를 재사용한다.

## 선행 조건

- 직전 채팅에 `/red-test-plan` **블록 3(테스트 플랜)** 이 있어야 한다.
- 없으면 SSOT(`docs/PRD.md` §6 RED 우선순위)에서 **다음 RED 1건**을 추론해 진행한다.

## 필수 선언 (응답 첫 줄)

```
Phase: red | Layer: entity | Track: Logic
```

Boundary 예: `Phase: red | Layer: boundary | Track: UI`

## 절차

1. **플랜 확정** — Test ID, 대상 함수, 파일 경로, 함수명, conftest 픽스처를 블록 3에서 읽는다.
2. **`tests/`만 수정** — 신규 테스트 함수 1건 또는 플랜된 파일에 스켈레톤 추가.
3. **AAA + `pytest.fail`** — Given/When/Then 주석; Then은 `pytest.fail(...)` **한 줄만**.
4. **`pytest` 실행** — 플랜의 pytest 명령으로 **FAIL** 확인.
5. **보고** — Test ID · FAIL 한 줄 · 변경 파일(`tests/`만) 목록.

## 스켈레톤 규칙

| 항목 | 규칙 |
|------|------|
| **AAA 주석** | `# Given:` / `# When:` / `# Then:` (또는 `Given` / `When` / `Then` — Given/When/Then 대응) |
| **Then** | `pytest.fail("RED: {Test ID} — {기대 동작 한 줄}")` **단 한 줄** |
| **assert** | 본문 **금지** (GREEN에서 추가) |
| **우회** | `pytest.skip` · `xfail` · `assert True` · 통과 더미 **금지** |
| **상수** | `34` / `16` / `4` 리터럴 **금지** → `entity/constants.py`에서 import (픽스처 **격자 데이터**만 리터럴 허용) |
| **conftest** | `tests/conftest.py`의 `grid_g1` 사용 — **0 두 개**, row-major 4×4 |
| **계약 ID** | 모듈 docstring·테스트 주석에 `INV-*` 또는 `E-*` |
| **마커** | Entity: `pytestmark = pytest.mark.entity` |
| **`src/`** | **수정 금지** |

### 상수 import (예)

```python
from entity.constants import GRID_SIZE, MAGIC_CONSTANT, CELL_MAX
```

- 모듈 위치: `entity/constants.py` (프로젝트 레이아웃에 맞게 `tests/entity/constants.py` 등 — Skill·기존 트리 따름).
- 스켈레톤 RED 단계에서 파일이 없으면 **`tests/entity/constants.py`만** 최소 생성 가능 (`src/` 금지).

### conftest — `grid_g1`

- 파일: `tests/conftest.py`
- 픽스처명: `grid_g1`
- 내용: PRD §3.2 슬라이드 예시 — 빈칸(0) **정확히 2개**, row-major 4×4
- 없으면 RED ④에서 `tests/conftest.py`에 **픽스처만** 추가 (기존 루트 `conftest.py` import path 설정은 유지)

## 템플릿 예시

파일: `tests/entity/test_d_loc.py` (플랜의 경로·이름 우선)

```python
"""D-LOC: 빈칸 좌표·row-major 배치 (설계표 Test ID 참조)."""

import pytest

from entity.constants import GRID_SIZE

pytestmark = pytest.mark.entity


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given: grid_g1 — 4×4, 0이 정확히 2개, row-major
    blanks = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid_g1[r][c] == 0]

    # When: (스켈레톤 — 대상 함수 호출은 GREEN에서 연결)
    _ = blanks  # Arrange 검증만; Act는 플랜의 When에 맞게 주석으로 명시

    # Then: RED — 구현 전 의도적 실패
    pytest.fail("RED: D-LOC-01 — row-major 빈칸 좌표 2개를 반환해야 한다")
```

- 함수명·Test ID·fail 메시지는 **플랜 블록 1·3**에 맞게 치환한다.
- Given에서 `grid_g1`·상수만 사용; When은 주석으로 대상 함수를 명시해도 되고, 호출 줄을 넣되 **Then은 반드시 `pytest.fail` 한 줄**.

## 실행 명령어

플랜 블록 3의 경로 사용 (예):

```bash
pytest tests/entity/test_inv_complete_validation.py::test_<함수명> -v
```

또는:

```bash
pytest tests/entity/test_d_loc.py::test_d_loc_01_blank_coords_row_major -v
```

**기대:** `FAILED` — `pytest.fail` 메시지에 `RED: {Test ID}` 포함.

## 완료 보고 (응답 마지막)

한 줄 형식:

```
{Test ID} · FAILED: RED: {Test ID} — … · tests/entity/test_….py
```

이어서 변경 파일 목록 (`tests/`만):

```
- tests/conftest.py (grid_g1 추가 시)
- tests/entity/test_….py
```

## 금지사항

| 금지 | 이유 |
|------|------|
| `src/` 수정 | RED ④는 테스트 스켈레톤만 |
| GREEN / REFACTOR | 다음 단계 |
| `assert` 본문 (Then 제외) | GREEN에서 작성 |
| `pytest.skip` · `xfail` · `assert True` | RED 우회 |
| 한 사이클에 Test ID 여러 개 | 플랜 Rule2: To-Do 1개 |
| Domain Mock (Entity) | `red-test-plan` 블록 4 |
| 사용자에게 Test ID **추가 질문** | 플랜·채팅에서 자동 추출 |

## 이전 · 다음 Command

| Command | 역할 |
|---------|------|
| `/red-test-plan` | RED ③ — C2C 설계표·테스트 플랜 (파일 생성 없음) |
| `/tdd-red` | (레거시) `validate_lines` assert 기반 RED |
