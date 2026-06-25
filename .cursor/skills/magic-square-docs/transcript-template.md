# Transcript Template — `Prompting/NN.Export-Transcript.md`

SSOT 참고: `Prompting/03.Export-Transcript.md` · 목표 형식: `Prompting/05.Export-Transcript.md`.

`NN` = Report와 **동일 번호**. `{…}` 는 Export 시 치환.

---

```markdown
# MagicSquare_1422 — Session Export Transcript

_Exported on {YYYY-MM-DD} from Cursor_

_Source: {uuid}_

---

## User

{User 메시지 전문 — 첫 턴}

---

## Cursor

{Cursor 응답 전문 — 첫 턴}

---

## User

{다음 User 턴}

---

## Cursor

{다음 Cursor 턴}

---

{… 채팅 끝까지 User/Cursor 교대 · 요약 금지 …}

---

## User

/export

또는

/export-session

---

## Cursor

{Export 생성 응답 전문}

---

## 생성·변경 파일 목록

| 파일 | 작업 |
|------|------|
| `Report/{NN}.REPORT.md` | 신규 |
| `Prompting/{NN}.Export-Transcript.md` | 신규 |
| `{기타 세션 산출물}` | {신규\|수정} |

관련 보고서: [Report/{NN}.REPORT.md](../Report/{NN}.REPORT.md)

*본 문서는 Prompting/{NN}.Export-Transcript.md — {세션 주제} 세션 Export입니다.*
```

---

## 작성 규칙

| 항목 | 규칙 |
|------|------|
| **_Exported on** | Export 실행일 `YYYY-MM-DD` |
| **_Source uuid** | agent transcript UUID (`agent-transcripts/{uuid}.jsonl`); 없으면 `unknown` |
| **턴 구분** | `## User` / `## Cursor` + `---` |
| **전문** | 요약·생략 금지; 코드·표는 원문 유지 |
| **마지막 User** | `/export` 또는 `/export-session` 턴 포함 |
| **파일 표** | Report·Transcript + 세션에서 실제 생성·수정된 경로만 |
| **쌍 번호** | Report `NN` = Transcript `NN` |

## _Source uuid 확보

1. 현재 채팅이 agent transcript에 저장된 경우 해당 `{uuid}` 사용.
2. 사용자가 transcript 경로를 준 경우 파일명에서 추출.
3. 확보 불가 시 `_Source: unknown_` — **임의 UUID 생성 금지**.
