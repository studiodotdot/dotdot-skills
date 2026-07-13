---
name: vanilla-slide
description: |
  순수 HTML/CSS/JavaScript(라이브러리 없음)로 웹 프레젠테이션 단일 파일을 생성하는 스킬.
  동봉된 완성형 엔진 템플릿(assets/template.html) 기반 — 방향키/스와이프 전환(translateX),
  F 전체화면 · I 목차 오버레이 · N 화자 노트 · S 발표자 모드(듀얼 창 동기화, 타이머, 다음 슬라이드 미리보기),
  진행바·카운터, data-step 빌드 효과, URL 해시 동기화, 인쇄(PDF 전 장 저장) 대응, 그레이/블루 디자인 토큰 포함.

  다음 요청에 반드시 사용:
  - "슬라이드 만들어줘", "프레젠테이션 HTML로", "웹 PPT", "발표자료/강의 교안 슬라이드"
  - 발표 자료를 HTML 파일 하나로 내보내달라는 요청
  - PPT/Google Slides 없이 브라우저에서 바로 발표하고 싶다는 요청
  - 기존 vanilla-slide 산출물을 기반으로 새 슬라이드를 만들어달라는 요청
  (.pptx 등 실제 오피스 파일을 요구하는 경우는 이 스킬 대상이 아님)
---

# Vanilla Slide 스킬

## 개요

단일 `.html` 파일로 완성되는 풀-스크린 웹 프레젠테이션을 만든다.
외부 라이브러리 없이 CSS `translateX` 전환 + 키보드·터치 입력으로 동작한다.

**표준 4키 = F(전체화면) · I(목차) · N(화자 노트) · S(발표자 모드).** 어떤 덱에서도 이 4가지가 빠지면 안 된다.

## 파일 생성 절차 — 템플릿 우선

검증된 엔진 완성본이 `assets/template.html`(이 스킬 폴더 기준)에 동봉되어 있다.
엔진 코드를 매번 다시 작성하면 미세 버그가 재발하므로, **반드시 템플릿을 복사한 뒤 콘텐츠만 교체한다.**

1. **콘텐츠 설계** — 요청/자료에서 슬라이드 수, 각 슬라이드 제목·내용 추출
2. **`assets/template.html` 읽기** → 새 파일로 복사
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

## 디자인 토큰 (그레이/블루 팔레트 — 기본값)

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
  --shadow:         0 2px 12px rgba(26,35,50,0.07);
  --shadow-lg:      0 8px 32px rgba(26,35,50,0.12);
  --radius:         14px;
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
