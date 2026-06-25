# red-test-plan — ARRR A단계(Ask=RED ③) C2C 설계표·테스트 플랜 (`/red-test-plan`)

**추가 입력 없이 즉시 실행.** 사용자가 `/red-test-plan` 만 입력했다. 세션 주제·Test ID·대상 함수는 **현재 채팅·`docs/PRD.md`·`.cursorrules`** 에서 자동 추출한다. 추가 질문·확인 요청 금지.

**역할:** ARRR **A단계(Ask = RED ③)** — C2C 설계표와 테스트 플랜만 **채팅에 출력**한다. `tests/`·`src/` 파일은 **생성·수정하지 않는다.**

> **Track A (Boundary):** 본 Command는 기본 **Track B (Logic / Entity)** 용이다. Boundary(UI) 트랙은 **Layer만 `boundary`로 바꾸면** 동일 절차·출력 형식을 그대로 재사용한다.

## SSOT (읽기 전용)

| 문서 | 용도 |
|------|------|
| `.cursorrules` | 도메인(4×4·0·1~16·34·10선), `validate_lines` API, TDD 금지 |
| `docs/PRD.md` | FR·SC·INV-* / E-* 계약, RED 우선순위, Entity API, ECB 분류 |
| `AGENTS.md` | ECB 구조, `tests/entity/` · `tests/boundary/` 트랙 분리 |

## 자동 추출 (사용자에게 묻지 말 것)

- **세션 주제**: 이번 대화의 핵심 작업 (예: INV-006 RED, E-011 RED)
- **Layer**: Entity → `entity` / Boundary → `boundary` (대화·PRD §6 기준)
- **Track**: Entity → `Logic` / Boundary → `UI`
- **Test ID**: 다음 RED 1건 — PRD §6.2·§6.3 **RED 우선순위**에서 아직 플랜되지 않은 첫 계약
- **대상 함수**: PRD §6.6 Entity API 또는 Boundary 진입점
- **Invariant / E 계약**: 해당 Test ID의 검증 내용

## 필수 선언 (응답 첫 줄)

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

예 (Entity): `Phase: red | Layer: entity | Track: Logic`  
예 (Boundary): `Phase: red | Layer: boundary | Track: UI`

## 절차

1. SSOT에서 **다음 RED 1건**의 계약 ID·FR·대상 함수를 확정한다.
2. 아래 **출력 4블록**을 표 형식으로 채팅에 작성한다 (파일 생성 없음).
3. ECB·Mock 점검을 수행하고 위반 시 플랜을 수정한다.
4. 마지막 줄에 완료 문구를 출력한다.

---

## 출력 4블록 (표 형식 — 채팅 본문에만 작성)

### 블록 1 — C2C (Rule1~3)

| Rule | 내용 |
|------|------|
| **Rule1** | PRD FR 인용 — `docs/PRD.md`에서 해당 Test ID와 연결된 SC·INV/E·§6 문장을 **그대로 인용** |
| **Rule2** | To-Do **1개** — 이번 RED 사이클에서 검증할 단일 행동 (한 테스트 = 한 케이스) |
| **Rule3** | Test ID + **Given / When / Then** — Arrange·Act·Assert에 대응 |

출력 예시 골격:

| 항목 | 값 |
|------|-----|
| Test ID | `INV-00X` 또는 `E-00X` |
| Rule1 (PRD FR) | «PRD §… 인용» |
| Rule2 (To-Do) | «한 줄» |
| Given | «입력 격자·전제» |
| When | «호출 함수·인자» |
| Then | «기대 결과·assert 요지» |

### 블록 2 — Track 표

| Test ID | 대상 함수 | Given → Then | Invariant / E | Expected RED Failure |
|---------|-----------|--------------|---------------|----------------------|
| … | … | … | … | `ImportError` / `AttributeError` / assert 실패 메시지 요지 |

- **Expected RED Failure**: 아직 `src/`에 구현이 없거나 동작이 틀릴 때 pytest가 내야 할 **실패 유형** (우회 금지).

### 블록 3 — 테스트 플랜

| 항목 | 값 |
|------|-----|
| **파일 경로** | Entity: `tests/entity/test_inv_*.py` / Boundary: `tests/boundary/test_e_*.py` |
| **함수명** | `test_<계약_요지>_…` (pytest 규칙, AAA 주석 예정) |
| **conftest 픽스처** | 루트 `conftest.py` + 트랙 `tests/{entity\|boundary}/conftest.py` 에서 쓸 픽스처명 (예: `partial_grid`, `solved_grid`) |
| **pytest 명령** | `pytest tests/entity/test_inv_….py -v` 또는 `pytest tests/boundary/… -v` |
| **RED 묶음 범위** | 이번 사이클에 포함할 테스트 1건 ID; 같은 파일 내 기존 통과 테스트와 분리 여부 |

### 블록 4 — ECB·Mock 점검

| 점검 | Logic Track (Entity) | UI Track (Boundary) |
|------|----------------------|---------------------|
| Entity import | `src/magic_square.py` 등 Entity만 | Boundary는 Entity를 호출, Flask 등은 mock 가능 |
| Domain Mock | **금지** — 실제 격자·순수 함수로 검증 | UI·I/O만 mock; Entity 로직 mock 금지 |
| E-001~E-005 | Entity RED에서 **emit 금지** (입력 거절은 Boundary 책임) | E-001~E-005 **검증 대상**일 때만 해당 |
| Boundary in Entity | Entity 테스트가 `app`/Flask import **금지** | — |
| 계약 ID | 테스트 docstring·주석에 `INV-*` | 테스트 docstring·주석에 `E-*` |

위 표를 채우고, **위반 항목이 있으면 플랜을 수정**한 뒤 재출력한다.

---

## 완료 (응답 마지막 줄)

```
/red-skeleton 으로 넘길 준비됐다
```

---

## 금지사항

| 금지 | 이유 |
|------|------|
| `src/` 수정 | RED ③은 설계·플랜만; 구현은 GREEN |
| GREEN / REFACTOR 단계 진행 | A단계 범위 밖 |
| `pytest.skip` · `xfail` · `assert True` | RED 우회 |
| `tests/` · `src/` **파일 생성·수정** | 다음 단계 `/red-skeleton` 담당 |
| 한 사이클에 Test ID 여러 개 | Rule2: To-Do 1개 |
| 사용자에게 세션 주제·Test ID **추가 질문** | SSOT·채팅에서 자동 추출 |

## 다음 Command

| Command | 역할 |
|---------|------|
| `/red-skeleton` | 블록 3 플랜대로 `tests/` 에 실패 테스트 골격 작성 (RED ④) |
| `/tdd-red` | (레거시) `validate_lines` 단일 파일 RED |
