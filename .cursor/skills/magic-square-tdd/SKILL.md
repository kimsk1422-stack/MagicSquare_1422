---
name: magic-square-tdd
description: >-
  MagicSquare Dual-Track TDD (ARRR · C2C · ECB). Guides RED/GREEN/REFACTOR
  phases, pytest.fail skeletons, golden masters, and safe refactor budgets.
  Use when Phase is red, green, or refactor; when running Commands
  /red-test-plan, /red-skeleton, /green-minimal, /golden-master,
  /refactor-smell, or /refactor-safe; or when the user mentions TDD, RED,
  GREEN, REFACTOR, Dual-Track, C2C, or pytest.fail.
disable-model-invocation: true
---

# magic-square-tdd

MagicSquare_1422 프로젝트 TDD 워크플로 Skill. **명시 호출·Command 실행 시에만** 적용한다.

**SSOT (항상 우선):**
- `.cursorrules` — 도메인·API·TDD 금지
- `docs/PRD.md` — SC·INV-* / E-* 계약·RED 우선순위·Entity API·ECB

**응답 언어:** 한국어.

---

## 1. ARRR ↔ TDD 매핑

| ARRR | TDD | 단계 | Command | 수정 범위 |
|------|-----|------|---------|-----------|
| **Ask** | RED | ③ 플랜 | `/red-test-plan` | 없음 (채팅만) |
| **Ask** | RED | ④ 스켈레톤 | `/red-skeleton` | `tests/` |
| **Respond** | GREEN | 최소 구현 | `/green-minimal` | `src/` + `tests/` (fail→assert) |
| **Respond** | GREEN | Golden Master | `/golden-master` | `tests/_approval.py`, `tests/golden/` |
| **Refine** | REFACTOR | ⑦ 스멜 탐지 | `/refactor-smell` | 없음 (읽기만) |
| **Refine** | REFACTOR | ⑧ Safe Refactor | `/refactor-safe` | `src/`·`tests/` (Budget 내) |

사이클: **RED → GREEN → REFACTOR**. 단계 건너뛰기·역행 금지.

---

## 2. Phase 선언 (응답 첫 줄)

| Phase | 형식 |
|-------|------|
| RED ③ | `Phase: red \| Layer: {entity\|boundary} \| Track: {Logic\|UI}` |
| RED ④ | 동일 |
| GREEN | `Phase: green \| Layer: entity \| Track: Logic` (Boundary: `boundary` / `UI`) |
| REFACTOR ⑦ | `Phase: refactor \| Scope: src/ tests/ \| Track: Logic+UI` |
| REFACTOR ⑧ | `Phase: refactor \| Layer: entity \| Track: Logic` |

소문자 `red` / `green` / `refactor` 사용 (Command 파일과 통일).

---

## 3. C2C Rule 1~3

Contract-to-Code: PRD 계약 ID → 테스트 → 구현 추적.

| Rule | 내용 |
|------|------|
| **Rule1** | PRD FR 인용 — `docs/PRD.md` §6에서 Test ID와 연결된 SC·INV/E 문장 **그대로** 인용 |
| **Rule2** | To-Do **1개** — 1 RED 사이클 = 1 Test ID = 1 테스트 케이스 |
| **Rule3** | Test ID + **Given / When / Then** — AAA 주석과 1:1 대응 |

구현 줄 주석: `# INV-00X: …` 또는 `# E-00X: …`

---

## 4. RED 절대 금지

| 금지 | 대안 |
|------|------|
| `src/` 수정 (③ 플랜) | `/green-minimal`까지 대기 |
| `pytest.skip` · `xfail` · `assert True` | `pytest.fail("RED: {Test ID} — …")` |
| assert 본문 (④ 스켈레톤) | Then은 `pytest.fail` 한 줄만 |
| **Logic Track Domain Mock** | 실제 격자·순수 함수; Entity 로직 mock 금지 |
| E-001~E-005 emit (Entity) | Boundary 책임 |
| 한 사이클 복수 Test ID | Rule2 위반 |

**RED 우선순위 (Entity):** INV-005 → INV-006 → INV-008 → INV-011  
**RED 우선순위 (Boundary):** E-002 → E-011 → E-014

---

## 5. GREEN 규칙

| 항목 | 규칙 |
|------|------|
| 범위 | **RED 1묶음**만 통과시키는 최소 구현 |
| 커밋 | **1커밋 = 1 RED 묶음** (사용자 요청 시만) |
| 상수 SSOT | `34`·`16`·`4` → `entity/constants.py` (`GRID_SIZE`, `MAGIC_CONSTANT`, `CELL_MAX`) |
| 테스트 | `pytest.fail` 제거 → assert 교체; AAA 유지 |
| ECB | Entity → boundary/control/Flask import **금지** |
| E-001~E-005 | Entity에서 raise/return으로 입력 거절 **금지** |

Entity API (`docs/PRD.md` §6.6): `magic_constant`, `validate_partial`, `line_sums`, `validate_complete`, `solve` — 모듈 `src/magic_square.py`.

---

## 6. REFACTOR 규칙

**전제:** `python -m pytest tests/ -v` 전부 PASS.

### Change Budget (1회)

| 항목 | 상한 |
|------|------|
| 파일 | ≤ 3 |
| 클래스 | ≤ 1 |
| 메서드 | ≤ 3 |

### Safe Refactor 원칙

- 입출력·예외·`int[6]` 1-index · `OK …` / `ERR {CODE}` 포맷 **변경 금지**
- 기능 추가·버그 수정 **금지** (별도 GREEN)
- **golden 유지:** `UPDATE_GOLDEN` 없이 matched 확인
- golden diff **의도적** → ISS 문서화 + `UPDATE_GOLDEN=1`
- golden diff **비의도적** → 롤백; golden 수동 편집 **금지**

### 스멜 우선순위

P0: ECB 위반, Magic Number · P1: Long Method, Duplicated Code, Feature Envy · P2: Mysterious Name

---

## 7. Track A (UI) vs Track B (Logic)

| | **Track B — Logic** | **Track A — UI** |
|---|---------------------|------------------|
| Layer | `entity` | `boundary` |
| Track 선언 | `Logic` | `UI` |
| 디렉터리 | `tests/entity/` | `tests/boundary/` |
| 계약 ID | **INV-*** | **E-*** |
| 마커 | `pytest.mark.entity` | `pytest.mark.boundary` |
| Domain Mock | **금지** | UI·I/O만 mock; Entity 로직 mock 금지 |
| E-001~E-005 | Entity RED/GREEN에서 emit **금지** | 검증 **대상** |
| Entity import | `src/magic_square.py` 등 | Entity 호출; Flask mock 가능 |

Boundary Command는 Layer만 `boundary` / Track `UI`로 바꿔 동일 체인 재사용.

---

## 8. Command 체인

```
/red-test-plan     → C2C 설계표·플랜 (파일 생성 없음)
       ↓
/red-skeleton      → pytest.fail 스켈레톤 (tests/만)
       ↓
/green-minimal     → src/ 최소 구현 + assert (1 RED 묶음)
       ↓
/golden-master     → tests/golden/{id}.approved.txt + assert_matches_golden
       ↓
/refactor-smell    → 스멜 탐지만 (수정 금지)
       ↓
/refactor-safe     → 후보 1건 Safe Refactor (Budget 내)
       ↓
/refactor-smell    → (반복)
```

완료 문구 (③): `/red-skeleton 으로 넘길 준비됐다`

---

## 9. pytest 명령 패턴

```bash
# 전체
python -m pytest tests/ -v
pytest -q

# 트랙
pytest tests/entity -q
pytest tests/boundary -q

# 단일 테스트 (RED/GREEN 1묶음)
pytest tests/entity/test_inv_magic_constant.py::test_magic_constant_for_4x4_is_34 -v

# 파일 회귀
pytest tests/entity/test_inv_magic_constant.py -v

# Golden — 기준 생성 (의도적 변경·ISS 후만)
UPDATE_GOLDEN=1 pytest tests/entity/test_inv_solver.py::test_inv_011_solve_slide_example -v

# Golden — matched 확인 (UPDATE_GOLDEN 없음)
pytest tests/ -k golden -v
```

**기대:** RED ④ → `FAILED` (`pytest.fail`); GREEN → `PASSED`; REFACTOR 후 → 전체 PASS + golden matched.

### Golden 직렬화 (고정)

- 성공: `OK r1 c1 v1 r2 c2 v2` — int[6], **1-index**
- 실패: `ERR {CODE}` — 예: `ERR INVALID:R2`, `ERR INCOMPLETE`, `ERR REJECTED:E002`

### conftest·픽스처

- 루트 `conftest.py` — import path
- `tests/conftest.py` — `grid_g1` (0 두 개, row-major 4×4, PRD §3.2)
- `tests/entity/conftest.py` — `partial_grid`, `solved_grid` 등

---

## 10. 완료 보고 형식

| 단계 | 한 줄 형식 |
|------|-----------|
| RED ③ | (플랜 표 4블록) + `/red-skeleton 으로 넘길 준비됐다` |
| RED ④ | `{Test ID} · FAILED: RED: {Test ID} — … · tests/entity/test_….py` |
| GREEN | `PASS {Test ID} · src/…, tests/…` |
| Golden | `{Test ID} · tests/golden/{id}.approved.txt · matched: yes · diff: —` |
| REFACTOR ⑦ | 스멜 표 + `P0 후보 중 1개만 골라 /refactor-safe 실행하세요. (권장: REF-001)` |
| REFACTOR ⑧ | `REF-001 · {요약} · pytest: N passed · golden matched: yes` |

변경 파일 목록은 단계별 허용 범위만 보고 (`tests/`만 / `src/`+`tests/`).

**git commit:** 사용자 명시 요청 시만. 예: `test(RED): INV-005` · `feat(GREEN): INV-005` · `refactor: REF-001`.

---

## 도메인 요약 (SSOT 발췌)

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 정수 배열 |
| 빈칸 | `0` (부분 문제: 정확히 2개) |
| 숫자 | 1~16 각 1회 |
| 마법 상수 | 34 |
| 10선 | R1~R4, C1~C4, D1, D2 |

```python
validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": [...]}
```

| status | 의미 |
|--------|------|
| `pass` | 10선 합 34 |
| `fail` | 완성이나 합 ≠ 34 |
| `incomplete` | 빈칸(0) 잔존 |

---

## ECB (구현 시)

| 계층 | 모듈 | import 금지 |
|------|------|-------------|
| Entity | `src/magic_square.py` | boundary, control, Flask |
| Boundary | (향후 `src/app.py`) | — |

구조적 변경과 동작적 변경을 **한 커밋에 섞지 않는다** (구조 먼저).

---

## Command 파일 위치

`.cursor/commands/` — `red-test-plan.md`, `red-skeleton.md`, `green-minimal.md`, `golden-master.md`, `refactor-smell.md`, `refactor-safe.md`

Command 실행 시 해당 `.md` 본문이 SSOT이며, 본 Skill과 충돌 시 **Command + PRD + .cursorrules** 순으로 따른다.
