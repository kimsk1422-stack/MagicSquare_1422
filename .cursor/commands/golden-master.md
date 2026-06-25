# golden-master — GREEN PASS 후 Golden Master 구축·검증 (`/golden-master`)

**추가 입력 없이 즉시 실행.** 사용자가 `/golden-master` 만 입력했다. Test ID·대상 테스트는 **직전 GREEN PASS**(`/green-minimal`)와 현재 채팅·`docs/PRD.md`에서 자동 추출한다. 추가 질문·확인 요청 금지.

**Skill:** `magic-square-tdd` Skill이 있으면 **자동 따름**.

**역할:** **GREEN PASS 후** Golden Master(Approval Test)를 구축·검증한다. 구현 회귀 시 golden diff로 탐지한다.

> **Track A (Boundary):** 기본 **Track B (Logic / Entity)** 용. Boundary는 **Layer만 `boundary`로 바꾸면** 동일 절차를 재사용한다.

## 전제

- 대상 **Test ID**의 pytest가 이미 **PASS** 상태여야 한다.
- PASS가 아니면 `/green-minimal`을 먼저 수행한다. golden 수동 편집·assert 완화로 우회 **금지**.

## 필수 선언 (응답 첫 줄)

```
Phase: green | Layer: entity | Track: Logic
```

Boundary 예: `Phase: green | Layer: boundary | Track: UI`

## 절차

1. **`tests/_approval.py`** — `assert_matches_golden` 헬퍼가 없으면 생성한다.
2. **golden 연결** — 대상 Test ID에 `tests/golden/{id}.approved.txt`를 연결한다 (`{id}` = 소문자·언더스코어, 예: `inv_005`, `e_011`).
3. **기준 파일 생성** — `UPDATE_GOLDEN=1`로 pytest를 실행해 현재 **정상 출력**을 golden에 기록한다.
4. **matched 확인** — `UPDATE_GOLDEN` **없이** 동일 테스트를 재실행해 golden과 **일치**함을 확인한다.

## `assert_matches_golden` 계약

파일: `tests/_approval.py`

| 항목 | 규칙 |
|------|------|
| 시그니처 | `assert_matches_golden(*, test_id: str, actual: str, golden_dir: Path \| None = None) -> None` |
| golden 경로 | `tests/golden/{test_id}.approved.txt` (기본) |
| `UPDATE_GOLDEN=1` | golden 파일을 `actual` 내용으로 **덮어쓰기** 후 통과 |
| `UPDATE_GOLDEN` 없음 | `actual.strip()` vs golden 파일 **완전 일치**; 불일치 시 diff와 함께 `AssertionError` |
| 수동 편집 | golden 파일을 손으로 고쳐 통과시키기 **금지** — 반드시 `UPDATE_GOLDEN=1`로 재생성 |

### 출력 직렬화 포맷 (고정)

모든 golden 한 줄은 아래 중 **하나**만 허용한다.

**성공 — `int[6]` 1-index (빈칸 2곳 좌표·값):**

```
OK r1 c1 v1 r2 c2 v2
```

- 6개 정수, **1-indexed** `(row, col)` — PRD §3.2 슬라이드 좌표계.
- 예: `OK 2 4 8 3 3 7` → (2,4)=8, (3,3)=7

**실패·판정 불가 — 에러 코드 문자열:**

```
ERR {CODE}
```

| CODE | 의미 |
|------|------|
| `INVALID:R1` … `INVALID:R4` | 행 합 ≠ 34 |
| `INVALID:C1` … `INVALID:C4` | 열 합 ≠ 34 |
| `INVALID:D1` · `INVALID:D2` | 대각선 합 ≠ 34 |
| `INVALID:DUPLICATE` | 1~16 중복/누락 |
| `INCOMPLETE` | 빈칸(0) 잔존 — 판정 불가 |
| `REJECTED:E001` … `REJECTED:E005` | Boundary 입력 거절 (Track A만) |

- 공백·대소문자·콜론 위치 **고정**. 임의 접두사·추가 필드 **금지**.

### 테스트 연결 예

```python
from tests._approval import assert_matches_golden, format_solve_result

def test_inv_011_solve_slide_example(grid_g1):
    result = solve(grid_g1)
    actual = format_solve_result(result)  # "OK …" 또는 "ERR …"
    assert_matches_golden(test_id="inv_011", actual=actual)
```

- `format_solve_result`는 `_approval.py`에 두거나 대상 모듈에서 import — **직렬화는 위 포맷만** 사용.

## 실행 명령어

**3. 기준 파일 생성** (`UPDATE_GOLDEN=1`):

```bash
UPDATE_GOLDEN=1 pytest tests/entity/test_inv_solver.py::test_inv_011_solve_slide_example -v
```

**4. matched 확인** (`UPDATE_GOLDEN` 없음):

```bash
pytest tests/entity/test_inv_solver.py::test_inv_011_solve_slide_example -v
```

파일 전체 회귀:

```bash
pytest tests/entity/test_inv_solver.py -q
```

**기대:** ④에서 `PASSED`; golden과 `actual` **matched**.

## 완료 보고 (응답 마지막)

| 항목 | 내용 |
|------|------|
| **golden 경로** | `tests/golden/{id}.approved.txt` |
| **matched** | `yes` / `no` |
| **diff 요약** | 불일치 시 `-expected` / `+actual` 한 줄씩; 일치 시 `—` |

한 줄 형식:

```
{Test ID} · tests/golden/inv_011.approved.txt · matched: yes · diff: —
```

또는 불일치:

```
{Test ID} · tests/golden/inv_011.approved.txt · matched: no · diff: -OK 2 4 8 3 3 7 / +OK 2 4 8 3 3 8
```

## 금지사항

| 금지 | 이유 |
|------|------|
| golden `.approved.txt` **수동 편집**으로 통과 | Approval Test 신뢰 붕괴 |
| `UPDATE_GOLDEN=1` 없이 golden 최초 생성 | 절차 3 생략 |
| 직렬화 포맷 임의 변경 | `int[6]` 1-index · `ERR {CODE}` 고정 |
| PASS 전 golden 구축 | 전제 위반 |
| assert 완화 · `skip` · `xfail` | 우회 금지 |
| 요청 없는 **git commit** | `.cursorrules` |

## 이전 · 다음 Command

| Command | 역할 |
|---------|------|
| `/green-minimal` | GREEN — 최소 구현 (선행) |
| `/golden-master` | **Golden Master** 구축·검증 (본 Command) |
| REFACTOR | 별도 지시 — golden matched 유지하며 구조 정리 |
