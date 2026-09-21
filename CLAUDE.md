# dotdot-skills — 스킬 관리 전용 폴더 (260920부터 이 폴더 세션이 스킬 전부를 관리)

Claude Code 플러그인/스킬 배포 채널(강의용 배포 통일 채널) + **한민님이 직접 만든 스킬의 관리 본부**.
다른 세션에서 스킬을 고치지 않는다 — 스킬 수정·검증·배포는 전부 여기서.

## 구조 — 원본과 배포본

| | 경로 | 역할 |
|---|---|---|
| **원본** | `~/.claude/skills/<스킬>/` | Claude Code가 실제로 읽는 곳. 여기가 현재 동작 |
| **배포본** | `plugins/<스킬>/skills/<스킬>/` (이 레포) | 마켓플레이스. 수강생이 설치하는 건 이쪽 |
| 플러그인 메타 | `plugins/<스킬>/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` | 버전·설명 |

- GitHub: `studiodotdot/dotdot-skills` (Public) — 구 `aible-edu/aible-skills`(260715 rename). 커밋에 Co-Author 트레일러 안 붙임(개인 프로젝트)
- 수강생 설치: `/plugin marketplace add studiodotdot/dotdot-skills` → `/plugin install <스킬>@dotdot-skills`
- **수정 절차: 원본 고침 → 검증 → `rsync -a --delete ~/.claude/skills/<스킬>/ plugins/<스킬>/skills/<스킬>/` → `plugins/<스킬>/.claude-plugin/plugin.json` 버전 bump(marketplace.json엔 버전 필드 없음) → README → 커밋·push(push는 한민님 확인)**
- 🚨 공개 레포다. 업체·고객·직장 실명, `/Users/hanmin` 개인 경로, 회사 자료가 SKILL.md·템플릿에 들어가면 안 된다. push 전 grep

## 보유 스킬

| 스킬 | 버전 | 용도 | 비고 |
|---|---|---|---|
| vanilla-slide | 1.3.1 | 강의 교안·교육자료 HTML 슬라이드 | F·I·N·S 4키 엔진 원본. `<body>` 직후 라인 아이콘 SVG 스프라이트 26종 동봉(`#i-…`) |
| vanilla-deck | 1.0.1 | 사내 보고·제안·공모전·IR 발표 덱 | vanilla-slide 엔진에서 노트(N)·발표자(S) 뺀 F·I 2키 파생. 흐름 3종 `references/flows.md` |
| edu-designer | 1.0.0 | ADDIE·딕앤케리·메릴 기반 커리큘럼 설계 | |
| (buildlog) | — | 제작 과정 빌드로그 | 개인용, 마켓 미등재 |

**엔진 공유 규칙**: 두 vanilla 템플릿의 `⛔ 엔진` 아래(전환 goTo·키 판별·목차·해시·`@page` 인쇄)는 같은 코드다. 공통부를 고치면 **양쪽 템플릿에 똑같이** 반영. 노트·발표자 모드를 deck에 되살리지 않는다(한민님 결정 260918).

## 디자인 근거 — 레퍼런스 이미지 라이브러리 (260919 Aside 수집)

`~/Downloads/레퍼런스_슬라이드_260919/` — 국내 PPT 디자인 업체 포트폴리오 원본 이미지 240장
(발표 15건 149장 / 교육 6건 91장, `01_슬라이드인덱스.csv` 유형 태그, `02_관찰노트.md`, `99_진행상황.txt`에 미완 목록).
- **두 스킬의 시각 레이어는 이 이미지를 보고 만들었다.** 부품을 고칠 땐 SKILL.md 개요에 적힌 레퍼런스 장(예: 3단 → `발표/01_*/04`)을 Read로 직접 보고 나란히 비교
- ⭐ 교훈(메모리 `feedback_mimic_from_images`): 글로 정리한 규칙(색 HSL·구조 서술)로 만든 판은 반려됐다. **실물 이미지를 보고 만들어야 통과.** 업체 색은 고객사 CI라 규칙화 대상이 아님
- 저작권: 개인 학습 참고용. 재배포·레포 포함 금지

## `_work/` (gitignore, 로컬 작업물)

- `samples/` — 현재 템플릿 그대로인 샘플 = `vanilla-deck_샘플_260921`(1.0.1) · `vanilla-slide_교육샘플_260921`(1.3.1). 260920 판 2개는 이전 버전 비교용
- `test-decks/` — 260919 실험: 서브에이전트가 **옛 템플릿**으로 만든 공모전·교육 제안서 덱 2개(가짜 수치)
- `backup/` — vanilla-deck 이전 판 2개(v1 글규칙판 · v2 챔피언 단색 시트형 — 회사 양식 1장 보고서엔 이게 맞을 수 있음)

## 검증 방법 (표준)

```bash
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$C" --headless=new --hide-scrollbars --window-size=1280,720 --virtual-time-budget=3000 --screenshot=sN.png "file://$PWD/덱.html#slide-N"
"$C" --headless=new --no-pdf-header-footer --virtual-time-budget=3000 --print-to-pdf=덱.pdf "file://$PWD/덱.html"   # 페이지 수 = 슬라이드 수
```
- 캡처를 Read로 직접 보고 레퍼런스와 비교. data-step 요소는 복사본에 `[data-step]{opacity:1!important;transform:none!important}` 넣어 확인
- 스킬 자체 테스트는 맥락 없는 서브에이전트에게 가짜 요청을 주고 "헷갈린 점"을 보고받는 방식이 효과적이었음(260919, 지적 20여 건 반영)

## 한민님 취향·결정 (되돌리지 말 것)

- 명조·손글씨 금지, Pretendard(jsdelivr) · 원문자 ①② 금지 · `word-break: keep-all`
- 채도 높은 형광색 금지("눈 아픔"). 색 조합을 내가 먼저 제안하지 않는다 — 레퍼런스나 지정 색에서 출발
- 산출물에 가정·검증 메모 금지, 결과만. 지어내지 않는다(수치·출처·실적 없으면 묻거나 `확인 필요`)
- 대용량 제작은 서브에이전트 병렬. 백그라운드 에이전트 10분 무응답이면 멈추고 확인

## 남은 작업
- [x] vanilla-slide v1.2.0 배포·push (260715) · edu-designer v1.0.0 등재 (260715) · 계정·레포 rename (260715)
- [x] vanilla-slide v1.3.0 교육 레이어 재작성 + vanilla-deck v1.0.0 신규 등재 · push (260920)
- [x] vanilla-deck 1.0.1 레이아웃 재점검 (260921) — 샘플 10장 전부 캡처해 레퍼런스(GC IR 02·04·10, 충남 02, SBA 02·03·07)와 나란히 비교. 목차 장식 2×4 타일 격자 재작성 · 카드 격자 자연 높이 + 결론 밴드 채움 · 60/40 표 글자 키우고 빈 `.visual` 대신 `.kpis--2` · 목표 장 `.goals__lead` 목표 문장 + 원형 배경 · 타임라인 이모지 흰 글리프 필터. 옛 실험 덱의 "표 사이즈" 문제(자연 높이·열 폭 쏠림)는 v1 템플릿 것 — 현 템플릿엔 `.split` stretch + `th nowrap`로 대응
- [ ] ▶ 한민님: 1.0.1 샘플(`_work/samples/vanilla-deck_샘플_260921.html`) 브라우저로 열어 확인 → OK면 push
- [x] vanilla-slide 1.3.1 아이콘·이미지 보강 (260921) — 교육 레퍼런스(67 표지·04 개념·21 마무리, 39 표지·마무리, 70 개념) 확인: 큰 슬롯은 일러스트가 꽉 차고 제목 아이콘은 노란 원 안 라인 아이콘. 템플릿에 직접 그린 라인 아이콘 SVG 스프라이트 26종 동봉 + `.ico`·`.pictos/.picto` 부품 추가, 샘플 이모지 전부 교체(표지·마무리는 픽토그램 3개가 하단 흰 띠 위에 서고, 개념 원은 아이콘 약 50%). SKILL.md에 "아이콘·일러스트" 절(우선순위 이미지>픽토그램>이모지, 슬롯별 규칙, unDraw·Open Peeps·Storyset·OpenMoji 소스와 라이선스 주의) 추가
- [ ] ▶ 한민님: 1.3.1 샘플(`_work/samples/vanilla-slide_교육샘플_260921.html`) 확인 → deck 1.0.1과 함께 push
- [ ] vanilla-deck 타임라인 라벨 아이콘도 이모지(필터 임시) → slide 스프라이트 방식으로 교체 (1.0.2)
- [ ] 레퍼런스 라이브러리 미완분 — 발표 10건 99장 태그 미부여, 나머지 55건 미수집(`99_진행상황.txt`). 필요해지면 Aside에 이어서 지시(지시문 `~/Downloads/Aside지시문_레퍼런스_슬라이드_수집_260919.txt`)
