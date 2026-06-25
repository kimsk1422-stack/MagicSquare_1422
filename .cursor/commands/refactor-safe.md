# refactor-safe — ARRR R단계(Refine ⑧) Safe Refactor (`/refactor-safe`)

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-safe` 만 입력했다. 대상 스멜은 **직전 `/refactor-smell` 표에서 선택한 1건**(`REF-NNN`) 또는 채팅에 명시된 후보 1건에서 자동 추출한다. 추가 질문·확인 요청 금지.

**Skill:** `magic-square-tdd` Skill이 있으면 **자동 따름**.

**역할:** `/refactor-smell` 표에서 **선택한 스멜 1개만** Change Budget 내에서 안전 리팩터한다. **동작 변경·기능 추가는 하지 않는다.**

> **Track A (Boundary):** 기본 **Track B (Logic / Entity)** 용. Boundary는 **Layer만 `boundary`로 바꾸면** 동일 절차를 재사용한다.

## 선행 조건

- 직전 `/refactor-smell` **후보 1건**이 확정되어 있어야 한다 (`REF-NNN`).
- 리팩터 전 `python -m pytest tests/ -v` **전부 PASS**.
- 후보가 `over-budget`이면 **분할 후** 다시 `/refactor-smell`부터 진행.

## 필수 선언 (응답 첫 줄)

```
Phase: refactor | Layer: entity | Track: Logic
```

Boundary 예: `Phase: refactor | Layer: boundary | Track: UI`

## Safe Refactor 원칙

| 원칙 | 규칙 |
|------|------|
| **범위** | 선택한 **스멜 1건**·**후보 1건**만 처리 |
| **입출력** | 공개 API 시그니처·반환값·**관측 가능한 동작** 변경 **금지** |
| **예외** | raise/return 패턴·에러 의미 변경 **금지** |
| **직렬화** | `int[6]` **1-index** · `OK …` / `ERR {CODE}` 포맷 변경 **금지** |
| **E-001~E-005** | Entity 리팩터에서 입력 거절 **emit 금지** |
| **ECB** | Entity ↔ Boundary 의존 방향 악화 **금지** |
| **기능** | 새 기능·버그 수정 **금지** — 별도 **GREEN** 사이클 |
| **테스트** | assert 완화·삭제·`skip`·`xfail` **금지** |

## Change Budget (1회 리팩터 상한 — 반드시 준수)

| 항목 | 상한 |
|------|------|
| **파일** | ≤ 3 |
| **클래스** | ≤ 1 |
| **메서드** | ≤ 3 |

- 예산 초과 변경이 필요하면 **이번 실행에서 중단**하고 `/refactor-smell`에서 후보를 분할한다.

## 절차

1. **대상 확정** — `REF-NNN`, 스멜 유형, 파일·함수 범위를 `/refactor-smell` 표에서 읽는다.
2. **리팩터 실행** — 구조·이름·중복 제거·상수 추출 등 **동작 보존** 변경만 (`src/`·`tests/`).
3. **pytest** — `python -m pytest tests/ -v` 전부 PASS 확인.
4. **golden matched** — `UPDATE_GOLDEN` **없이** approval·golden 테스트 PASS 확인.
5. **golden diff 처리** — 아래 분기.
6. **보고** — 변경 요약 · pytest · golden matched.

## golden diff 처리

| diff 성격 | 조치 |
|-----------|------|
| **의도적** (리팩터로 출력 포맷·직렬화가 바뀌어야 함) | **ISS 문서화** (변경 사유·전후·계약 ID) → `UPDATE_GOLDEN=1 pytest …` 로 golden 재생성 → matched 재확인 |
| **비의도적** (동작 회귀·버그) | **즉시 롤백** — 리팩터 변경 되돌림 → pytest·golden 재확인 |

- golden **수동 편집**으로 matched 맞추기 **금지**.
- ISS 문서: 채팅 보고에 포함하거나 `Report/`·이슈에 기록 (사용자 요청 시).

### golden 확인 명령

```bash
pytest tests/ -v
```

approval 테스트만:

```bash
pytest tests/ -k golden -v
```

의도적 golden 갱신 (ISS 문서화 **후에만**):

```bash
UPDATE_GOLDEN=1 pytest tests/entity/test_inv_solver.py::test_inv_011_solve_slide_example -v
```

## 스멜별 허용 리팩터 (참고)

| 스멜 | 허용 예 |
|------|---------|
| Magic Number | `entity/constants.py` import로 치환 |
| Duplicated Code | private 헬퍼 추출 (메서드 ≤3) |
| Long Method | Extract Method (동작 동일) |
| Mysterious Name | rename (호출부·테스트 동시, Budget 내) |
| ECB 위반 | import 제거·계층 이동 (파일 ≤3) |
| Feature Envy | 메서드 이동 (클래스 ≤1) |

## 완료 보고 (응답 마지막)

| 항목 | 내용 |
|------|------|
| **REF-ID** | `REF-001` |
| **변경 요약** | 파일·함수·스멜 1~2문장 |
| **pytest** | `tests/ — N passed` |
| **golden matched** | `yes` / `no` (+ diff 한 줄) |

한 줄 형식:

```
REF-001 · Magic Number→constants import · pytest: 12 passed · golden matched: yes
```

- **git commit**: 사용자가 **명시적으로 요청할 때만**. 메시지 예: `refactor: REF-001 Magic Number in validate_lines`.

## 금지사항

| 금지 | 이유 |
|------|------|
| 스멜 **2건 이상** 동시 리팩터 | 1실행 = 1후보 |
| Change Budget 초과 | 안전 리팩터 |
| 기능 추가·버그 수정 | GREEN 담당 |
| 입출력·예외·`int[6]` 포맷 변경 | Safe Refactor 위반 |
| golden 수동 편집 | Approval Test 신뢰 |
| 요청 없는 **git commit** | `.cursorrules` |

## 이전 · 다음 Command

| Command | 역할 |
|---------|------|
| `/refactor-smell` | Refine ⑦ — 스멜 탐지 (선행) |
| `/refactor-safe` | **Refine ⑧** — 후보 1건 안전 리팩터 (본 Command) |
| `/refactor-smell` | 추가 스멜 있으면 ⑦ 반복 |
