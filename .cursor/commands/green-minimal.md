# green-minimal — ARRR R단계(Respond=GREEN) 최소 구현 (`/green-minimal`)

**추가 입력 없이 즉시 실행.** 사용자가 `/green-minimal` 만 입력했다. Test ID·대상 함수·파일 경로는 **직전 RED 묶음**(`/red-skeleton`·`pytest.fail` 스켈레톤)과 현재 채팅·`docs/PRD.md`에서 자동 추출한다. 추가 질문·확인 요청 금지.

**Skill:** `magic-square-tdd` Skill이 있으면 **자동 따름**.

**역할:** ARRR **R단계(Respond = GREEN)** — **RED 1묶음당** `src/` 최소 구현으로 해당 테스트만 통과시킨다. **1커밋 = 1 RED 묶음** (커밋은 사용자 요청 시만).

> **Track A (Boundary):** 기본 **Track B (Logic / Entity)** 용. Boundary는 **Layer만 `boundary`로 바꾸면** 동일 절차를 재사용한다.

## SSOT (읽기 전용)

| 문서 | 용도 |
|------|------|
| `docs/PRD.md` §6.6 | Entity API · 계약 ID 매핑 |
| `.cursorrules` | 도메인·TDD 금지 |
| `entity/constants.py` | `GRID_SIZE`·`MAGIC_CONSTANT`·`CELL_MAX` 등 **상수 SSOT** |

## 필수 선언 (응답 첫 줄)

```
Phase: green | Layer: entity | Track: Logic
```

Boundary 예: `Phase: green | Layer: boundary | Track: UI`

## 절차

1. **RED 재확인** — 대상 테스트가 `pytest.fail("RED: {Test ID} — …")` 로 **FAIL**인지 실행한다. 이미 PASS면 스킵·우회하지 말고 원인을 보고한다.
2. **`src/` 최소 구현** — 이번 RED 묶음의 Test ID **1건**만 만족하는 코드만 추가·수정한다. 구현 줄에 계약 ID 주석 (`# INV-00X: …`).
3. **테스트 GREEN화** — `pytest.fail` 제거 → 플랜·스켈레톤의 Then에 맞는 **assert**로 교체. AAA 주석 유지.
4. **PASS 확인** — 단일 테스트 PASS 후, 해당 파일·관련 entity 트랙 회귀 없음 확인 (`pytest -q`).
5. **보고** — PASS Test ID · 변경 파일 · 회귀 실패 시 즉시 수정 후 재보고.

## 구현 규칙

| 항목 | 규칙 |
|------|------|
| **범위** | 이번 RED 묶음 Test ID **1건**만 해결 |
| **최소성** | 통과에 필요한 최소 코드·분기만 |
| **상수** | `34` / `16` / `4` 등 **매직넘버·하드코딩 금지** → `entity/constants.py` import |
| **계약 주석** | `src/` 구현 줄에 `# INV-*` 또는 `# E-*` |
| **E-001~E-005** | Entity GREEN에서 **raise/return으로 입력 거절 처리 금지** (Boundary 책임) |
| **ECB** | Entity(`src/magic_square.py` 등)는 **boundary·control·Flask import 금지** |
| **테스트** | 이번 묶음 외 기존 테스트 **수정·삭제·완화 금지** |

### assert 교체 예

```python
# Before (RED ④)
pytest.fail("RED: INV-005 — magic_constant(4)는 34를 반환해야 한다")

# After (GREEN)
result = magic_constant(size=GRID_SIZE)
assert result == MAGIC_CONSTANT  # INV-005
```

## 실행 명령어

**단일 테스트** (이번 RED 묶음):

```bash
pytest tests/entity/test_inv_magic_constant.py::test_magic_constant_for_4x4_is_34 -v
```

**파일 전체** (같은 파일 회귀 확인):

```bash
pytest tests/entity/test_inv_magic_constant.py -v
```

회귀·전체 확인:

```bash
pytest tests/entity -q
```

**기대:** 대상 테스트 `PASSED`; 기존 테스트 회귀 없음.

## 완료 보고 (응답 마지막)

한 줄 형식:

```
PASS {Test ID} · src/magic_square.py, tests/entity/test_….py
```

- **회귀 실패** 시: 즉시 수정 → 재실행 → 수정 내용을 보고에 포함.
- **git commit**: 사용자가 **명시적으로 요청할 때만** 수행. 메시지 예: `feat(GREEN): INV-005`.

## 금지사항

| 금지 | 이유 |
|------|------|
| 이번 RED 묶음 **외** Test ID 동시 해결 | 1사이클 = 1묶음 |
| REFACTOR (구조 정리·이름 변경·추출) | GREEN 이후 별도 단계 |
| assert 완화 · `skip` · `xfail` · `assert True` | 우회 금지 |
| 매직넘버·하드코딩 | `constants.py` SSOT |
| Entity에서 E-001~E-005 emit | ECB·트랙 분리 |
| Entity → boundary/control import | ECB |
| 요청 없는 **git commit** | `.cursorrules` |
| 사용자에게 Test ID **추가 질문** | RED 묶음·채팅에서 자동 추출 |

## 이전 · 다음 Command

| Command | 역할 |
|---------|------|
| `/red-test-plan` | RED ③ — C2C 설계표·테스트 플랜 |
| `/red-skeleton` | RED ④ — `pytest.fail` 스켈레톤 |
| `/green-minimal` | **GREEN** — 최소 구현 (본 Command) |
| REFACTOR | 별도 지시 — 전부 PASS 후 구조 정리 |
