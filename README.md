# MagicSquare_1422

4×4 **부분 마방진**(빈칸 2개, 1~16, 10선 합 34)을 다루는 Python 학습 프로젝트.  
Mom Test로 발견한 **진짜 문제**(조합·노가다·불확신)를 **검증 가능한 불변식(INV-*)** 으로 고정하고, **Dual-Track TDD**(RED → GREEN → REFACTOR)로 구현한다.

## 진짜 문제 (한 문장)

마방진을 손으로 풀 때 빈칸·숫자 조합을 경우의 수처럼 맞춰야 해서 시간과 노력이 커지고, 답을 찾아도 ‘노가다로 맞춘 것’이라 정답과 풀이에 대한 확신이 생기지 않는다.

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (중복 없음) |
| 10선 | 4행 + 4열 + 2대각선, 각 합 **34** |
| 입력 | 14칸 고정, **2칸은 0(빈칸)** |

## 구조 (ECB)

```
src/           Entity — 순수 로직 (Boundary import 금지)
tests/entity/  불변식 INV-*
tests/boundary/ 입력·UI 계약 E-*, UC-*
```

| 계층 | 이번 범위 |
|------|-----------|
| Entity + Test Loop | ✅ |
| Boundary UI | ❌ (표면 문제 — PRD 참고) |

## 요구사항

상세 PRD: [docs/PRD.md](docs/PRD.md)

- Mom Test 증거 · R-G-I-O · 성공 기준 SC-1~3
- 표면 문제(하지 않을 것) · ECB 개념 분류

## 개발 환경

- Python 3.12+
- pytest

```bash
pip install pytest
```

## 테스트

```bash
pytest -q                  # 전체
pytest tests/entity -q     # Entity (INV-*)
pytest tests/boundary -q   # Boundary (E-*, UC-*)
```

## 워크플로

1. **RED** — `tests/` 에 실패 테스트 추가 (계약 ID 명시)
2. **GREEN** — `src/` 최소 구현 (구현 줄에 INV-/E- 주석)
3. **REFACTOR** — `pytest -q` 통과 유지하며 구조 정리

자세한 규칙: [AGENTS.md](AGENTS.md) · `.cursor/rules/dual-track-tdd.mdc`

## 문서

| 파일 | 설명 |
|------|------|
| [docs/PRD.md](docs/PRD.md) | 제품 요구사항 (Mom Test 기반 초안) |
| [Report/01.REPORT.md](Report/01.REPORT.md) | 세션 1 보고서 |
| [Prompting/01.Export-Transcript.md](Prompting/01.Export-Transcript.md) | Mom Test Transcript |

## 라이선스

(미정)
