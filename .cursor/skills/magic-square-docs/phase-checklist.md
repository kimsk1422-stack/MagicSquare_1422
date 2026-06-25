# Phase Checklist — magic-square-docs

Export 전·후 확인용. **실행한 항목만** `[x]` 표기.

## Step A — 입력 수집

- [ ] `git status` 실행 (실제 출력 확보)
- [ ] `python -m pytest tests/ -v` 실행 (실제 출력 확보)
- [ ] 채팅에서 **Phase** 추출 (`red` | `green` | `refactor` | `repeat`)
- [ ] 채팅에서 **Test ID** 추출 (`INV-*` | `E-*` | `REF-*` | 없음)
- [ ] 채팅에서 **Command** 추출 (`/red-test-plan` … `/export-session` 등)
- [ ] 세션 주제 한 줄 확정

## Step B — 번호 (NN)

- [ ] `Report/NN.REPORT.md` 목록에서 max NN 확인
- [ ] `Prompting/NN.Export-Transcript.md` 목록에서 max NN 확인
- [ ] `NN = max + 1` (2자리: `04`, `05`, …)
- [ ] 기존 NN 파일 **덮어쓰기 안 함** 확인

## Step C — Report

- [ ] [report-template.md](report-template.md) 기반 작성
- [ ] 제목: `# MagicSquare_1422 — {세션 주제}`
- [ ] 메타 표 4행 (프로젝트·단계·보고서 생성일·목적)
- [ ] **Phase별 STEP** 섹션 포함 (해당 Phase만 상세, 나머지 요약 또는 N/A)
- [ ] pytest 결과 = **Step A 실제 출력**만 기재
- [ ] git status = **Step A 실제 출력**만 기재
- [ ] Transcript 링크 + footer 줄

## Step D — Transcript

- [ ] [transcript-template.md](transcript-template.md) 기반 작성
- [ ] `_Exported on {YYYY-MM-DD} from Cursor_`
- [ ] `_Source: {uuid}_` (채팅·agent transcript ID, 없으면 `unknown`)
- [ ] **User** / **Cursor** 턴 전문 (요약 금지)
- [ ] 생성·변경 파일 표 + Report 링크 + footer 줄

## Step E — README

- [ ] `README.md` §문서 표에 `Report/NN.REPORT.md` 행 추가
- [ ] `README.md` §문서 표에 `Prompting/NN.Export-Transcript.md` 행 추가
- [ ] 기존 행 삭제·덮어쓰기 없이 **추가만**

## Step F — 완료 보고

- [ ] `Report/NN.REPORT.md` 경로
- [ ] `Prompting/NN.Export-Transcript.md` 경로
- [ ] 세션 주제 한 줄

---

## Phase별 STEP — Report에 넣을 내용

### RED (`Phase: red`)

| STEP | 기록 항목 |
|------|-----------|
| RED-③ | C2C Rule1~3 · Test ID · Given/When/Then (플랜) |
| RED-④ | 스켈레톤 파일 · `pytest.fail` 메시지 · FAIL 출력 |
| Command | `/red-test-plan` → `/red-skeleton` |

### GREEN (`Phase: green`)

| STEP | 기록 항목 |
|------|-----------|
| GREEN | `src/` 변경 요약 · assert 교체 · PASS Test ID |
| Golden | `tests/golden/{id}.approved.txt` · matched (해당 시) |
| Command | `/green-minimal` · `/golden-master` |

### REFACTOR (`Phase: refactor`)

| STEP | 기록 항목 |
|------|-----------|
| ⑦ | 스멜 표 · `REF-NNN` 후보 |
| ⑧ | Safe Refactor 요약 · Budget · golden matched |
| Command | `/refactor-smell` → `/refactor-safe` |

### REPEAT (`Phase: repeat`)

| STEP | 기록 항목 |
|------|-----------|
| 완료 사이클 | 이번 사이클 Test ID · PASS/FAIL 최종 상태 |
| 다음 | PRD RED 우선순위 다음 Test ID 1건 |
| 회고 | 1~2문장 (블로커·학습) |

---

## 금지 (체크리스트 하단)

- [ ] **git commit** 임의 실행 안 함
- [ ] **UPDATE_GOLDEN=1** 임의 실행 안 함 (Export는 기록만)
- [ ] 채팅·터미널에 **없는** pytest 결과 기재 안 함
- [ ] Report만 / Transcript만 생성 안 함 (반드시 쌍)
