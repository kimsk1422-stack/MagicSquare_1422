# Report Template — `Report/NN.REPORT.md`

SSOT 참고: `Report/03.REPORT.md` · 목표 형식: `Report/05.REPORT.md` (ARRR 1사이클).

`NN` = 2자리. `{…}` 는 Export 시 치환.

---

```markdown
# MagicSquare_1422 — {세션 주제}

| 항목 | 내용 |
|------|------|
| **프로젝트** | MagicSquare_1422 |
| **단계** | {Phase 요약 — 예: ARRR RED ④ INV-006 · GREEN · REFACTOR ⑧} |
| **보고서 생성일** | {YYYY-MM-DD} |
| **목적** | {이번 Export가 답하는 질문 1문장} |

## 0. 세션 메타 (Step A)

| 항목 | 값 |
|------|-----|
| **Phase** | `{red \| green \| refactor \| repeat}` |
| **Test ID** | `{INV-00X \| E-00X \| REF-00X \| —}` |
| **Command** | `{/red-test-plan \| /green-minimal \| …}` |
| **Track** | `{Logic \| UI \| Logic+UI}` |

### git status (실행 결과)

```
{Step A git status 실제 출력}
```

### pytest (실행 결과)

```
{Step A python -m pytest tests/ -v 실제 출력 요약 — passed/failed 수·실패 테스트명}
```

## 1. 요약

{3~5문장: 무엇을 했고, 현재 TDD/ARRR 상태가 어디인지}

## 2. Phase별 STEP

> 해당 Phase만 **상세** 기록. 미해당 Phase는 `N/A` 한 줄.

### RED (`Phase: red` — 해당 시)

| STEP | 내용 |
|------|------|
| **RED-③ 플랜** | {C2C Rule1 FR 인용 · Test ID · Given/When/Then} |
| **RED-④ 스켈레톤** | {파일 · pytest.fail 메시지 · FAIL 확인} |

### GREEN (`Phase: green` — 해당 시)

| STEP | 내용 |
|------|------|
| **GREEN** | {src/ 최소 구현 · PASS Test ID · 변경 파일} |
| **Golden** | {golden 경로 · matched yes/no — 해당 시만} |

### REFACTOR (`Phase: refactor` — 해당 시)

| STEP | 내용 |
|------|------|
| **⑦ 스멜** | {P0/P1 · 스멜 유형 · REF-NNN 후보} |
| **⑧ Safe** | {변경 요약 · Budget 준수 · golden matched} |

### REPEAT (`Phase: repeat` — 해당 시)

| STEP | 내용 |
|------|------|
| **완료 사이클** | {Test ID · 최종 pytest 상태} |
| **다음 RED** | {PRD 우선순위 다음 1건} |

## 3. 핵심 결정·산출물

### 산출물

| 파일 | 작업 | 비고 |
|------|------|------|
| `{path}` | {신규\|수정} | {Test ID / Command} |

### pytest 스냅샷 (Step A와 동일 출처)

| 항목 | 값 |
|------|-----|
| 명령 | `python -m pytest tests/ -v` |
| 결과 | `{N passed, M failed}` |
| 비고 | {대상 테스트·RED/GREEN 상태} |

## 4. 다음 단계

1. {다음 Command 또는 Test ID 1건}
2. {블로커 있으면 1건}

관련 Transcript: [Prompting/{NN}.Export-Transcript.md](../Prompting/{NN}.Export-Transcript.md)

*본 문서는 Report/{NN}.REPORT.md — {세션 주제} 세션 보고서입니다.*
```

---

## 작성 규칙

- 프로젝트명은 **`MagicSquare_1422`** (1004 등 구번호 사용 금지).
- pytest·git 출력은 **Step A 터미널 실제 결과**만 — 추정·과거 세션 복붙 금지.
- Phase 섹션 2에서 **이번 세션 Phase 1개**를 주로 상세화; 복수 Phase 세션이면 각각 짧게.
