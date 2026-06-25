---
name: magic-square-docs
description: >-
  MagicSquare session Report and Transcript export. Generates paired
  Report/NN.REPORT.md and Prompting/NN.Export-Transcript.md, updates README
  docs table, and documents ARRR cycle completion. Use for Report Export,
  Transcript, /export-session, Phase repeat, ARRR 1-cycle completion reports,
  or session N reports (세션 N 보고서).
disable-model-invocation: true
---

# magic-square-docs

MagicSquare_1422 **세션 문서화** Skill. Report·Transcript 쌍 생성·README 갱신.

**명시 호출·`/export`·`/export-session` 시에만** 적용.

> **Export 요청 시 magic-square-docs Skill 로드 후 [phase-checklist.md](phase-checklist.md) 수행.**

**SSOT 형식:**
- `Report/05.REPORT.md` (ARRR 1사이클 Report 목표 형식)
- `Prompting/05.Export-Transcript.md` (Transcript 목표 형식)
- 기존 실例: `Report/03.REPORT.md`, `Prompting/03.Export-Transcript.md`

**템플릿:**
- [report-template.md](report-template.md)
- [transcript-template.md](transcript-template.md)
- [phase-checklist.md](phase-checklist.md)

**응답 언어:** 한국어.

---

## 워크플로 개요

```
Step A 입력 수집 → Step B NN 결정 → Step C Report → Step D Transcript
    → Step E README 갱신 → Step F 완료 보고
```

---

## Step A — 입력 수집 (터미널 필수)

**추가 질문 없이** 채팅·터미널에서 수집. **실행하지 않은 명령 결과를 보고서에 쓰지 않는다.**

| 입력 | 수집 방법 |
|------|-----------|
| `git status` | 터미널 실행 — 실제 stdout |
| `pytest` | `python -m pytest tests/ -v` 실행 — 실제 stdout |
| **Phase** | 채팅 첫 줄·Command: `red` \| `green` \| `refactor` \| `repeat` |
| **Test ID** | `INV-*` · `E-*` · `REF-*` · Command 출력 |
| **Command** | `/red-test-plan` … `/refactor-safe` · `/export-session` |
| **세션 주제** | 대화 핵심 작업 한 줄 |

```bash
git status
python -m pytest tests/ -v
```

---

## Step B — 번호 NN

1. `Report/NN.REPORT.md` — 기존 `NN` 최대값
2. `Prompting/NN.Export-Transcript.md` — 기존 `NN` 최대값
3. **`NN = max(Report, Prompting) + 1`** — 2자리 (`04`, `05`, …)
4. 기존 번호 파일 **덮어쓰기 금지**

---

## Step C — Report

파일: `Report/NN.REPORT.md`  
템플릿: [report-template.md](report-template.md)

### 필수 구조

1. 제목 `# MagicSquare_1422 — {세션 주제}`
2. 메타 표 (프로젝트 · 단계 · 보고서 생성일 · 목적)
3. **§0 세션 메타** — Phase · Test ID · Command · git/pytest 실제 출력
4. **§1 요약**
5. **§2 Phase별 STEP** — 아래 해당 Phase 상세
6. **§3 핵심 결정·산출물**
7. **§4 다음 단계**
8. Transcript 링크 + footer

### Phase별 STEP (§2)

| Phase | STEP 기록 |
|-------|-----------|
| **RED** | ③ 플랜(C2C·Given/When/Then) · ④ 스켈레톤·FAIL |
| **GREEN** | 최소 구현·PASS · golden matched (해당 시) |
| **REFACTOR** | ⑦ 스멜·REF-NNN · ⑧ Safe·Budget |
| **repeat** | 완료 사이클 요약 · 다음 Test ID 1건 |

- 복수 Phase 세션: 각 STEP 짧게; **주 Phase 1개** 상세.
- 미진행 Phase: `N/A` 한 줄.

---

## Step D — Transcript

파일: `Prompting/NN.Export-Transcript.md`  
템플릿: [transcript-template.md](transcript-template.md)

### 필수 요소

- `_Exported on {YYYY-MM-DD} from Cursor_`
- `_Source: {uuid}_` — transcript ID; 없으면 `unknown` (임의 UUID 생성 금지)
- `## User` / `## Cursor` 교대 **전문**
- 마지막에 생성·변경 파일 표
- Report 링크 + footer

---

## Step E — README 문서 표 갱신

`README.md` § **문서** 표에 **행 추가** (기존 행 유지):

```markdown
| [Report/NN.REPORT.md](Report/NN.REPORT.md) | {세션 주제 한 줄} |
| [Prompting/NN.Export-Transcript.md](Prompting/NN.Export-Transcript.md) | {세션 주제} Transcript |
```

- 표만 갱신; README 다른 섹션 임의 수정 금지.

---

## Step F — 완료 보고

채팅에 짧게:

```
NN={NN} · {세션 주제 한 줄}
Report/NN.REPORT.md
Prompting/NN.Export-Transcript.md
```

---

## `/export-session` · `/export` 연동

`.cursor/commands/export.md` 실행 시:

1. **magic-square-docs Skill 로드**
2. [phase-checklist.md](phase-checklist.md) **전체** 수행
3. Step A→F 순서 준수
4. Report + Transcript **반드시 쌍** 생성

| Command | 별칭 |
|---------|------|
| `/export` | 세션 Export |
| `/export-session` | 동일 |

---

## ARRR 1사이클 완료 보고

`Phase: repeat` 또는 사용자가 「ARRR 1사이클 완료」 요청 시 §2에 **4 Phase 요약**:

| ARRR | TDD | 이번 사이클 기록 |
|------|-----|------------------|
| Ask | RED ③④ | Test ID · FAIL |
| Respond | GREEN | PASS · golden |
| Refine | REFACTOR ⑦⑧ | REF-NNN · matched |
| (다음) | repeat | 다음 Test ID |

---

## 금지

| 금지 | 이유 |
|------|------|
| **git commit** 임의 실행 | `.cursorrules` — 사용자 요청 시만 |
| **UPDATE_GOLDEN=1** 임의 실행 | golden 갱신은 GREEN/REFACTOR 의도적 절차만 |
| 채팅·터미널에 **없는** pytest 결과 기재 | 문서 신뢰 |
| Report만 / Transcript만 생성 | 쌍 필수 |
| 기존 `NN` 덮어쓰기 | 번호 규칙 |
| `MagicSquare_1004` 등 구 프로젝트명 | `MagicSquare_1422` 고정 |
| 사용자에게 주제·번호 **추가 질문** | 자동 추출 |

---

## Phase 선언 (Export 응답 첫 줄)

문서화 세션 자체가 TDD Phase가 아니면:

```
Phase: repeat | Scope: Report/ Prompting/ | Track: Docs
```

ARRR 사이클 직후 Export면 채팅의 마지막 TDD Phase를 메타에 기록.

---

## 관련 Skill · Command

| 리소스 | 역할 |
|--------|------|
| [magic-square-tdd](../magic-square-tdd/SKILL.md) | TDD Phase·Test ID·Command 체인 |
| `.cursor/commands/export.md` | Export Command SSOT |
| `docs/PRD.md` | Test ID·RED 우선순위 인용 |

---

## 빠른 체크 (Export 전)

```
[ ] Step A: git status + pytest 실행함
[ ] Step B: NN = max+1, 덮어쓰기 없음
[ ] Step C+D: Report·Transcript 쌍
[ ] Step E: README 표 2행 추가
[ ] Step F: 경로 2개 보고
[ ] 금지: commit · UPDATE_GOLDEN · 허위 pytest
```

상세: [phase-checklist.md](phase-checklist.md)
