---
name: vanilla-slide
description: |
  순수 HTML/CSS/JavaScript(라이브러리 없음)로 웹 프레젠테이션 단일 파일을 생성하는 스킬.
  방향키/스와이프로 슬라이드 전환(translateX 애니메이션), F 키 전체화면, 슬라이드 번호·진행바 표시,
  data-step 빌드 효과, URL 해시 동기화, 그레이/블루 디자인 토큰 포함.

  다음 요청에 반드시 사용:
  - "슬라이드 만들어줘", "프레젠테이션 HTML로", "웹 PPT", "순수 JS 슬라이드"
  - 발표 자료를 HTML 파일 하나로 내보내달라는 요청
  - PPT/Google Slides 없이 브라우저에서 바로 발표하고 싶다는 요청
  - 기존 slide-demo.html을 기반으로 새 슬라이드를 만들어달라는 요청
---

# Vanilla Slide 스킬

## 개요

이 스킬은 단일 `.html` 파일로 완성되는 풀-스크린 웹 프레젠테이션을 만든다.
외부 라이브러리 없이 CSS `translateX` 전환 + 키보드·터치 입력으로 동작한다.

---

## 핵심 구조 원칙

### 레이아웃: fixed + inset:0 (스케일 방식 금지)
각 `.slide`는 `position: fixed; inset: 0`으로 뷰포트 전체를 점유한다.
`scale()` + 1920×1080 고정 캔버스 방식은 **사용하지 않는다** — 반응형이 깨지고 텍스트가 흐려진다.

```css
.slide {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  transform: translateX(100%);          /* 기본: 오른쪽 대기 */
  transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  will-change: transform;
}
.slide.is-active  { transform: translateX(0); }
.slide.exit-left  { transform: translateX(-100%); }
.slide.exit-right { transform: translateX(100%); }
body.is-animating { pointer-events: none; }  /* 전환 중 클릭 차단 */
```

콘텐츠는 `max-width: 1280px` (또는 요청에 따라 조정) 컨테이너에 담아 중앙 정렬한다. padding은 `0 60px`.

### 전환 함수: getBoundingClientRect() 강제 reflow 필수

```javascript
function goTo(nextIndex, direction) {
  if (isAnimating || nextIndex === current) return;
  if (nextIndex < 0 || nextIndex >= total) return;

  isAnimating = true;
  document.body.classList.add('is-animating');

  const prevSlide = slides[current];
  const nextSlide = slides[nextIndex];
  const goingNext = direction === 'next';

  // 1. transition 없이 시작 위치 배치
  nextSlide.style.transition = 'none';
  nextSlide.classList.remove('is-active', 'exit-left', 'exit-right');
  nextSlide.style.transform = goingNext ? 'translateX(100%)' : 'translateX(-100%)';

  // 2. 강제 reflow — 이 줄이 없으면 transition이 무시되어 순간이동 버그 발생
  nextSlide.getBoundingClientRect();

  // 3. transition 복원
  nextSlide.style.transition = '';
  nextSlide.style.transform = '';

  // 4. 동시 이동
  prevSlide.classList.remove('is-active');
  prevSlide.classList.add(goingNext ? 'exit-left' : 'exit-right');
  leaveSlide(prevSlide);
  enterSlide(nextSlide, goingNext ? 'forward' : 'backward');

  current = nextIndex;
  updateUI();

  // 5. 전환 완료 후 정리
  nextSlide.addEventListener('transitionend', function handler(e) {
    if (e.target !== nextSlide || e.propertyName !== 'transform') return;
    prevSlide.classList.remove('exit-left', 'exit-right');
    document.body.classList.remove('is-animating');
    isAnimating = false;
    nextSlide.removeEventListener('transitionend', handler);
  });
}
```

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
font-family: 'Noto Sans KR', 'Inter', sans-serif;   /* body */
font-family: 'Inter', sans-serif;                    /* 태그·숫자 */
font-family: 'JetBrains Mono', monospace;            /* 코드 */
```

한글 슬라이드: `word-break: keep-all` 적용으로 단어 단위 줄바꿈.

기본 폰트 크기 (실제 화면에서 잘 보이는 크기 기준):

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

```html
<li data-step="1">첫 번째 항목</li>
<li data-step="2">두 번째 항목</li>
```

```css
[data-step] { opacity: 0; transform: translateY(12px); transition: opacity 0.35s, transform 0.35s; }
[data-step].visible { opacity: 1; transform: translateY(0); }
```

`advance()` 호출 시 현재 슬라이드의 미표시 스텝을 하나씩 `.visible` 처리한다.
뒤로 가기 시 `retreat()`는 마지막 스텝부터 `.visible` 제거한다.

---

## 키보드 + UI 컨트롤

| 키 | 동작 |
|---|---|
| `→` / `Space` / `PageDown` | 다음 (빌드 스텝 → 슬라이드 순서) |
| `←` / `PageUp` | 이전 |
| `Home` | 첫 슬라이드 |
| `End` | 마지막 슬라이드 |
| `F` | 전체화면 토글 (`requestFullscreen`) |
| `N` | 화자 노트 토글 |

터치/마우스 스와이프: Pointer Events API, `SWIPE_THRESHOLD = 60px`.

---

## UI 컴포넌트

### 상단 진행바 + 슬라이드 카운터

```html
<div id="progressBar"><div id="progressFill"></div></div>
<div id="slideCounter">1 / 5</div>
```

```css
#progressBar  { position: fixed; top: 0; left: 0; width: 100%; height: 3px; background: var(--border); z-index: 100; }
#progressFill { height: 100%; background: var(--accent); transition: width 0.4s ease; }
#slideCounter { position: fixed; bottom: 20px; right: 24px; font-size: 0.8rem; color: var(--text-muted); z-index: 100; }
```

### 이전/다음 버튼

```html
<button id="btnPrev">←</button>
<button id="btnNext">→</button>
```

---

## 슬라이드 HTML 구조 패턴

```html
<section class="slide" id="slide-1">
  <div class="slide__content">
    <p class="slide__tag">SECTION 01</p>
    <h1 class="slide__title">슬라이드 제목</h1>
    <p class="slide__body">본문 내용...</p>
    <!-- 빌드 효과: data-step -->
    <ul class="slide__list">
      <li data-step="1">항목 1</li>
      <li data-step="2">항목 2</li>
    </ul>
    <!-- 카드형 레이아웃 -->
    <div class="card">카드 내용</div>
    <!-- 코드 블록 -->
    <pre class="code-block"><code>코드 예시</code></pre>
  </div>
  <!-- 화자 노트 (N 키로 토글) -->
  <aside class="notes">
    <div class="notes__label">화자 노트</div>
    발표자 메모
  </aside>
</section>
```

---

## 파일 생성 절차

1. **슬라이드 내용 파악** — 사용자의 요청/자료에서 슬라이드 수, 각 슬라이드 제목·내용 추출
2. **단일 .html 파일로 출력** — 모든 CSS·JS 인라인 포함
3. **필수 포함 요소 체크리스트**:
   - [ ] `position: fixed; inset: 0` 슬라이드 레이아웃
   - [ ] `getBoundingClientRect()` reflow 포함 `goTo()` 함수
   - [ ] `isAnimating` 플래그
   - [ ] `transitionend` 이벤트로 정리
   - [ ] 진행바 + 슬라이드 카운터
   - [ ] `F` 키 전체화면
   - [ ] URL 해시 동기화 (`#slide-N`)
   - [ ] Noto Sans KR 폰트 로드 (한글 포함 시)
4. **저장 위치**: 사용자가 별도 지정하지 않으면 현재 작업 디렉토리에 저장

---

## 주의사항

- `scale()` 기반 고정 캔버스 방식 사용 금지 — 반응형 깨짐, 텍스트 흐림 발생
- `getBoundingClientRect()` reflow 줄을 절대 생략하지 말 것 — 없으면 첫 전환이 순간이동
- 폰트 `font-weight` 직접 지정 시 Google Fonts에 해당 weight가 로드되어 있는지 확인
- `transitionend` 핸들러는 `e.target !== nextSlide` 또는 `e.propertyName !== 'transform'` 체크 필수 (자식 요소 이벤트 버블링 오발 방지)
- 불릿 점(dot)과 텍스트 정렬은 반드시 `align-items: center` 사용 — `flex-start` + `margin-top` 조합은 폰트 크기 변경 시 어긋남. `margin-top` 제거할 것

```css
/* ✅ 올바른 방식 */
.list-item { display: flex; align-items: center; gap: 10px; }
.dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }

/* ❌ 잘못된 방식 — 폰트 크기 바뀌면 틀어짐 */
.list-item { display: flex; align-items: flex-start; }
.dot { margin-top: 8px; }
```
