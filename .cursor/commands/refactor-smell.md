# refactor-smell — ARRR R단계(Refine ⑦) 코드 스멜 탐지 (`/refactor-smell`)

**추가 입력 없이 즉시 실행.** 사용자가 `/refactor-smell` 만 입력했다. 분석 범위는 **`src/`·`tests/`** 현재 트리 전체. 추가 질문·확인 요청 금지.

**Skill:** `magic-square-tdd` Skill이 있으면 **자동 따름**.

**역할:** ARRR **R단계(Refine = ⑦)** — 코드 스멜을 **탐지·분류만** 한다. **수정·commit 금지.**

> 본 Command는 **읽기 전용 분석**이다. 리팩터 실행은 `/refactor-safe`가 담당한다.

## 필수 선언 (응답 첫 줄)

```
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

## 전제 (미충족 시 즉시 중단)

```bash
python -m pytest tests/ -v
```

- **전부 PASS**여야 한다. 하나라도 FAIL이면 스멜 분석을 **시작하지 않는다**.
- 중단 보고: 실패 테스트 목록만 출력하고 종료.

## 절차

1. **pytest 전체 PASS 확인** — 위 명령 실행.
2. **`src/`·`tests/` 정적 분석** — 아래 스멜 유형으로 후보 수집.
3. **우선순위 부여** — P0 / P1 / P2.
4. **Change Budget 검토** — 각 후보가 예산 내에서 안전하게 다뤄질 수 있는지 표기.
5. **출력** — 스멜 표 + `/refactor-safe`에 넘길 후보 **1~3개**.
6. **다음 안내** — P0 **1개만** 골라 `/refactor-safe` 실행하라고 안내.

## 스멜 유형 · 우선순위

| 우선순위 | 스멜 | 탐지 기준 |
|----------|------|-----------|
| **P0** | **ECB 위반** | Entity가 Boundary/Control/Flask import; Boundary가 도메인 로직 중복; 계층 역방향 의존 |
| **P0** | **Magic Number** | `34`·`16`·`4` 등이 `entity/constants.py` 밖 리터럴로 반복 |
| **P1** | **Long Method** | 한 함수가 25줄 초과 또는 다중 책임(검증+풀이+직렬화 혼재) |
| **P1** | **Duplicated Code** | 동일·유사 로직 2곳 이상(10선 합산, 빈칸 탐색, 선 ID 생성 등) |
| **P1** | **Feature Envy** | 한 클래스/모듈이 타 계층 데이터를 과도하게 조작 |
| **P2** | **Mysterious Name** | `x`, `tmp`, `do_it`, 축약만으로 의도 불명; 계약 ID·도메인 용어 미사용 |

- 한 항목에 복수 스멜이면 **가장 높은 우선순위**로 분류.
- P0가 없으면 P1에서 후보를 고른다.

## Change Budget (리팩터 1회 상한 — `/refactor-safe`에 전달)

| 항목 | 상한 |
|------|------|
| **파일** | ≤ 3 |
| **클래스** | ≤ 1 |
| **메서드** | ≤ 3 |

- 후보가 예산을 **초과**하면 표에 `over-budget` 표기하고 `/refactor-safe` 후보에서 제외하거나 분할 제안.

## 출력 형식

### 1. 스멜 표

| P | 스멜 | 위치 (파일:줄) | 요약 | Budget OK? |
|---|------|----------------|------|------------|
| P0 | ECB 위반 | `src/magic_square.py:12` | … | yes / over-budget |

- 위치는 **구체적** (파일·함수·가능하면 줄 번호).
- `src/`·`tests/` 모두 대상.

### 2. `/refactor-safe` 후보 (1~3개)

| # | 후보 ID | P | 스멜 | 범위 | 예상 변경 |
|---|---------|---|------|------|-----------|
| 1 | `REF-001` | P0 | Magic Number | `src/validate_lines.py` | 상수 import로 치환 |

- 후보 ID는 `REF-NNN` 형식 (세션 내 연번).
- **1~3개**만 제시; P0 우선.

### 3. 다음 안내 (응답 마지막)

```
P0 후보 중 1개만 골라 /refactor-safe 실행하세요. (권장: REF-001)
```

- P0가 없으면: `P1 후보 중 1개만 골라 /refactor-safe 실행하세요.`
- **코드 수정·commit은 이 단계에서 하지 않습니다.**

## 금지사항

| 금지 | 이유 |
|------|------|
| **`src/`·`tests/` 코드 수정** | Refine ⑦은 탐지만 |
| **git commit** | `/refactor-safe` 이후·사용자 요청 시 |
| pytest FAIL 상태에서 분석 진행 | 전제 위반 |
| 스멜 후보 4개 이상 동시 제안 | Change Budget·안전 리팩터 원칙 |
| assert 완화 · 테스트 삭제로 PASS 맞추기 | 우회 금지 |

## 이전 · 다음 Command

| Command | 역할 |
|---------|------|
| `/green-minimal` | GREEN — 최소 구현 |
| `/golden-master` | Golden Master 구축·검증 |
| `/refactor-smell` | **Refine ⑦** — 스멜 탐지 (본 Command) |
| `/refactor-safe` | Refine ⑧ — 후보 1건 안전 리팩터 (예산 내) |
