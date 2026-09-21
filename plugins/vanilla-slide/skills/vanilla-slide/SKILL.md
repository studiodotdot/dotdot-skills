---
name: vanilla-slide
description: |
  강의 교안·교육자료를 순수 HTML/CSS/JavaScript(라이브러리 없음) 단일 파일 웹 슬라이드로 만드는 스킬.
  동봉된 완성형 엔진 템플릿(assets/template.html) 기반 — 방향키/스와이프 전환(translateX),
  F 전체화면 · I 목차 오버레이 · N 화자 노트 · S 발표자 모드(듀얼 창 동기화, 타이머, 다음 슬라이드 미리보기),
  진행바·카운터, data-step 빌드 효과, URL 해시 동기화, 인쇄(PDF 전 장 저장) 대응.
  교육자료 설계 규칙(니모닉 목차·빈칸 채우기·정리 슬라이드·금지 예시·활동지·챕터별 색 코딩) 부품 동봉.
  핵심 절차는 "보여줄 그림 먼저" — 부품을 고르기 전에 장마다 메시지를 그림으로 번역한 한 줄을 적고, 메시지 유형별 그림 사전으로 시각 앵커를 정한다.
  10장 넘는 덱은 전 장 제작 전 톤 시안 2~3개 비교, 같은 그림 유형 3장 연속 금지, "글을 가리고 봐도 메시지가 보이나" 검수.

  다음 요청에 반드시 사용:
  - "교안 만들어줘", "강의 슬라이드", "교육자료 HTML로", "워크숍 자료", "강의용 웹 PPT"
  - 교육·강의용 자료를 HTML 파일 하나로 내보내달라는 요청
  - PPT/Google Slides 없이 브라우저에서 바로 강의하고 싶다는 요청
  - 기존 vanilla-slide 산출물을 기반으로 새 교안을 만들어달라는 요청
  경계: 사내 보고·제안서·공모전·IR 같은 발표자료 덱은 vanilla-deck 스킬 대상이다.
  (.pptx 등 실제 오피스 파일을 요구하는 경우는 이 스킬 대상이 아님)
---

# Vanilla Slide 스킬

## 개요

단일 `.html` 파일로 완성되는 풀-스크린 웹 교안을 만든다.
**교육용**이다 — 학습자가 나중에 혼자 다시 보는 자료. 발표자료(보고·제안·공모전)는 `vanilla-deck`을 쓴다.
외부 라이브러리 없이 CSS `translateX` 전환 + 키보드·터치 입력으로 동작한다.

**표준 4키 = F(전체화면) · I(목차) · N(화자 노트) · S(발표자 모드).** 어떤 덱에서도 이 4가지가 빠지면 안 된다.

## 파일 생성 절차 — 템플릿 우선

검증된 엔진 완성본이 `assets/template.html`(이 스킬 폴더 기준)에 동봉되어 있다.
엔진 코드를 매번 다시 작성하면 미세 버그가 재발하므로, **반드시 템플릿을 복사한 뒤 콘텐츠만 교체한다.**
템플릿에 실린 파스텔 종이 카드 스타일은 **기본값이지 정답이 아니다** — 톤은 아래 "교육자료 설계 규칙 → 제작 절차"의 시안 단계에서 사용자가 고른다.

1. **콘텐츠 설계 + 장별 시각 아이디어** — 요청/자료에서 슬라이드 수, 각 장의 제목·내용을 뽑고, **장마다 "이 메시지를 어떤 그림으로 보여줄지" 한 줄**을 먼저 적는다(아래 "보여줄 그림 먼저"). 재료(캡처·이미지·표)가 있으면 어느 장에 쓸지 이때 배정
2. **톤 시안 → `assets/template.html` 읽기** → 새 파일로 복사. 10장 넘는 덱은 전 장을 만들기 전에 같은 장면 3장으로 톤 시안 2~3개를 만들어 고르게 한다
3. **슬라이드 영역만 교체** — `✏️ 슬라이드 영역` 주석 블록 안의 `<section>`들만 수정.
   `⛔ 엔진` 주석 아래(UI 마크업 + JS)와 엔진 CSS는 건드리지 않는다.
   - 각 `<section class="slide">`에 `id="slide-N"`(1부터 순번)과 `data-title="목차용 제목"` 부여
   - 화자 노트는 `<aside class="notes">...</aside>` (레이블 불필요, 엔진이 붙임).
     **노트는 실제 발표 대본 수준으로 상세하게** 쓴다 — 여는 멘트(따옴표로 실제 문장) →
     강조 포인트 → 다음 슬라이드 전환 멘트, `<br>`로 구분한 2~4문장. 발표자 모드에서 그대로 읽으며
     진행할 수 있는 수준이 기준이다 (템플릿 샘플 노트가 이 형식)
   - 순차 등장 요소에 `data-step="1"`, `"2"`, ...
   - 콘텐츠 강조용 보조 스타일(경고 콜아웃, 하이라이트 등)은 슬라이드 영역 안에서
     인라인 style이나 새 클래스로 자유롭게 추가한다 — 금지 대상은 엔진 CSS/JS와
     `:root` 토큰·기존 컴포넌트 규칙의 **수정**이지, 콘텐츠 스타일 추가가 아니다
4. **문서 정보 교체** — `<title>`, 타이틀 슬라이드 내용. 팔레트 변경 요청 시 `:root` 변수만 교체
5. **체크리스트 검증** (아래 섹션) 후 저장
   - 파일명: `{주제}_슬라이드_{YYMMDD}.html` (산출물 날짜 규칙), 위치는 지정 없으면 현재 작업 디렉토리

템플릿 파일을 읽을 수 없는 환경에서만 아래 엔진 스펙대로 직접 구현한다.

---

## 핵심 구조 원칙 (엔진 스펙)

### 레이아웃: fixed + inset:0 (스케일 방식 금지)

각 `.slide`는 `position: fixed; inset: 0`으로 뷰포트 전체를 점유한다.
`scale()` + 1920×1080 고정 캔버스 방식은 **사용하지 않는다** — 반응형이 깨지고 텍스트가 흐려진다.

```css
.slide {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  background: var(--bg);                /* 불투명 필수 — 전환 정리 중인 뒷슬라이드 가림 */
  transform: translateX(100%);          /* 기본: 오른쪽 대기 */
  transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  will-change: transform;
}
.slide.is-active  { transform: translateX(0); }
.slide.exit-left  { transform: translateX(-100%); }
.slide.exit-right { transform: translateX(100%); }
body.is-animating { pointer-events: none; }  /* 전환 중 클릭 차단 */
```

콘텐츠는 `.slide__content` (`max-width: 1280px`, 중앙 정렬, 슬라이드 padding `0 60px`)에 담는다.

### 전환 함수 goTo(): reflow 강제 + 유령 방지 + 워치독

```javascript
var TRANSITION_MS = 500;   // .slide transition-duration과 일치시킬 것

function goTo(nextIndex, direction) {
  if (isAnimating || nextIndex === current) return;
  if (nextIndex < 0 || nextIndex >= total) return;

  isAnimating = true;
  document.body.classList.add('is-animating');

  var prevSlide = slides[current];
  var nextSlide = slides[nextIndex];
  var goingNext = direction === 'next';

  // 1. transition 없이 시작 위치 배치
  nextSlide.style.transition = 'none';
  nextSlide.classList.remove('is-active', 'exit-left', 'exit-right');
  nextSlide.style.transform = goingNext ? 'translateX(100%)' : 'translateX(-100%)';

  // 2. 강제 reflow — 이 줄이 없으면 transition이 무시되어 순간이동 버그 발생
  nextSlide.getBoundingClientRect();

  // 3. transition 복원
  nextSlide.style.transition = '';
  nextSlide.style.transform = '';

  // 4. 동시 이동 (뒤로 진입하는 슬라이드는 스텝 전부 표시)
  prevSlide.classList.remove('is-active');
  prevSlide.classList.add(goingNext ? 'exit-left' : 'exit-right');
  resetSteps(nextSlide, !goingNext);
  nextSlide.classList.add('is-active');

  current = nextIndex;
  updateUI();

  // 5. 정리 — prev의 transition을 잠시 꺼야 유령 슬라이드(화면 가로지르는 잔상)가 안 생긴다.
  //    transitionend는 유실될 수 있으므로(탭 숨김·전환 취소) 워치독 타이머로 이중 보장.
  var finished = false;
  function finish() {
    if (finished) return;
    finished = true;
    prevSlide.style.transition = 'none';
    prevSlide.classList.remove('exit-left', 'exit-right');
    prevSlide.getBoundingClientRect();
    prevSlide.style.transition = '';
    document.body.classList.remove('is-animating');
    isAnimating = false;
    nextSlide.removeEventListener('transitionend', handler);
  }
  function handler(e) {
    if (e.target !== nextSlide || e.propertyName !== 'transform') return;
    finish();
  }
  nextSlide.addEventListener('transitionend', handler);
  setTimeout(finish, TRANSITION_MS + 150);
}
```

### 키 입력은 e.code로 판별

`e.key`는 한글 입력 상태에서 `'ㄹ'`, `'ㅑ'` 등을 반환해 단축키가 죽는다.
반드시 `e.code`(`'KeyF'`, `'KeyI'`, `'KeyN'`, `'ArrowRight'`, `'Space'` 등)로 판별한다 — 한/영 전환과 무관하게 동작.

---

## 디자인 토큰 (엔진 기본값 · 교육 레이어는 `--edu-*` `--ch1~4` 별도)

```css
:root {
  --bg:             #F0F2F5;
  --surface:        #FFFFFF;
  --border:         #E2E8F0;
  --text-primary:   #1A2332;
  --text-secondary: #4A5568;
  --text-muted:     #94A3B8;
  --accent:         #4A8FDB;
  --accent-light:   #BFDBF7;
  --accent-dark:    #2563EB;
  --point:          #F59E0B;   /* 포인트 강조색 — 어두운 발표자 창 강조색 겸용 */
  --shadow:         0 2px 12px rgba(26,35,50,0.07);
  --shadow-lg:      0 8px 32px rgba(26,35,50,0.12);
  --radius:         14px;
  /* 챕터 색 코딩 (교육자료) — 챕터 수만큼 쌍으로 */
  --ch1: #A36A12;  --ch1-bg: #FFF8E6;   /* 연노랑 */
  --ch2: #2F855A;  --ch2-bg: #EAF6EE;   /* 연그린 */
  --ch3: #2B6CB0;  --ch3-bg: #E8F1FB;   /* 연블루 */
  --ch4: #8C6A4A;  --ch4-bg: #F5EFE6;   /* 베이지 */
  --warn: #C53030; --warn-bg: #FFF5F5;  /* 금지 예시 */
  --good: #2F855A; --good-bg: #F0FAF4;  /* 권장 예시 */
}
```

사용자가 다른 팔레트를 요청하면 `:root` 변수만 교체한다. 컴포넌트 코드는 건드리지 않는다.

### 폰트 스택

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```

```css
/* 오프라인 대비 시스템 고딕 폴백 포함 */
font-family: 'Noto Sans KR', 'Inter', -apple-system, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;  /* body */
font-family: 'Inter', sans-serif;                    /* 태그·숫자 */
font-family: 'JetBrains Mono', monospace;            /* 코드 */
```

- 폰트 교체 요청 시에도 **고딕(산세리프) 계열만** 사용한다 (Pretendard, SUIT 등).
  명조·붓글씨·손글씨 계열 금지.
- `font-weight` 직접 지정 시 Google Fonts에 해당 weight가 로드되어 있는지 확인.

### 한국어 타이포그래피 규칙

```css
body { word-break: keep-all; overflow-wrap: break-word; }  /* 단어 중간 끊김 방지 — 필수 세트 */
```

- 카피에 `<br>`을 넣을 때는 **문장이 끝나는 지점에서만** 줄바꿈한다. 문장 중간 꺾임 금지.
- 짧은 2문장 블록은 첫 문장 끝에 `<br>`을 명시한다.

### 기본 폰트 크기 (실제 화면에서 잘 보이는 크기 기준)

```css
.slide__tag   { font-size: 1.05rem; }                          /* 섹션 레이블 */
.slide__title { font-size: clamp(2.6rem, 5.2vw, 4.2rem); }    /* 제목 */
.slide__subtitle { font-size: clamp(1.4rem, 2.9vw, 2rem); }   /* 부제목 */
.slide__body  { font-size: clamp(1.3rem, 2.35vw, 1.5rem); }   /* 본문 */
.card__title  { font-size: 1.35rem; }
.card__body   { font-size: 1.2rem; }
.card__icon   { font-size: 2.6rem; }
```

---

## 교육자료 설계 규칙

국내 PPT 디자인 전문 업체 포트폴리오 실측(교육 6건 91장 + 발표 15건 149장)에서 뽑은 **공통 문법과 제작 방식**이다.
레퍼런스는 베끼는 대상이 아니다 — 새 주제·새 CI가 와도 **같은 방식으로** 만들어지게 하는 것이 목적이다. 특정 장을 복제하는 건 문법을 익히는 연습일 뿐, 산출물이 아니다.

**전제: 학습자가 나중에 혼자 다시 본다 → 해설이 슬라이드에 글로 들어간다.** 발표자가 말로 채우는 발표자료(vanilla-deck)와 문법이 다르다.
**전부 쓰라는 체크리스트가 아니다** — 60분짜리 가벼운 강의에 활동지·서약서·니모닉을 다 넣을 필요는 없다. 요청 성격에 맞는 것만 골라 쓴다.

### 제작 절차 (6단계)

**순서가 곧 품질이다.** 부품 표부터 열면 "레퍼런스처럼 생긴 틀 + 글"이 나온다(260921 반려 — "기존 자료와 퀄리티가 다르지 않다, 모방만 할 줄 아는 느낌"). 그림을 먼저 정하고 부품은 그 그림을 만드는 재료로만 쓴다.

1. **재료 모으기** — 사용자가 준 캡처·이미지·표·실제 문장을 먼저 목록으로 만든다. **재료가 있는데 안 쓴 장은 검수에서 걸린다.** 사진이 필요한데 없으면 이 단계에서 확보(Pexels 등, "아이콘·일러스트·사진" 절)
2. **장별 시각 아이디어 한 줄** — 장마다 메시지를 그림으로 번역한 한 줄을 적는다. 아래 "보여줄 그림 먼저" 사전을 쓴다. 한 줄이 "카드 3개" "불릿"이면 아직 그림이 아니다 — 다시. 같은 아이디어가 3장 연속이면 다시
3. **레퍼런스 보기** — 원본 이미지 라이브러리가 있으면(작성자 로컬: `~/Downloads/레퍼런스_슬라이드_260919/교육/`) 같은 유형의 장을 **2~3장 Read로 직접 보고** 시작한다. 글 규칙만으로 만든 판은 반려된 전력이 있다
   (개념 장 → `67_*/04`, 빈칸 → `67_*/08`, 금지 예시 → `67_*/07`, 정리 → `67_*/15`, 숫자 강조 → `67_*/14`, 활동지 → `67_*/10`, 번호 상자 제목 + 차시 점 → `70_*/03`, 원형 사진 격자 → `70_*/07`, 다크 밴드 제목 → `62_*/03`, 목차 → `39_*/02`)
4. **톤 시안 2~3개 → 사용자가 고른다** — 10장 넘는 덱이면 전 장을 만들기 전에 **같은 장면 3장**(표지·개념 1장·정리 1장)을 톤만 다르게 2~3개 만들어 비교 캡처로 보여준다. 템플릿 기본 톤(파스텔 종이 카드)도 후보 중 하나일 뿐, 취향 검증을 대신하지 못한다(260921 — 기본 테마로 32장 만들고 전부 폐기). 사용자가 색·분위기를 이미 줬으면 그 톤 1개 + 대안 1개
   - 톤 = 바탕색 · 제목 서체 굵기·자간 · 카드(흰/검정) · 강조 1색(단색 또는 그라데이션) · 하단 띠 · 표지 오브제. CI 색을 받으면 `--edu-main`(제목·정답) `--edu-point`(밑줄·숫자·CTA)만 바꾼다. 흰 배경 글자색은 명암비 4.5:1 계산, 밝은 CI는 글자 대신 면·선에만
   - 260921 실측 예(사용자 선택): 밝은 회색 `#F5F5F7` 바탕 · Pretendard 800 큰 제목(자간 -0.03em) · 흰/검정 카드 · 파랑→보라→분홍 그라데이션 포인트 · 하단 검정 알약 띠 · 표지에 실물 목업
5. **장별 조립** — 2단계 한 줄을 그대로 그린다. 부품 표(아래 "템플릿 부품")는 그림을 만드는 재료. **한 장에 반복 단위(원 3개·카드 2×2·원 격자)는 하나**, 그리고 반복 단위만 있는 장은 그림이 아니다
6. **검증 2종** — (a) 메시지: 전 장 캡처에서 **글을 가리고 봐도 메시지가 보이나** — 안 보이면 2단계로. 같은 구조 3장 연속 없나, 재료 안 쓴 장 없나. (b) 모양: 레퍼런스와 나란히 빈 곳·겹침·넘침·푸터 침범, PDF 페이지 수 = 슬라이드 수(zlib로 스트림을 풀어 `/Type /Page`를 센다 — `grep`만으로는 틀린다), 헤드리스 콘솔 에러 0

### 보여줄 그림 먼저 — 메시지 유형 → 그림 사전

장의 메시지를 아래 유형 중 하나로 분류하고, 그 그림을 그린다. 글은 그림에 붙는 라벨이다.

| 메시지 유형 | 그림 | 그리는 법 (전부 CSS·SVG, 라이브러리 없음) |
|---|---|---|
| 시간·순서·출시 일정 | **타임라인 위 실물 실루엣** | 가로선 + 점, 각 시점 위에 대상(폰·문서·사람)을 실루엣으로. 미래·미정은 **점선 실루엣 + "?"** |
| 된다 · 안 된다, 지원 · 미지원 | **밝음 vs 잠금** | 되는 쪽 밝은 카드 + ✓ 칩 나열, 안 되는 쪽 어두운 카드 + 큰 자물쇠·`EN` 배지. 같은 크기 박스 2개 나란히 놓지 않는다 |
| 지금 vs 앞으로, 현재 → 변화 | **화살표 하나** | 왼쪽 실선 상자(지금) → 그라데이션 화살표 → 오른쪽 **점선 상자**(앞으로). 인용문 나열 금지 |
| 계승·후속·신규 라인 | **계보도** | 이전 모델(회색) → 화살표 → 후속. 이전이 없으면 점선 "이전 모델 없음" 상자 → "새로 생긴 라인" 강조. 핵심 스펙(화면 비율 등)은 **비율대로 도형**으로 |
| 수치 비교·크기 차이 | **비율대로 그린 도형** | 막대·원·사각의 크기를 실제 값에 비례. 숫자는 도형 옆 라벨 |
| 없는 것·오해·거짓 정보 | **점선 실루엣 + "?"** 또는 큰 ✕ | 있는 것과 같은 모양을 점선으로, 안에 "?"; 오답 문장은 "정답 X" 배지 |
| 절차·단계 | 번호 원 사진 3~4개 또는 화살표 스텝 | 각 단계에 실물 사진·캡처. 사진 없으면 라인 아이콘 |
| 개념·정의 | 원형 실물 + 큰 불릿 3~6개 | `.pair > .fig + .biglist` |
| 정답 채우기·암기 | 빈칸 문장 | `.bracket` + `.blank` — 정답이 크고 색으로 |
| 오답 모음·금지 | 이름 붙인 원 격자 | `.circles` 또는 원 격자 + 각 원에 오답 이름 알약 |
| 요약·정리 | 노트 3줄 또는 원 3개 | `.note` / 원 3개 — 챕터 끝에만 |
| 실제 화면·제품 | **실물 캡처를 크게** | 재료가 있으면 이게 앵커. 캡처 위에 번호·화살표 오버레이 |
| 분류 문제(이 중 어느 쪽?) | **두 칸 분류판** | 위에 후보 썸네일 줄, 아래 "A에만 / 둘 다" 두 칸. 정답 공개(`data-step`) 때 칸이 채워진다 |
| 반복 절차(루프) | **순환 고리** | 노드 3~4개를 타원 위에 놓고 화살표로 한 바퀴 (목차 → 시연 → 한 문장 → 목차) |
| 시간 배분 | **비율 막대 하나** | 막대 길이 = 실제 분. "수치 → 비율 도형"의 시간판 |
| 상황 → 해답 매칭 | **사람 + 말풍선 → 선 → 해답 칩** | 사람 아이콘에 상황 말풍선, 정답 공개 때 아래로 선이 내려와 해답 칩에 연결 |
| 배포물 안내 | **실물 종이 목업** | A4 두 장 앞·뒤를 살짝 기울여 "받을 물건"을 미리 보여준다 |
| 행동 약속·과제 | **빈 체크박스 미션 카드 한 장** | "이번 주 미션 하나" — 체크박스는 비워 둔다 |
| 조작 안내(단축키·버튼) | **실제 키캡 모양 + 한 단어** | 키캡 CSS + 누르면 생기는 일 한 단어 |

- 한 장에 그림 하나. 그림이 두 개면 장을 나눈다
- **같은 그림 유형이 3장 연속이면 하나는 바꾼다** — 카드 격자가 이어지면 그중 하나는 계보도·타임라인·화살표로
- 응용 예: 언어별 차이 → "된다·안 된다"를 말풍선 두 쌍으로(영어 질문→응답 ✓ / 한국어 질문→점선 빈 응답) · 금지 표현 → 카드 + 빨간 X 도장 · 손님 질문 퀴즈 → 말풍선 3개 + 큰 O/X
- 이 사전에 없는 메시지면 "이걸 종이에 손으로 그린다면?"을 먼저 답하고 그 그림을 CSS로 옮긴다
- 사전은 현장에서 나온 유형을 계속 추가한다(260921 psnm/ai-phone-edu 18장 재작업에서 7종 추가)

### 공통 문법 (발표자료와도 공유)

- **한 장 = 제목 블록 + 시각 앵커 하나 + 아래 결론 띠.** 앵커는 위 그림 사전에서 정한 **그림**이다 — 카드·불릿은 앵커가 아니다
- **글자가 적고 크다.** 불릿은 본문의 1.5배, 결론 문장은 2배, 빈칸 정답은 1.6배. 한 장에 문장 3~6개
- **제목은 학습자 쪽 말투** — 질문형·청유형·동사형. 발표자료의 주장 완결 문장과 다르다
- **사진은 꽉 채우거나 사라지거나.** 원형으로 꽉 채우기(`object-fit: cover`) 또는 위로 갈수록 투명해지는 마스크. 어중간한 사각 사진, 흰 덮개 페이드 금지
- **색은 역할 3개.** 바탕 1 + 강조 1 + 파스텔 세트(원·카드 구분). 강조는 알약·번호 배지·밑줄·CTA에만
- **반복 단위는 장당 하나.** 원 3개 / 카드 2×2 / 원 격자 3×2 / 사진 원 3~4개
- **하단 결론은 알약형 밴드, 가운데.** 정리·실습 안내·다음 차시 예고
- **번호는 CSS로 `1 2 3`** — 원문자(①②③) 금지. 페이지 번호는 하단 중앙
- **과정명·차시를 계속 노출** — 우상단 작게 또는 우측 세로

### 템플릿 부품 — 파스텔 종이 카드 기본 톤 (`assets/template.html`, 샘플 12장)

- **페이지 = 파스텔 배경 위 흰 종이 카드.** `<section class="slide edu" data-chapter="1~4">` 한 줄로 배경 톤(연노랑 → 연그린 → 연블루 → 베이지)이 챕터별로 바뀐다 — 색은 강조가 아니라 **위치 기억**. 본문은 `.paper`(큰 라운드 흰 카드) 안에
- **일러스트가 한 축.** 좌측 원형/블롭 슬롯(`.fig`)에 사진, 우측에 큰 불릿. 사진이 없으면 동봉 라인 아이콘(픽토그램)
- 페이지 번호는 카드 밖 하단 중앙 **색 원 배지**(`.pgno`, 헬퍼가 자동으로 붙임). 과정명은 `.course`(우상단) 또는 `.course-rail`(우측 세로)

#### 제목 3종

| 클래스 | 생김새 | 언제 |
|---|---|---|
| `.hd` (기본) | 노란 원 안 라인 아이콘(`.hd__icon > svg.ico`) + 큰 색 제목 + **짧은 코랄 밑줄**(제목 폭만큼, 전폭 아님) | 개념·설명 장 |
| `.edu--plain` + `.hd-box` | 큰 번호(`.hd-box__no`) + 노란 라운드 상자 안 제목 + 우상단 차시 점(`.session`) + 우측 세로 과정명(`.course-rail`) | 차시제 과정, 사례 장 |
| `.edu--band` + `.band` | 좌측 오렌지 번호 박스(`.band__no`) + 다크 밴드 안 노란 제목 + 우측 breadcrumb(`.band__crumb`) | 매뉴얼·법령·정의 장 |

#### 부품 목록

| 장 유형 | 클래스 | 생김새 |
|---|---|---|
| 표지 | `.edu--cover` + `.cover__kicker` `.cover__title` `.cover__fig` `.cover__meta` | 파스텔 풀블리드 + 작은 한 줄 + 큰 제목 + 하단 일러스트 슬롯(`<img>` 또는 `.pictos` 픽토그램 3개가 흰 띠 위에 선다) |
| 니모닉 목차 | `.toc-label` + `.toc3 > .toc3__item`(`__no` `__word` `__title`) + `.mnemonic-word` | 작은 "목 차" 상자 + N열 번호 배지 + 두문자 + 구어체 부 제목(열마다 색) + 두문자 모은 문장 |
| 개념 (일러스트 + 불릿) | `.pair > .fig + .biglist(.biglist--2col)` | 좌 원형 슬롯(`<img>` 꽉 채움 또는 `svg.ico` 픽토그램), 우 큰 불릿(회색 점) |
| 빈칸 채우기 | `.bracket`(노란 대괄호 콜아웃) + `.panel.panel--blue/--yellow`(접힌 귀퉁이 틴트 패널) + `.fill > p > .blank > .blank__ans[data-step]` | 문장 속 `( 정답 )` — 정답이 크고 굵고 MAIN색, → 키로 공개 |
| 금지 예시 | `.warn > .warn__label > span`(코랄 알약 "절대 하지 말아야 하는 자세" + 옆으로 뻗는 선) + `.warn__box` | 흰 박스 안 큰 볼드 키워드 문장 |
| 금지 예시 (라벨형) | `.say-no` + `.circles > .circle > .circle__ball + .circle__label` | 노란 원 안 오답 문장 + 아래 오답 이름 |
| 숫자 강조 | `.iconrow > .iconrow__item`(`__icon` `__label` `__num`) + `.brace` + `.big-say` + `.src-paren` | 노란 원 아이콘 3개 + 라벨 + 코랄 큰 숫자 + 둥근 브래킷 + 큰 결론 문장 + 출처 괄호 |
| 정리해 보아요 | `.note > .note__rings + .ribbon + .note__list` | 링 구멍 12개 노트 종이 + 갈색 리본 배너 + 큰 불릿 3줄(줄 사이 가는 선). 배경 베이지 |
| 사례 | `.cases > div > .case__label + .case__body` | 노란 알약 "사례N" + 선 + 문장 (핵심어 `<b>`) |
| 활동지·서약서 | `.cert > .cert__sub .cert__title .cert__list .cert__sign .cert__date` | 진한 테두리 + 안쪽 금선 액자, 제목 두 줄, ● 불릿, 이름·날짜 기입란 |
| 간지·마무리 | `.divider__big` + `.divider__line` + `.divider__fig(.pictos.pictos--sm)` | 카드 가득 큰 문장 중앙 + 짧은 코랄 선 + 일러스트 슬롯(작은 픽토그램 3개) |
| 챕터 두문자 배지 | `.paper.has-badge` + `.badge-char` | 좌상단 코랄 원 안 두문자 한 글자 |
| 원형 사진 격자 (260921) | `.lead`(코랄 한 문장) + `.pgrid[--n:3~4] > .pgrid__item > .pgrid__no + .pgrid__ph > img + .pgrid__cap` | 번호 배지 + 노랑/파랑 교대 테두리 원 사진 + 캡션. `.edu--plain` 장에서 (레퍼런스 70_*/07) |
| 사진 페이드 (260921) | `.fade-up[--fade:60%]` 를 사진 컨테이너에 | 위로 갈수록 투명해져 뒤 요소가 비친다. 흰 덮개 그라데이션 방식은 금지("점점 연해지는" 느낌이 안 남) |
| 알약 CTA (260921) | `.cta > 문장 + <small>` | 장 하단 중앙 코랄 알약 한 문장(폭 58%까지, 한 줄 40자 안쪽 — 우하단 단축키 힌트와 겹치지 않는 폭). 정리·실습 안내·다음 차시 예고 |
| 표지 원형 사진 (260921) | `.cover__fig > .fig.cover__photo > img` | 흰 테두리 원 사진이 하단 흰 띠 위에 선다 |

### 아이콘·일러스트 (260921, 레퍼런스 실측: 표지·마무리는 일러스트가 아래 절반을 채우고, 개념 장 원은 그림이 꽉 찬다. 제목 옆은 노란 원 안 **라인 아이콘**)

**우선순위: 실제 이미지 > 동봉 라인 아이콘(픽토그램) > 이모지.** 이모지는 컬러·입체라 파스텔 종이 카드와 어긋나고, 큰 슬롯에선 원의 1/3밖에 못 채워 "엉뚱하게 떠 있는" 모양이 된다. 큰 슬롯(`.fig` `.cover__fig` `.divider__fig`)에 이모지 금지.

| 슬롯 | 이미지가 있을 때 | 없을 때 |
|---|---|---|
| 제목 아이콘 `.hd__icon` · 아이콘 줄 `.iconrow__icon` | — | `<svg class="ico"><use href="#i-eye"/></svg>` (원의 60% · 50%) |
| 개념 원 `.fig` / 블롭 `.fig--blob` | `<img src>` — `object-fit: cover`로 원을 꽉 채움 | `svg.ico` 하나 (원의 약 50%, MAIN색 선. `.fig--sm`은 45%) |
| 표지·마무리 `.cover__fig` | `<img>` 높이 최대 24em, 하단 흰 띠 위에 서게 | `<div class="pictos">` 흰 원 3개(가운데 `.picto--accent` 노랑) — 자동으로 띠 위에 선다 |
| 간지 `.divider__fig` | `<img>` | `.divider__fig.pictos.pictos--sm` 작은 원 3개 |

**동봉 스프라이트 26종** (`<body>` 바로 아래, `#i-…`): eye · clock · hourglass · chat · mic · ear · bulb · check · star · target · users · user · heart · hand · book · pen · clipboard · list · chart · help · alert · flag · smile · frown · home · grad.
부족하면 `<symbol id="i-이름" viewBox="0 0 24 24">`을 추가한다 — Lucide(ISC)·Tabler(MIT) 같은 오픈 라이선스 아이콘의 path를 붙여 넣어도 된다(파일 상단 주석에 출처·라이선스 한 줄).

**이미지 소스** (무료·상업 이용 가능한 것만. 사용 전 각 사이트 라이선스 페이지를 한 번 더 확인한다):
- 사람·장면 일러스트: **unDraw**(undraw.co — 출처 표기 불필요, 사이트에서 MAIN색 지정 후 SVG 다운로드 → 레퍼런스 풍 플랫 일러스트에 가장 가깝다), **Open Peeps**(openpeeps.com — CC0), Storyset(storyset.com — Freepik, **출처 표기 필요**)
- 플랫 이모지 SVG: OpenMoji(openmoji.org — CC BY-SA, 표기 필요)
- 파일은 덱 HTML 옆 `img/` 폴더에 두고 상대 경로로. 단일 파일이 꼭 필요하면 `data:` URI로 인라인(용량 주의)
- 사용자가 준 사진은 **원형(`.fig` `.pgrid__ph` `.cover__photo`)으로 꽉 채우거나, `.fade-up`으로 사라지게** — 어중간한 사각 사진·흰 덮개 금지
- 무료 사진: Pexels(pexels.com — 출처 표기 불요, 재배포·판매만 금지). 후보를 6~18장 받아 **컨택트 시트(HTML 격자 → 캡처 1장)로 보고 고른다**. 직접 URL `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=1200`

### 기억·행동 장치 (내용 규칙)

- **니모닉 목차** — 챕터 제목 첫 글자를 모으면 한 단어가 되게 짓고 과정명과 연결한다 (마음 먼저 읽어요·음성 톤을 맞춰요·열린 질문을 던져요·기록으로 남겨요 → "마음열기")
- **예고 후 전개** — 전체 지도를 한 장에 먼저 보여주고 다음 장부터 하나씩 펼친다
- **빈칸 채우기** — "이를 ( )이라고 부릅니다" 받아 적게 만든다. 정답 없는 배포용 PDF는 `<body class="print-blanks">`로 인쇄
- **정리해 보아요** — 챕터 끝마다 핵심 3~4줄
- **금지 예시** — 오답을 모으고 **각 오답에 이름을 붙인다**("무성의한 위로", "성급한 해결")
- **활동지** — 읽는 자료가 아니라 쓰는 자료. 이름·날짜 기입란
- 사례는 추상 설명 대신 실물(장면·실제 문장)로

### 적용 우선순위 (손이 덜 가는 순)

1. 니모닉 목차 2. 빈칸 채우기 3. 정리해 보아요 4. 활동지 5. 금지 예시 6. 챕터별 배경색(`data-chapter`만 달면 된다)

### 발표자료와 차이 (요약)

| | 교육자료 (이 스킬) | 발표자료 (vanilla-deck) |
|---|---|---|
| 전제 | 학습자가 혼자 다시 봄 | 발표자가 말로 채움 |
| 텍스트 | 해설문 포함, 크고 적게 | 완결 문장 제목 + 시각 앵커 |
| 제목 | 질문·구어체·동사형 | 주장·완결 문장 |
| 색·배경 | 파스텔 배경 챕터별 전환 + 흰 종이 카드 | 흰 바탕 + 다크 표지·간지 |
| 구조 | 예고 → 전개 → 정리 → 활동 | 데이터 → 해석 → 결론 |
| 번호 | 좌상단 크게 + 하단 원 배지 | 하단 작게 |

### 부품 사용 주의

- **불릿·목록 항목에 `display:flex`를 쓰지 않는다** — 문장 안 `<b>`가 별도 칸으로 쪼개져 간격이 벌어진다. `.biglist li` `.note__list li` `.case__body`는 `position:relative` + `padding-left` + `::before` 절대 배치다
- 두문자 배지·차시·과정명 세로줄은 슬라이드 기준 `position:absolute`다. 슬라이드마다 마크업을 직접 넣는다
- 엔진 카운터(`#slideCounter`)는 교육 레이어에서 숨긴다 — `.pgno` 원 배지가 대신한다
- 크기는 전부 em — `.slide.edu { font-size: min(1.5vw, 2.6667vh) }`(1280×720에서 19.2px). 큰 화면에서 비율 그대로 커진다
- **em 함정(260921 재발 2회)**: `top` `height` 등을 em으로 주면 **그 요소 자신의 font-size**에 곱해진다. 글자 크기를 키운 제목·SVG의 위치·높이는 %나 부모 기준으로
- **덱 전용 클래스는 접두어 필수** — `.band` `.panel` `.cta`처럼 짧은 이름은 템플릿 부품과 겹쳐 조용히 깨진다(260921). 덱 전용 스타일은 `x-` 같은 접두어로
- **슬라이드 밖으로 나가는 장식(큰 원·아치)은 그 슬라이드에 `overflow: hidden`** — 대기 중인 옆 슬라이드의 장식이 현재 장에 비친다(260921)
- 슬라이드 영역을 스크립트로 잘라 넣을 때 `<title>` 치환은 **인덱스 계산보다 먼저** — 길이가 바뀌면 슬라이스가 어긋나 주석이 안 닫히고 첫 장이 통째로 사라진다(260921)
- **첫 장은 안내 주석의 `-->` 뒤에서 찾는다** — `✏️ 슬라이드 영역` 주석 안에 예시로 `<section class="slide edu">` 문자열이 있어서, `index('<section class="slide')`로 찾으면 주석 한가운데를 잘라 덱 전체가 주석 처리된다(엔진은 슬라이드 0장 → init TypeError). 260921 다른 세션에서 재발
- `assets/template-dark.html`은 1.5.0에서 삭제됐다 — 그 경로를 엔진 소스로 읽던 빌드 스크립트는 `assets/template.html`로 바꾼다(엔진 동일)
## 빌드 효과 (data-step)

단계적으로 나타나는 항목은 `data-step="1"`, `data-step="2"` ... 속성을 부여한다.

```css
[data-step] { opacity: 0; transform: translateY(12px); transition: opacity 0.35s, transform 0.35s; }
[data-step].visible { opacity: 1; transform: translateY(0); }
```

- `advance()`: 현재 슬라이드의 미표시 스텝을 번호순으로 하나씩 `.visible` 처리, 다 보이면 다음 슬라이드
- `retreat()`: 마지막 스텝부터 `.visible` 제거, 다 지워지면 이전 슬라이드
- **뒤로 이동으로 진입한 슬라이드는 스텝을 전부 표시 상태로** 되돌린다 (앞으로 진입은 전부 숨김)

---

## 키보드 + 터치

| 키 (`e.code`) | 동작 |
|---|---|
| `ArrowRight` / `Space` / `PageDown` | 다음 (빌드 스텝 → 슬라이드 순서) |
| `ArrowLeft` / `PageUp` | 이전 |
| `Home` / `End` | 첫 / 마지막 슬라이드 |
| `KeyF` | 전체화면 토글 (`requestFullscreen`) |
| `KeyI` | **목차 오버레이 토글** (클릭으로 슬라이드 점프) |
| `KeyN` | 화자 노트 패널 토글 |
| `KeyS` | **발표자 모드** — 별도 창 열기 (아래 스펙) |
| `Escape` | 목차 닫기 / 발표자 창에서는 창 닫기 |

- 목차가 열려 있는 동안 이동 키는 무시한다.
- 수정자 키(meta/ctrl/alt) 조합은 전부 무시해 브라우저 단축키를 보존한다 — 특히 `Cmd+P` 인쇄.
- 터치/마우스 스와이프: Pointer Events API, `SWIPE_THRESHOLD = 60px`, 세로 이동이 더 크면 무시.

---

## UI 컴포넌트

### 상단 진행바 + 슬라이드 카운터 + 네비 버튼

```html
<div id="progressBar"><div id="progressFill"></div></div>
<div id="slideCounter">1 / 5</div>
<button class="nav-btn" id="btnPrev" type="button" aria-label="이전 슬라이드">←</button>
<button class="nav-btn" id="btnNext" type="button" aria-label="다음 슬라이드">→</button>
```

진행바는 `top:0` 고정 3px, 카운터는 우하단, 버튼은 좌하단 원형 (`z-index:100`).

### 단축키 힌트 박스 (#kbdHint) — 항상 표시

우하단(카운터 위)에 `<kbd>F</kbd>전체화면 <kbd>I</kbd>목차 <kbd>N</kbd>노트 <kbd>S</kbd>발표자` 형태로
작게 상시 노출 (반투명 흰 배경 + blur). 단축키는 알아야 쓸 수 있다.

### 목차 오버레이 (I 키) — 필수

- 반투명 백드롭(`rgba(26,35,50,.55)` + blur) 위 흰 패널, 슬라이드 번호 + 제목 목록
- 제목은 `data-title` 속성 → 없으면 `.slide__title` 텍스트 → 없으면 "슬라이드 N" 순으로 취득
- 항목 클릭 → 해당 슬라이드로 `goTo` + 오버레이 닫힘, 현재 슬라이드는 하이라이트 표시
- 백드롭 클릭 / `I` / `Escape`로 닫힘. `z-index: 200`

### 화자 노트 패널 (N 키) — 필수

- 각 슬라이드의 `<aside class="notes">`는 항상 `display:none` (데이터 보관용)
- N 키를 누르면 화면 하단 고정 패널(다크 배경, `max-height:32vh`)에 현재 슬라이드의 노트 표시
- 슬라이드 전환 시 패널 내용 자동 갱신. `z-index: 90`

### 발표자 모드 (S 키) — 필수, PPT 발표자 보기와 동일한 역할

- S 키 → **같은 파일을 `?presenter=1`로 새 창에 열고** (`window.open`, 1400×900),
  `BroadcastChannel('vanilla-slide::' + location.pathname)`로 두 창을 **양방향 동기화**
- `?presenter=1`로 열리면 `body.is-presenter`가 붙어 덱 대신 발표자 UI 표시:
  - 현재 슬라이드 대형 미리보기 + 다음 슬라이드 소형 미리보기 (슬라이드 DOM을 복제해
    1280×720 기준 `transform: scale()` 축소 렌더 — `data-step` 전부 표시 상태)
  - 화자 노트(대형 폰트) + 현재 슬라이드 제목 + 카운터
  - 경과 타이머(리셋 버튼) — 발표 시간 관리용
  - 방향키로 슬라이드 단위 이동 → 관객 창도 함께 이동. `Esc`로 창 닫기
- 동기화 프로토콜: 이동 시 `{type:'goto', index}` 발신, 발표자 창 최초 로드 시
  `{type:'request-state'}`로 메인 창의 현재 위치를 받아 온다
- 팝업 차단 시 허용 안내 alert 표시

---

## 슬라이드 HTML 구조 패턴

```html
<section class="slide" id="slide-1" data-title="목차에 표시될 제목">
  <div class="slide__content">
    <p class="slide__tag">SECTION 01</p>
    <h1 class="slide__title">슬라이드 제목</h1>
    <p class="slide__body">본문 내용...</p>
    <!-- 빌드 효과 -->
    <ul class="slide__list">
      <li data-step="1">항목 1</li>
      <li data-step="2">항목 2</li>
    </ul>
    <!-- 카드형 레이아웃 -->
    <div class="cards"><div class="card">카드 내용</div></div>
    <!-- 코드 블록 -->
    <pre class="code-block"><code>코드 예시</code></pre>
  </div>
  <aside class="notes">발표자 메모 (N 키 패널에 표시됨)</aside>
</section>
```

---

## 인쇄(PDF 배포) 대응 — 전 장표가 각 1페이지

교안 배포용 PDF는 브라우저 인쇄(⌘P → PDF 저장)로 뽑는다. 아래 규칙이 있으면 **모든 슬라이드가
슬라이드당 1페이지(16:9)로 저장**된다 — `@page` 없이 두면 fixed 레이아웃이 겹쳐 1장만 나온다.

```css
@page { size: 1280px 720px; margin: 0; }   /* 16:9 페이지 = 슬라이드 1장 */
@media print {
  html, body { overflow: visible; height: auto;
               -webkit-print-color-adjust: exact; print-color-adjust: exact; }  /* 배경색 보존 */
  .slide { position: relative; inset: auto; transform: none !important;
           height: 100vh; page-break-after: always; break-inside: avoid; }
  .slide:last-of-type { page-break-after: auto; }   /* 마지막 빈 페이지 방지 */
  [data-step] { opacity: 1 !important; transform: none !important; }  /* 스텝 전부 표시 */
  #progressBar, #slideCounter, .nav-btn, #tocOverlay, #notesPanel, #presenterMode { display: none !important; }
}
```

---

## 필수 포함 요소 체크리스트

- [ ] `position: fixed; inset: 0` + **불투명 배경** 슬라이드 레이아웃
- [ ] `getBoundingClientRect()` reflow + 워치독 포함 `goTo()` 함수, `isAnimating` 플래그
- [ ] **F 전체화면 / I 목차 / N 화자 노트 / S 발표자 모드 — 표준 4키 전부**
- [ ] 발표자 모드: `?presenter=1` UI + BroadcastChannel 양방향 동기화 + 타이머
- [ ] 화자 노트가 발표 대본 수준으로 상세하게 (여는 멘트·강조·전환)
- [ ] `e.code` 기반 키 판별 (한/영 무관) + 수정자 키 조합 무시
- [ ] 진행바 + 슬라이드 카운터 + 네비 버튼 + 단축키 힌트 박스(#kbdHint)
- [ ] 각 슬라이드에 `id="slide-N"` + `data-title`
- [ ] URL 해시 동기화 (`#slide-N`, `history.replaceState` + `hashchange` 수신)
- [ ] `word-break: keep-all; overflow-wrap: break-word` (한글 포함 시)
- [ ] Noto Sans KR 로드 + 시스템 고딕 폴백 (한글 포함 시)
- [ ] `@page { size: 1280px 720px; margin: 0 }` + `@media print` — 전 장표 1페이지씩 인쇄
- [ ] 장마다 시각 아이디어 한 줄을 먼저 적었다 — 같은 그림 유형 3장 연속 없음, 받은 재료(캡처·이미지) 안 쓴 장 없음
- [ ] 10장 넘는 덱은 톤 시안 2~3개를 먼저 보여주고 골랐다 · 레퍼런스 2~3장을 직접 봤다
- [ ] 전 장 캡처에서 글을 가리고 봐도 메시지가 보인다
- [ ] 교육 규칙은 요청에 맞는 것만 — 챕터가 있으면 `data-chapter` 색 코딩, 챕터 끝엔 정리 장 검토
- [ ] 사진은 원형 꽉 채움 또는 `.fade-up` — 사각 사진·이모지 큰 슬롯 없음
- [ ] 전 장 캡처 확인 · PDF 페이지 수 = 슬라이드 수(zlib 계수) · 콘솔 에러 0
- [ ] 빈칸 슬라이드가 있으면 배포용은 `print-blanks`로 정답 없는 PDF도 뽑을지 확인
- [ ] 파일명 `{주제}_슬라이드_{YYMMDD}.html`

---

## 주의사항 (재발 버그 목록)

- `scale()` 기반 고정 캔버스 방식 사용 금지 — 반응형 깨짐, 텍스트 흐림 발생
- `getBoundingClientRect()` reflow 줄을 절대 생략하지 말 것 — 없으면 첫 전환이 순간이동
- `transitionend` 핸들러는 `e.target !== nextSlide || e.propertyName !== 'transform'` 체크 필수
  (자식 요소 이벤트 버블링 오발 방지) + **워치독 타이머 병행** (탭 숨김 시 이벤트 유실 → 덱 영구 잠김)
- 전환 정리 시 prev의 transition을 끄지 않으면 **유령 슬라이드**가 화면을 가로지른다
  (특히 슬라이드 배경이 반투명이면 그대로 노출)
- `.slide`에 불투명 `background` 누락 금지 — 뒤에서 정리되는 슬라이드가 비쳐 보임
- URL 해시는 `location.hash` 직접 대입 대신 `history.replaceState` 사용 — 히스토리 오염 + `hashchange` 루프 방지
- 발표자 모드 단축키는 **S** — P를 쓰면 `Cmd+P` 인쇄와 충돌한 전례가 있다. 키 핸들러 첫 줄에서
  meta/ctrl/alt 조합을 반드시 무시할 것
- 발표자 미리보기 클론(`.pm-scale .slide`)에는 `color: var(--text-primary)` 필수 — 없으면 발표자 창의 흰 글자색을
  상속해 제목이 안 보인다
- 발표자 UI에서 덱을 숨길 때는 `body.is-presenter > .slide` (직계 자식 선택자) — 후손 선택자로 쓰면
  미리보기 클론까지 숨겨진다
- `@page { size }` 없이 인쇄하면 fixed 슬라이드가 겹쳐 **PDF가 1장만 나온다**
- 불릿 dot과 텍스트 정렬은 반드시 `align-items: center` — `flex-start` + `margin-top` 조합은
  폰트 크기 변경 시 어긋남

```css
/* ✅ 올바른 방식 */
.list-item { display: flex; align-items: center; gap: 10px; }
.dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }

/* ❌ 잘못된 방식 — 폰트 크기 바뀌면 틀어짐 */
.list-item { display: flex; align-items: flex-start; }
.dot { margin-top: 8px; }
```
