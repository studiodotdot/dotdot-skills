---
name: vanilla-slide
description: |
  강의 교안·교육자료를 순수 HTML/CSS/JavaScript(라이브러리 없음) 단일 파일 웹 슬라이드로 만드는 스킬.
  동봉된 완성형 엔진 템플릿(assets/template.html) 기반 — 방향키/스와이프 전환(translateX),
  F 전체화면 · I 목차 오버레이 · N 화자 노트 · S 발표자 모드(듀얼 창 동기화, 타이머, 다음 슬라이드 미리보기),
  진행바·카운터, data-step 빌드 효과, URL 해시 동기화, 인쇄(PDF 전 장 저장) 대응.
  교육자료 설계 규칙(니모닉 목차·빈칸 채우기·정리 슬라이드·금지 예시·활동지·챕터별 색 코딩) 수록.
  템플릿에는 디자인이 없다(엔진 + 톤 토큰 자리 + 아이콘 스프라이트) — 톤과 그림은 덱마다 시안에서 새로 정하고 덱 전용 스타일로 그린다.
  핵심 절차는 "보여줄 그림 먼저" — 부품을 고르기 전에 장마다 메시지를 그림으로 번역한 한 줄을 적고, 메시지 유형별 그림 사전으로 시각 앵커를 정한다.
  장수와 무관하게 전 장 제작 전 톤 시안(사용자가 톤을 안 줬으면 2~3개, 줬으면 그 톤 + 대안 1개) 비교, 같은 그림 유형 3장 연속 금지, "글을 가리고 봐도 메시지가 보이나" 검수.
  이벤트 모드(1.7.0): 행사·시상식·시연 영상용 화려한 연출 덱 — 같은 엔진의 assets/template-event.html(무대·디졸브·글자/단어 등장·레터박스·입자·패럴랙스 메커니즘 + 녹화용 UI 숨김)과
  "연출 사전"(배경·등장·전환·재질·타이포 기법을 덱마다 다르게 조합)으로 만든다. 요청에 모드가 드러나지 않으면 호출 직후 실무용/이벤트용을 묻는다.

  다음 요청에 반드시 사용:
  - "교안 만들어줘", "강의 슬라이드", "교육자료 HTML로", "워크숍 자료", "강의용 웹 PPT"
  - 교육·강의용 자료를 HTML 파일 하나로 내보내달라는 요청
  - PPT/Google Slides 없이 브라우저에서 바로 강의하고 싶다는 요청
  - 기존 vanilla-slide 산출물을 기반으로 새 교안을 만들어달라는 요청
  - 행사·시상식·오프닝·시연 영상용 슬라이드, "화려하게", "영상처럼 움직이는" 슬라이드 요청(이벤트 모드)
  경계: 사내 보고·제안서·공모전·IR 같은 발표자료 덱은 vanilla-deck 스킬 대상이다.
  (.pptx 등 실제 오피스 파일을 요구하는 경우는 이 스킬 대상이 아님)
---

# Vanilla Slide 스킬

## 개요

단일 `.html` 파일로 완성되는 풀-스크린 웹 교안을 만든다.
**교육용**이다 — 학습자가 나중에 혼자 다시 보는 자료. 발표자료(보고·제안·공모전)는 `vanilla-deck`을 쓴다.
외부 라이브러리 없이 CSS `translateX` 전환 + 키보드·터치 입력으로 동작한다.

**표준 4키 = F(전체화면) · I(목차) · N(화자 노트) · S(발표자 모드).** 어떤 덱에서도 이 4가지가 빠지면 안 된다.

## 모드 인터뷰 — 스킬 호출 직후, 파일을 읽기 전에

두 모드가 있다. **실무용**(강의·교안·인쇄 배포, 가독성·가벼움 우선 — 이 문서의 본문)과 **이벤트용**(행사·시상식·오프닝·시연 영상, 연출 우선 — 아래 "이벤트 모드" 절). 톤·그림·절차는 같은 원칙이고, 이벤트 모드는 템플릿과 연출 사전만 다르다.

1. 요청에 모드가 드러나면 묻지 않는다 — "교안·강의·워크숍·배포용 PDF" → 실무용, "행사·시상식·오프닝·시연 영상·화려하게·영상처럼" → 이벤트용
2. 드러나지 않으면 `AskUserQuestion` 도구(화면 아래 선택 창 — 보기 2~4개, 사용자가 직접 적는 "Other" 칸이 자동으로 붙는다)로 한 번 묻는다. 질문 "이 슬라이드는 어디에 쓰나요?" · 보기 ① 실무용 — 강의·교안·인쇄 배포 ② 이벤트용 — 행사·시상식·시연 영상. 채팅으로 길게 묻지 않는다
3. 이벤트용이면 같은 도구로 분위기를 이어서 묻는다. 질문 "어떤 분위기로 갈까요?" · 보기 ① 어둡고 극적(검정 바탕 + 빛) ② 밝고 대담(흰 바탕 + 초대형 글자) ③ 몽환·유리(오로라 + 반투명 카드) — "Other"로 직접 적을 수 있다. 답은 톤 시안(2~3개)의 출발점일 뿐, 그대로 고정 템플릿을 꺼내는 게 아니다. **색은 묻고 받는다**(CI·좋아하는 색·행사 포스터) — 없으면 시안에서 예시 값으로 출발하되 클로드가 색 조합을 새로 제안하지 않는다
4. 도구를 쓸 수 없는 환경(자동 실행)이면 실무용으로 가정하고 산출물 첫 줄에 그 가정을 적는다

## 파일 생성 절차 — 템플릿 우선

검증된 엔진 완성본이 `assets/template.html`(이 스킬 폴더 기준)에 동봉되어 있다.
엔진 코드를 매번 다시 작성하면 미세 버그가 재발하므로, **반드시 템플릿을 복사한 뒤 콘텐츠만 교체한다.**

**템플릿에는 디자인이 없다.** 들어 있는 것은 엔진(전환·4키·인쇄) · `✏️ 덱 톤 토큰` 자리(중립 회색 자리표시) · 라인 아이콘 스프라이트 26종 · 기법 3개(`.ico` `.fade-up` `.pgno`) · 검증용 예시 3장뿐이다.
카드·원·띠·제목 스타일 같은 부품은 **일부러 싣지 않았다** — 파일에 보이는 부품은 규칙으로 못 막고, 그걸 채우면 "레퍼런스처럼 생긴 틀 + 글"이 된다(260921 반려 2회). 이 덱의 그림과 부품은 매번 `✏️ 덱 전용 스타일`에서 새로 그린다.
과거 시안(파스텔 종이 카드 부품 30여 개 포함)은 `references/example_pastel_paper_v150.html`에 있다 — **보고 배우되 복사하지 않는다.**

**순서는 아래 "교육자료 설계 규칙 → 제작 절차(6단계)" 하나뿐이다.** 이 절은 그 절차 5단계(조립)에서 지킬 **파일 편집 규칙**이다.

- **템플릿을 복사한 새 파일에서 `✏️` 표시가 있는 세 곳만 만진다**: `:root`의 `✏️ 덱 톤 토큰` · `<style>` 끝의 `✏️ 덱 전용 스타일` · `<body>`의 `✏️ 슬라이드 영역`. `⛔ 엔진` 아래(UI 마크업 + JS)와 엔진 CSS는 건드리지 않는다
- 톤 토큰: 시안에서 고른 값으로 `--tone-*`을 **전부** 교체(자리표시 회색 그대로 내보내지 않는다). 챕터 쌍 `--ch1~4`는 쓰는 챕터 수만큼만 채우고 나머지는 자리표시 그대로 둬도 된다(`data-chapter`를 안 달면 안 쓰인다)
- 덱 전용 스타일: 이 덱의 그림·부품을 전부 여기서 그린다. 클래스는 덱 약칭 접두어(예: 고객응대 → `cs-`). 템플릿 예시의 `ex-` CSS는 지운다
- 슬라이드 영역: 각 `<section class="slide edu">`에 `id="slide-N"`(1부터 순번)과 `data-title="목차용 제목"`. 표지·마무리는 `edu--cover` 추가(페이지 번호 안 붙음). 예시 3장은 전부 교체
- 화자 노트 `<aside class="notes">`: **첫 줄에 이 장의 시각 아이디어 한 줄**("이 장의 그림: 타임라인 위 실루엣"), 이어서 발표 대본 — 여는 멘트(따옴표로 실제 문장) → 강조 → 전환, `<br>`로 구분한 2~4문장. "여는 멘트:" 같은 레이블은 써도 되고 안 써도 된다(엔진은 레이블을 붙이지 않는다)
- 순차 등장 요소에 `data-step="1"`, `"2"`, … (빈칸 정답 공개·단계 공개)
- `<title>`, 표지·마무리 내용 교체
- 파일명: `{주제}_슬라이드_{YYMMDD}.html`, 위치는 지정 없으면 현재 작업 디렉토리. 시안·설계 메모는 같은 폴더의 `tone_samples/`·`설계_{YYMMDD}.md`
- **이벤트 모드는 `assets/template-event.html`을 복사한다** — 엔진(`⛔` 이후)은 `template.html`과 바이트 단위로 같고, 그 앞에 연출 메커니즘(무대·디졸브·쪼개기·레터박스·입자·패럴랙스·녹화용 UI 숨김)만 더 있다. 편집 규칙은 위와 같다(`✏️` 세 곳 + `<body>`의 스위치 클래스). 실무용 덱에 이 템플릿을 쓰지 않는다

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

(엔진 UI·옛 범용 덱 전용) `.slide__content`는 발표자 창 등 엔진 UI가 쓰는 래퍼다. 교육 장은 `.slide.edu`(padding 0, em 체계)에 직접 그린다.

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

## 디자인 토큰 (엔진 UI 기본값 · 덱 톤은 `--tone-*` `--ch1~4` 자리표시)

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
  /* ✏️ 덱 톤 토큰 — 시안에서 고른 값으로 전부 교체 (아래는 중립 회색 자리표시) */
  --tone-bg: #F4F5F7;  --tone-card: #FFFFFF;  --tone-ink: #1E2430;  --tone-ink2: #4B5563;  --tone-muted: #8A93A3;
  --tone-accent: #3B5BDB;  --tone-accent-2: #DCE3FA;
  /* 챕터 색 쌍(선택) — 배경과 배지가 한 쌍. 색 = 위치 기억 */
  --ch1: #3B5BDB;  --ch1-bg: #F4F5F7;   /* … --ch4 까지 */
}
```

톤은 `--tone-*`·`--chN`만 바꾼다. 엔진 토큰(`--bg` `--accent` 등)은 UI(진행바·목차·노트 창)용이라 건드리지 않는다.

**폰트 기준**: 장(`.slide.edu`)의 본문 폰트는 Pretendard(jsdelivr, 시스템 고딕 폴백). 아래 "폰트 스택"의 Noto Sans KR 스택은 엔진 UI(목차·노트·발표자 창)용이다. 장 안에서 크기 단위는 em — `.slide.edu`가 1280×720에서 **1em = 19.2px**이고 "본문"은 1em, 불릿은 1.5em, 결론 문장은 2em, 빈칸 정답은 1.6em을 뜻한다.

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

---

## 교육자료 설계 규칙

국내 PPT 디자인 전문 업체 포트폴리오 실측(교육 6건 91장 + 발표 15건 149장)에서 뽑은 **공통 문법과 제작 방식**이다.
레퍼런스는 베끼는 대상이 아니다 — 새 주제·새 CI가 와도 **같은 방식으로** 만들어지게 하는 것이 목적이다. 특정 장을 복제하는 건 문법을 익히는 연습일 뿐, 산출물이 아니다.

**전제: 학습자가 나중에 혼자 다시 본다 → 해설이 슬라이드에 글로 들어간다.** 발표자가 말로 채우는 발표자료(vanilla-deck)와 문법이 다르다.
**전부 쓰라는 체크리스트가 아니다** — 60분짜리 가벼운 강의에 활동지·서약서·니모닉을 다 넣을 필요는 없다. 요청 성격에 맞는 것만 골라 쓴다.

### 제작 절차 (6단계)

**순서가 곧 품질이다.** 부품 표부터 열면 "레퍼런스처럼 생긴 틀 + 글"이 나온다(260921 반려 — "기존 자료와 퀄리티가 다르지 않다, 모방만 할 줄 아는 느낌"). 그림을 먼저 정하고 부품은 그 그림을 만드는 재료로만 쓴다.

1. **재료 모으기** — 사용자가 준 캡처·이미지·표·실제 문장을 먼저 목록으로 만든다. **재료가 있는데 안 쓴 장은 검수에서 걸린다.** 사진이 필요한데 없으면 이 단계에서 확보(Pexels 등, "아이콘·일러스트" 절)
2. **장별 시각 아이디어 한 줄** — 장마다 메시지를 그림으로 번역한 한 줄을 적는다. 아래 "보여줄 그림 먼저" 사전을 쓴다. 한 줄이 "카드 3개" "불릿"이면 아직 그림이 아니다 — 다시. 같은 아이디어가 3장 연속이면 다시. **기록 위치**: 작업 폴더 `설계_{YYMMDD}.md`에 장 번호 순으로 표로 적고, 조립 때 각 장 노트 첫 줄에도 옮긴다(나중에 덱만 봐도 의도가 남게)
3. **레퍼런스 보기(있을 때만)** — 원본 이미지 라이브러리가 있는 환경(작성자 로컬: `~/Downloads/레퍼런스_슬라이드_260919/교육/`)에서만. 같은 유형의 장을 **2~3장 Read로 직접 보고** 시작한다. 글 규칙만으로 만든 판은 반려된 전력이 있다. 라이브러리가 없으면 건너뛰고 `references/example_pastel_paper_v150.html`의 구현만 참고한다. 그림 사전 유형 중 레퍼런스 장이 없는 것(계보도·화살표·밝음 vs 잠금·목업·미션 카드)은 사전의 "그리는 법"이 기준
   (개념 장 → `67_*/04`, 빈칸 → `67_*/08`, 금지 예시 → `67_*/07`, 정리 → `67_*/15`, 숫자 강조 → `67_*/14`, 활동지 → `67_*/10`, 번호 상자 제목 + 차시 점 → `70_*/03`, 원형 사진 격자 → `70_*/07`, 다크 밴드 제목 → `62_*/03`, 목차 → `39_*/02`)
4. **톤 시안 → 사용자가 고른다** — 장수와 무관하게, 전 장을 만들기 전에 **같은 장면 3장**(표지 · 그림이 있는 본문 1장 · 정리 1장)을 톤만 다르게 만들어 비교 캡처로 보여준다. 사용자가 색·분위기를 안 줬으면 2~3개, 줬으면 그 톤 1개 + 대안 1개. 템플릿 기본 톤(중립 회색)은 후보가 아니다(260921 — 기본 테마로 32장 만들고 전부 폐기). 사용자가 없는 환경(자동 실행)이면 후보를 전부 파일로 남기고 하나를 고른 뒤 이유를 적는다
   - 산출물 규격: `tone_samples/tone_A.html` `tone_B.html`(각 3장, 같은 엔진) + `tone_samples/톤비교.html`(캡처를 나란히 + 각 톤 한 줄 설명). 고른 뒤 그 톤의 토큰·CSS를 본 덱에 옮긴다
   - 톤 = 바탕색 · 제목 서체 굵기·자간 · 카드(흰/검정) · 강조 1색(단색 또는 그라데이션) · 하단 띠 · 표지 오브제. CI 색을 받으면 `--tone-accent`(정답·밑줄·배지·CTA) `--tone-ink`(제목·본문)와 챕터 쌍 `--chN`만 바꾼다. 흰 배경 글자색은 명암비 4.5:1 계산, 밝은 CI는 글자 대신 면·선에만
   - 260921 실측 예(사용자 선택): 밝은 회색 `#F5F5F7` 바탕 · Pretendard 800 큰 제목(자간 -0.03em) · 흰/검정 카드 · 파랑→보라→분홍 그라데이션 포인트 · 하단 검정 알약 띠 · 표지에 실물 목업
5. **장별 조립** — 2단계 한 줄을 그대로 그린다. 그리는 법은 "보여줄 그림 먼저" 사전의 오른쪽 열, 구현은 `✏️ 덱 전용 스타일`에 직접(파일 편집 규칙은 위 "파일 생성 절차"). **한 장에 반복 단위(원 3개·카드 2×2·원 격자)는 하나**, 그리고 반복 단위만 있는 장은 그림이 아니다
6. **검증 2종** — (a) 메시지: 전 장 캡처에서 **글을 가리고 봐도 메시지가 보이나** — 안 보이면 2단계로. 같은 구조 3장 연속 없나, 재료 안 쓴 장 없나. (b) 모양: 빈 곳·겹침·넘침·하단 UI 침범(아래 안전 영역), PDF 페이지 수 = 슬라이드 수(zlib로 스트림을 풀어 `/Type /Page`를 센다 — `grep`만으로는 틀린다), 헤드리스 콘솔 에러 0. 명령은 아래 "검증 명령"

### 검증 명령 (헤드리스 Chrome)

```bash
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$C" --headless=new --hide-scrollbars --window-size=1280,720 --virtual-time-budget=3000 --screenshot=sN.png "file://$PWD/덱.html#slide-N"   # 장별 캡처
"$C" --headless=new --no-pdf-header-footer --virtual-time-budget=4000 --print-to-pdf=덱.pdf "file://$PWD/덱.html"                        # PDF
"$C" --headless=new --enable-logging=stderr --v=1 --virtual-time-budget=3000 --dump-dom "file://$PWD/덱.html" 2>&1 >/dev/null | grep -c CONSOLE   # 콘솔 에러 수 → 0
```
- `data-step` 요소는 복사본에 `<style>[data-step]{opacity:1!important;transform:none!important}</style>`를 넣어 전부 보이는 상태로 캡처한다
- 장수는 `grep -c '<section class="slide'`로 세지 않는다 — 안내 주석 안 예시 문자열에 걸릴 수 있다. `grep -c 'id="slide-[0-9]'`로
- PDF 페이지 수: 스트림을 zlib로 풀어 `/Type /Page`(Pages 제외)를 센다

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
| 개념·정의 | 원형 실물 + 큰 불릿 3~6개 | 좌 원형 사진(꽉 채움) + 우 큰 불릿(본문 1.5배). 2단 grid |
| 정답 채우기·암기 | 빈칸 문장 | 큰 대괄호 프레임 안 문장, `( 정답 )`은 본문 1.6배·강조색·`data-step`으로 공개 |
| 오답 모음·금지 | 이름 붙인 원 격자 | 파스텔 원 3~6개, 안에 오답 문장, 각 원 아래 오답 이름 알약 |
| 요약·정리 | 노트 3줄 또는 원 3개 | 링 노트 종이 + 리본 배너 + 큰 불릿 3줄, 또는 채운 원 3개 — 챕터 끝에만 |
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
- 사전은 현장에서 나온 유형을 계속 추가한다(260921 실전 교안 18장 재작업에서 7종 추가)

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

### 템플릿에 실린 것 (`assets/template.html`)

| 구분 | 내용 | 비고 |
|---|---|---|
| 엔진 | 전환·F/I/N/S·진행바·목차·노트·발표자·인쇄 | `⛔ 엔진` 아래, 수정 금지 |
| 덱 톤 토큰 | `--tone-bg` `--tone-card` `--tone-ink` `--tone-ink2` `--tone-muted` `--tone-accent` `--tone-accent-2` + 챕터 쌍 `--ch1~4` / `--ch1~4-bg` | `--tone-*`은 자리표시 — 시안 값으로 **전부 교체**. 챕터 쌍은 쓰는 만큼만 |
| 장 기본 | `<section class="slide edu" data-chapter="N">` — em 크기 체계(1280×720에서 1em = 19.2px), 챕터 배경 | 표지·마무리는 `edu--cover` 추가 |
| 페이지 번호 | `.pgno` 하단 중앙, 헬퍼가 자동으로 붙임. 번호 = 표지를 포함한 순번(표지 다음 장이 2) | 표지·마무리(`edu--cover`)엔 안 붙음. 모양은 덱 전용 스타일에서 덮어써도 됨 |
| 라인 아이콘 | `<body>` 직후 스프라이트 26종 + `.ico`(크기 = font-size, 색 = color) | 부족하면 `<symbol>` 추가 |
| 사진 페이드 | `.fade-up[--fade:60%]` — 위로 갈수록 투명 | 흰 덮개 방식 금지 |
| 덱 전용 스타일 자리 | `✏️ 덱 전용 스타일` — 이 덱의 그림·부품을 전부 여기서 그린다 | 접두어 = 덱 약칭 2~3글자(예: `cs-`). 예시의 `ex-`는 지운다 |
| 예시 3장 | 표지 · "시간·순서 → 타임라인 위 실루엣" 그림 1장 · 마무리 (`ex-` 클래스) | 엔진 검증용, CSS·마크업 전부 교체 |

**부품은 그때그때 그린다.** 원형 사진 슬롯, 카드, 알약 띠, 빈칸 문장, 체크 칩 같은 것도 이 덱의 톤에 맞춰 덱 전용 스타일에 새로 쓴다. 매번 시간이 더 들지만 그게 목적이다 — 같은 부품에서 나온 덱은 전부 같은 얼굴이 된다.

**예시 시안** (`references/`) — 보고 배우되 복사하지 않는다:
- `example_pastel_paper_v150.html` — 파스텔 종이 카드 톤 12장. 종이 카드·노란 원 아이콘·코랄 밑줄·빈칸·금지 예시·링 노트·서약서·니모닉 목차 등 부품 30여 개의 **구현 참고**(어떻게 그렸는지). 레퍼런스 교육자료 6건 실측판
- 다른 톤 예(260921 사용자 선택, 파일 없음): 밝은 회색 `#F5F5F7` · Pretendard 800 큰 제목(자간 -0.03em) · 흰/검정 카드 · 파랑→보라→분홍 그라데이션 포인트 · 하단 검정 알약 띠 · 표지에 실물 목업

### 아이콘·일러스트 (260921, 레퍼런스 실측: 표지·마무리는 일러스트가 아래 절반을 채우고, 개념 장 원은 그림이 꽉 찬다. 제목 옆은 노란 원 안 **라인 아이콘**)

**우선순위: 실제 이미지 > 동봉 라인 아이콘(픽토그램) > 이모지.** 이모지는 컬러·입체라 대부분의 톤과 어긋나고, 큰 슬롯에선 원의 1/3밖에 못 채워 "엉뚱하게 떠 있는" 모양이 된다. 큰 슬롯(개념 원·표지·간지)에 이모지 금지.

아래 표는 **그림 사전으로 장의 그림을 정한 뒤, 그 안의 이미지 슬롯을 채우는 규칙**이다. 표지·마무리도 먼저 그림 사전(메시지를 오브제로)을 적용하고, 마땅한 그림이 없을 때만 폴백 열을 쓴다.

| 슬롯 | 이미지가 있을 때 | 없을 때(폴백) |
|---|---|---|
| 제목 옆·아이콘 줄의 작은 원 | — | `<svg class="ico"><use href="#i-eye"/></svg>` (원 지름의 50~60%) |
| 개념 장 큰 원·블롭 | `<img>` — `object-fit: cover`로 원을 꽉 채움 | `svg.ico` 하나(원의 약 50%, 강조색 선) |
| 표지·마무리 하단 | `<img>` 크게(높이 화면의 40~45%), 바닥 띠 위에 서게 | 원 3개 + 라인 아이콘(가운데만 강조색 면) |
| 간지 | `<img>` | 작은 원 3개 + 라인 아이콘 |

**동봉 스프라이트 26종** (`<body>` 바로 아래, `#i-…`): eye · clock · hourglass · chat · mic · ear · bulb · check · star · target · users · user · heart · hand · book · pen · clipboard · list · chart · help · alert · flag · smile · frown · home · grad.
부족하면 `<symbol id="i-이름" viewBox="0 0 24 24">`을 추가한다 — Lucide(ISC)·Tabler(MIT) 같은 오픈 라이선스 아이콘의 path를 붙여 넣어도 된다(파일 상단 주석에 출처·라이선스 한 줄).

**이미지 소스** (무료·상업 이용 가능한 것만. 사용 전 각 사이트 라이선스 페이지를 한 번 더 확인한다):
- 사람·장면 일러스트: **unDraw**(undraw.co — 출처 표기 불필요, 사이트에서 MAIN색 지정 후 SVG 다운로드 → 레퍼런스 풍 플랫 일러스트에 가장 가깝다), **Open Peeps**(openpeeps.com — CC0), Storyset(storyset.com — Freepik, **출처 표기 필요**)
- 플랫 이모지 SVG: OpenMoji(openmoji.org — CC BY-SA, 표기 필요)
- 파일은 덱 HTML 옆 `img/` 폴더에 두고 상대 경로로. 단일 파일이 꼭 필요하면 `data:` URI로 인라인(용량 주의)
- 사용자가 준 사진은 **원형으로 꽉 채우거나(`object-fit: cover`), `.fade-up`으로 사라지게** — 어중간한 사각 사진·흰 덮개 금지
- 무료 사진: Pexels(pexels.com — 출처 표기 불요, 재배포·판매만 금지). 후보를 6~18장 받아 **컨택트 시트(HTML 격자 → 캡처 1장)로 보고 고른다**. 직접 URL `https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=1200`

### 기억·행동 장치 (내용 규칙)

- **니모닉 목차** — 챕터 제목 첫 글자를 모으면 한 단어가 되게 짓고 과정명과 연결한다 (마음 먼저 읽어요·음성 톤을 맞춰요·열린 질문을 던져요·기록으로 남겨요 → "마음열기")
- **예고 후 전개** — 전체 지도를 한 장에 먼저 보여주고 다음 장부터 하나씩 펼친다
- **빈칸 채우기** — "이를 ( )이라고 부릅니다" 받아 적게 만든다. 정답 없는 배포용 PDF가 필요하면 덱 전용 스타일에 `@media print { .print-blanks .정답클래스 { color: transparent !important; border-bottom-color: inherit; } }`를 넣고 `<body class="print-blanks">`로 인쇄한다(엔진 인쇄 규칙이 `[data-step]`을 `opacity:1 !important`로 강제하므로 opacity로는 못 숨긴다)
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
| 색·배경 | 덱마다 시안에서 정한 톤(챕터별 색 쌍 선택) | 흰 바탕 + 다크 표지·간지 |
| 구조 | 예고 → 전개 → 정리 → 활동 | 데이터 → 해석 → 결론 |
| 번호 | 장 번호 크게 + 하단 중앙 페이지 번호 | 하단 작게 |

### 부품 사용 주의

- **불릿·목록 항목에 `display:flex`를 쓰지 않는다** — 문장 안 `<b>`가 별도 칸으로 쪼개져 간격이 벌어진다. `position:relative` + `padding-left` + `::before` 절대 배치로
- 배지·차시·과정명 같은 장식은 슬라이드 기준 `position:absolute`. 슬라이드마다 마크업을 직접 넣는다
- 엔진 카운터(`#slideCounter`)는 덱 톤에 안 맞으면 덱 전용 스타일에서 숨긴다 — `.pgno`가 페이지 번호를 맡는다
- 크기는 전부 em — `.slide.edu { font-size: min(1.5vw, 2.6667vh) }`(1280×720에서 19.2px). 큰 화면에서 비율 그대로 커진다
- **em 함정(260921 재발 2회, 260928 재발)**: 위치·크기 속성 **전부**(`top` `left` `bottom` `right` `width` `height` `padding` `margin`)를 em으로 주면 **그 요소 자신의 font-size**에 곱해진다. 글자 크기를 바꾼 요소(각주·제목·SVG)의 위치·크기는 %나 부모 기준으로
- **표지 flex 함정(260928)**: 엔진 `.slide`가 `display:flex; align-items:center; justify-content:center`이고 `.slide.edu`는 `display:block`만 되돌린다. 덱에서 `.slide.edu.cs-cover { display:flex }`를 주는 순간 `justify-content:center`가 되살아나 내용이 세로 중앙으로 내려간다 — flex를 켜면 `justify-content`·`align-items`를 반드시 명시
- **하단 안전 영역**: 엔진 UI가 항상 떠 있다 — 좌하단 네비 버튼(폭 약 9%, 높이 약 4em) · 우하단 단축키 힌트(폭 약 22%) · 하단 중앙 `.pgno`. 하단 알약 띠·각주·CTA는 **폭 58% 이내, 아래에서 2.6em 위**에 두고 좌우 하단 모서리를 비운다
- **덱 전용 클래스는 덱 약칭 접두어 필수**(예: 고객응대 → `cs-`, AI폰 → `ap-`) — 엔진 클래스(`.slide` `.slide__*` `.cards` `.card` `.code-block` `.notes` `.toc__*` `.pm-*` `.nav-btn`)나 템플릿 예시(`ex-`)와 겹치면 조용히 깨진다(260921 — 권장 접두어와 예시 접두어가 같아 다른 덱이 깨진 전력). `.cards` `.card` `.slide__title` 등은 엔진의 범용 UI 잔재라 **덱 본문에 쓰지 않는다**
- **장 자체(display·padding·배경)를 바꾸는 규칙은 `.slide.edu.cs-…`로** — `.cs-cover` 한 개짜리 셀렉터(0-1-0)는 기본 규칙 `.slide.edu`(0-2-0)에 져서 조용히 무시된다(260921 1.6.0 리뷰에서 발견)
- **슬라이드 밖으로 나가는 장식(큰 원·아치)은 그 슬라이드에 `overflow: hidden`** — 대기 중인 옆 슬라이드의 장식이 현재 장에 비친다(260921)
- 슬라이드 영역을 스크립트로 잘라 넣을 때 `<title>` 치환은 **인덱스 계산보다 먼저** — 길이가 바뀌면 슬라이스가 어긋나 주석이 안 닫히고 첫 장이 통째로 사라진다(260921)
- **첫 장은 안내 주석의 `-->` 뒤에서 찾는다** — 1.6.1 이하 템플릿과 그 산출물은 `✏️ 슬라이드 영역` 주석 안에 예시로 `<section class="slide edu">` 문자열이 있어서(1.6.2부터 전각 꺾쇠지만 옛 파일은 그대로), `index('<section class="slide')`로 찾으면 주석 한가운데를 잘라 덱 전체가 주석 처리된다(엔진은 슬라이드 0장 → init TypeError). 260921 다른 세션에서 재발
- `assets/template-dark.html`은 1.5.0에서 삭제됐다 — 그 경로를 엔진 소스로 읽던 빌드 스크립트는 `assets/template.html`로 바꾼다(엔진 동일)
- 1.6.0부터 템플릿에 파스텔 부품(`.paper` `.hd` `.fig` `.biglist` `.bracket` `.note` `.cert` …)이 없다 — 그 클래스를 쓰던 산출물은 `references/example_pastel_paper_v150.html`의 CSS를 덱 전용 스타일로 가져와야 한다

---

## 이벤트 모드 — 행사·시상식·시연 영상 (1.7.0)

**언제**: 무대 화면·시상식·오프닝·시연 영상처럼 **한 번 보고 지나가는 자료**. 학습자가 나중에 혼자 다시 보는 교안·인쇄 배포물엔 쓰지 않는다(실무 교안에 이 모드 금지 — 화려함은 가독성과 인쇄를 깎는다). 실무용 덱의 동작·속도는 이 모드와 무관하게 그대로다(`assets/template.html`은 손대지 않는다).

**원칙은 같다.** 템플릿에 디자인을 싣지 않는다 — 이벤트 템플릿에도 톤(색·글꼴 굵기·카드)은 없고 **연출 메커니즘**만 있다. 시안 A/B/C(`references/event_examples/`)는 고정 테마가 아니라 **기법을 뽑아낸 원본**이다. 덱마다 아래 연출 사전에서 기법을 **다르게 조합**한다 — 세 예시 중 하나를 통째로 쓰면 반려 대상이다.

### 이벤트 템플릿에 실린 것 (`assets/template-event.html`)

| 구분 | 스위치·마크업 | 하는 일 |
|---|---|---|
| 엔진 | `⛔` 이후 | `template.html`과 바이트 동일(F·I·N·S, 인쇄, 발표자 스텝 동기화) |
| 무대 | `<body class="ev-stage">` + `<div id="ev-stage">`(첫 장 앞) | 장이 투명해지고 고정 무대가 전 장 뒤에 계속 비친다 — 배경 연출(빛 번짐·오로라·입자)은 여기 그린다. 전환 때 배경이 끊기지 않는다 |
| 디졸브 전환 | `<body class="ev-dissolve">` + `:root { --ev-xf-in; --ev-xf-out; --ev-xfade }` | 밀기 대신 디졸브+줌. **장은 transform만, 페이드는 자식이**(헬퍼가 `.ev-fade`를 붙인다) — 유리 카드 흐림이 전환 중 꺼지지 않는다. `--ev-xfade`는 .6s 이하(엔진 워치독 650ms) |
| 글자·단어 등장 | `data-split`(글자) / `data-split="word"` | `.ev-ch` / `.ev-m > .ev-w`로 쪼개고 순번 `--i`, 개수 `--n`. **애니메이션은 덱 전용 스타일에서 정의** — `animation-delay: calc(var(--d,0s) + var(--i) * 45ms)` |
| 스텝 연동 | `data-step="N"` + `ev-gate` | 상자를 중립으로(이동·전환 없음) → 안쪽 요소의 애니메이션을 `.visible` 뒤에 시작시키는 패턴(`.x.visible .child { animation: … both }`) |
| 레터박스 | 장에 `data-letterbox` | 그 장이 활성일 때 위·아래 띠(`--ev-bar` 7.5% · `--ev-bar-time` 1s · `--ev-bar-color`) |
| 패럴랙스 | `<body class="ev-parallax">` + 요소에 `.ev-par` `--z` | `:root`에 `--px --py`(마우스 + 자동 흔들림 — 녹화 중 마우스가 없어도 움직인다). `--z` 음수 = 뒤층 |
| 입자 | 무대 안 `<canvas class="ev-dust" data-count data-color="r,g,b" data-size data-speed>` | 스프라이트 1장을 찍어 그린다(입자마다 그라데이션 X) |
| 녹화용 UI 숨김 | `H` 키 · `?clean=1` | 진행바·카운터·네비·힌트·페이지 번호 숨김. 발표자 창엔 영향 없음 |
| 계측·정지 | `?fps=1` · `?still=1` | 우상단 fps(5초마다 콘솔 `[ev-fps]`) · rAF 루프 정지(헤드리스 캡처·PDF용) |
| 자동 | — | 화면에 없는 장의 애니메이션 정지 · `prefers-reduced-motion`이면 연출 0.01s · 인쇄 때 무대 숨김·투명 장에 `--tone-bg` 채움 |
| 예시 3장 | `ex-` | 글자별 흐림→선명 + 레터박스 / 잘린 거대 숫자 + 단어별 등장 + 스텝 / 마무리. 실제 덱에서 전부 교체 |

### 절차 — 실무용 6단계 그대로, 다른 점만

1. **재료**: 행사 큐시트·수상 부문·시연 순서·로고·CI색·포스터. **인물 실명·회사명·수치는 사용자가 준 재료에서만** — 없으면 묻거나 `확인 필요`. 공개 레포·샘플에는 넣지 않는다
2. **장별 한 줄 두 개**: "이 장의 그림"(그림 사전 그대로 적용 — 시상 = 이름 하나가 화면 전체, 부문 소개 = 번호 원 사진, 시연 순서 = 타임라인) + **"이 장의 연출"**(연출 사전에서 **1~2개**). 노트 첫 두 줄에 적는다. **같은 연출 3장 연속 금지**(글자별 등장이 이어지면 하나는 단어별·타이핑·조립으로)
3. **레퍼런스**: `references/event_examples/` 3개를 **브라우저에서 실제로 넘겨 본다**(캡처만 보면 타이밍을 모른다). 무엇을 뽑았는지는 아래 사전의 "출처" 열
4. **톤 시안 2~3개**: 분위기 답을 출발점으로, 같은 장면 3장(표지·본문 1·마무리)을 **움직임까지** 만들어 `tone_samples/`에 두고 캡처 비교(`톤비교.html`) + 파일 열어 보기 링크. 세 시안이 배경·전환·등장 조합이 서로 달라야 한다
5. **조립**: `template-event.html` 복사 → `<body>` 스위치 → 무대 → 장. **글은 더 적고 크게**: 한 장에 문장 1~3개, 제목 3~7em, 본문 1.2em 이상. 인쇄·가독성 제약(하단 안전 영역·명암비 4.5:1)은 해제하되 **글자 위에 움직이는 것**은 두지 않는다. 장당 유리 8개 이하
6. **검증**: 실무용 2종 + 아래 "이벤트 검증"

### 연출 사전 — 시안 A(시네마틱 다크)·B(키노트)·C(오로라 글래스)에서 뽑은 기법

색 값은 전부 **그 시안의 예**다. 새 덱은 사용자가 준 색·분위기 답에서 출발한다. 비용: 낮 = 합성만(transform·opacity) · 중 = 큰 반투명 레이어 또는 rAF 1개 · 높 = backdrop-filter·filter 애니메이션·blend.

**배경(무대 — `#ev-stage` 안, 전 장 공유)**

| 기법 | 쓰는 순간 | 그리는 법 | 비용 | 같이 쓰면 안 되는 것 · 출처 |
|---|---|---|---|---|
| 빛 번짐 메시 | 어두운 바탕에 온기·깊이 | `radial-gradient(circle, rgba(강조,.2) 0%, transparent 62%)` 원 3개(80~90vw), `animation: 26s ease-in-out infinite alternate`로 `translate(18vw,22vh) scale(1.15)`. `will-change: transform` | 낮 | 밝은 바탕(안 보임) · A(예 금 `rgba(255,181,71,.20)` + 보조 파랑 `rgba(58,85,255,.22)`) |
| 오로라 | 몽환·유리와 짝 | 블롭 4개(위 메시와 같은 원리, 알파 .35~.55) + **리본 2개**: `width:140vw; height:38vh; mask-image: radial-gradient(ellipse 50% 50%, #000, transparent 70%)`에 가로 그라데이션, `rotate(-8deg→6deg) translateX scaleY(.7→1.2)` 18~23s alternate + 중앙 흰 하이라이트 | 중 | 입자·필름 질감(밝은 바탕에서 지저분) · C(예 청록 `#10BFAE` + 보라 `#7152FF`) |
| 입자(먼지) | 어두운 무대의 공기감 | `<canvas class="ev-dust" data-count="110" data-color="255,226,176">` | 중(rAF 1) | 밝은 바탕 · 패럴랙스와 겹치면 rAF 2개 → 계측 필수 · A |
| 필름 질감 | 영화 느낌 | SVG `feTurbulence` data URI 타일, `opacity:.07; mix-blend-mode: overlay; inset:-50%`, `steps(5) .8s` 흔들림 | 높(blend) | 유리·밝은 바탕 · 무대에 1장만 · A |
| 빛줄기 | 표지 뒤 조명 | `conic-gradient(from 180deg, transparent 0 40%, rgba(255,210,150,.07) 44%, transparent 47%, …)` 340vh 원, `rotate 40s linear infinite` | 낮 | — · A |
| 비네트 | 가장자리 어둡게 → 중앙 집중 | `radial-gradient(ellipse 75% 70% at 50% 50%, transparent 55%, rgba(0,0,0,.75))` 고정 레이어 | 0 | 밝은 바탕 · A |
| 거대 구체(잘림) | 밝고 대담한 표지 | 34em 원을 `right:-9em`으로 화면 밖까지, `radial-gradient` 3겹(하이라이트·두 색) + 그림자 레이어, 안쪽 채움만 `rotate 14s linear infinite`. 장에 `overflow:hidden` | 낮 | 유리(경계가 흐려짐) · B(예 `#2E5BFF→#A146FF` + 하이라이트 `#FF7BC2`) |
| 유리 구슬 | 유리 덱의 뒤층 장식 | 원에 `radial-gradient(circle at 32% 28%, rgba(255,255,255,.95), … .08 55%)` + 틴트 + `backdrop-filter: blur(6px)` + `translateY(-.6em)` 5~8s 부유. 패럴랙스 뒤층(`--z:-2`) | 높 | 장당 3개 이하 · C |

**등장(텍스트·요소)**

| 기법 | 쓰는 순간 | 그리는 법 | 비용 | 같이 쓰면 안 되는 것 · 출처 |
|---|---|---|---|---|
| 글자별 흐림→선명 | 표지 제목·마무리 한 문장(**20자 이내**) | `data-split` + `.is-active [data-split] .ev-ch { animation: ch 1.1s cubic-bezier(.2,.7,.2,1) both; animation-delay: calc(var(--d,0s) + var(--i)*45ms) }` `@keyframes ch { from { opacity:0; filter: blur(14px); transform: translateY(.25em) scale(1.15) } }` | 중(글자 수만큼 filter) | `background-clip:text` 그라데이션(글자마다 끊긴다 → 단색 + `text-shadow` 발광) · 긴 문단 · A |
| 단어별 밀어 올리기 | 큰 제목·목차·결론 | `data-split="word"` + `.ev-w { animation: up 1s cubic-bezier(.16,.9,.2,1) both; animation-delay: calc(var(--d,.35s) + var(--i)*90ms) }` `@keyframes up { from { transform: translateY(115%) } }`. 마스크 `.ev-m`이 잘라 준다. 스텝 안이면 `[data-step].visible [data-split="word"] .ev-w` | 낮 | 글자별과 한 장에 같이 · B |
| 자간 조이기 | 킥커·라벨(대문자 자간 .5em) | `@keyframes track { from { opacity:0; letter-spacing:1.4em; filter: blur(6px) } }` 1.4s | 낮 | 본문 · A |
| 떠오르기 | 범용(보조 문장·카드) | `@keyframes rise { from { opacity:0; transform: translateY(1.2em); filter: blur(8px) } }` 1.2s, 요소마다 `--d` 0.15s 간격 | 낮 | — · A |
| 타이핑 | 한 줄 문장(프롬프트·대사) | `white-space:nowrap; overflow:hidden` + `@keyframes type { from { clip-path: inset(0 100% 0 0) } to { clip-path: inset(0) } }` `steps(22, end)` 1.1s | 낮 | 두 줄 이상 · C |
| 선 그리기 | 연결선·궤적·트랙 | SVG `pathLength="1"` + `stroke-dasharray:1; stroke-dashoffset:1` → `0`(animation 또는 transition 1s `cubic-bezier(.6,0,.2,1)`). 스텝 구간별로는 `.flow:has(.st[data-step="2"].visible) .seg2 { stroke-dashoffset:0 }` | 낮 | — · A·B·C |
| 조립(별자리·케이블) | 요소 N개가 하나로 모이는 메시지(구성 요소·부문) | 허브 1개 + `data-step` 묶음마다: 선 그리기(0→1s) → 점 팝(`scale 0→1.8→1` .9s, `.75s + --k*.15s`) → 라벨 떠오르기(.9s+). C는 칩→케이블→창에 타이핑 | 낮~중 | 한 장에 두 조립 · A·C |
| 팝 | 칩·배지·점·CTA | `@keyframes pop { from { opacity:0; transform: scale(.4) } }` `.9s cubic-bezier(.2,.9,.3,1.4)`(오버슈트) | 낮 | 큰 면(카드 전체) · C |
| 3D 카드 진입 | 카드 2~4장 | 부모 `perspective:1800px`, `@keyframes in { from { opacity:0; transform: translateY(5em) rotateX(45deg) rotateY(var(--ry)) } }` 1.3s, 바깥 카드일수록 `--ry` ±10~16deg | 중(유리면 높) | 유리 + 패럴랙스 + 3D 셋 다 · C |
| 격자선 자라기 | 표·격자에 단어를 끼울 때 | 선마다 `transform-origin: left/top` + `@keyframes grow { from { transform: scaleX(0) } }` 1.2s `cubic-bezier(.7,0,.2,1)`, 선끼리 .1s 간격 | 낮 | — · B |
| 빛 쓸기(sheen) | 표지 제목 위 광택(반복) | `::after { content: attr(data-text); background: linear-gradient(105deg, transparent 38%, rgba(255,255,255,.95) 50%, transparent 62%); background-size: 250% 100%; background-clip: text; color: transparent }` `background-position 130%→-30%` 5.5s 반복 | 낮 | 본문 · 한 장에 1개 · A |
| 플레어 라인 | 표지 밑줄·CTA 밑 | 2px 선 `scaleX(0→1)` 1.6s + 중심 원 `radial-gradient` `scale(0→1.4→1)` + `pulse 4s infinite`, `box-shadow: 0 0 18px 2px rgba(강조,.6)` | 낮 | — · A |
| 충격파 | 점이 켜지는 순간 | `::after` 원 테두리 `@keyframes shock { from { transform: scale(.6); opacity:1 } to { transform: scale(2.4); opacity:0 } }` 1.4s | 낮 | — · A |
| 혜성 | 궤적 완성 뒤 장식 | 7em 그라데이션 막대 `translateX(-7em → 53em)` 3.2s infinite, `filter: blur(1px)` | 낮 | 완성 전 · A |

**전환(장 사이)**

| 기법 | 쓰는 순간 | 그리는 법 | 비용 | 같이 쓰면 안 되는 것 · 출처 |
|---|---|---|---|---|
| 밀기(기본) | 흰·불투명 장 | 엔진 기본(translateX .5s). 스위치 없음 | 낮 | — · B |
| 밀기 + 후퇴 | 밀기에 깊이 | `.slide.edu { transition: transform .6s cubic-bezier(.77,0,.18,1), opacity .6s }` `.exit-left { transform: translateX(-26%) scale(.94); opacity:0 }` + `.is-active { box-shadow: ±3em 0 6em rgba(…,.1) }` | 낮 | **유리가 있는 덱**(장 opacity) · B |
| 디졸브 + 줌 | 어두운 무대 위 장면 전환 | `body.ev-dissolve` + `--ev-xf-in: scale(1.05); --ev-xf-out: scale(.96)` | 낮 | `--ev-xfade` > .6s · A |
| 깊이에서 떠오르기 | 유리·몽환 | `body.ev-dissolve` + `--ev-xf-in: translateY(4%) scale(.93); --ev-xf-out: scale(1.1)` | 낮 | — · C |
| 레터박스 | 표지·마무리·시상 순간 | 장에 `data-letterbox` | 0 | 본문 장 전부에(효과가 죽는다) · A |

**재질**

| 기법 | 쓰는 순간 | 그리는 법 | 비용 | 같이 쓰면 안 되는 것 · 출처 |
|---|---|---|---|---|
| 유리 카드 | 오로라·사진 무대 위 패널 | `background: linear-gradient(140deg, rgba(255,255,255,.62), rgba(255,255,255,.26)); border: 1.5px solid rgba(255,255,255,.78); backdrop-filter: blur(22px) saturate(1.6); box-shadow: 0 1.6em 3.2em -1.2em rgba(…,.28), inset 0 1px 0 rgba(255,255,255,.95)` | 높 | **조상에 opacity<1·filter·mask·clip-path·mix-blend-mode**(아래 "유리 규칙") · 장당 8개 초과 · blur 24px 초과 · C |
| 기울임(3D) | 카드 줄에 원근 | 부모 `perspective`, 카드 `transform: rotateY(var(--ry))`, 바깥일수록 큰 각 | 낮(유리면 높) | 4장 초과 · C |
| 패럴랙스 | 표지·마무리의 층 | `body.ev-parallax` + 층마다 `.ev-par` `--z`(-2 뒤 · 1 중간 · 3 앞). 판 자체는 `rotateY(calc(var(--px,0) * 5deg))` | 낮(rAF 1) | 본문 장 전부(멀미) · C |
| 발광 | 다크의 강조(금·네온) | `text-shadow: 0 0 .6em rgba(강조,.55), 0 0 1.6em rgba(강조,.25)` / `box-shadow` 같은 값 | 낮~중 | 밝은 바탕 · A |
| 외곽선 숫자 | 목차·순서의 큰 번호 | `color: transparent; -webkit-text-stroke: 1.5px rgba(강조,.85); text-shadow: 0 0 .35em rgba(강조,.25)` 6em+ | 낮 | 본문 크기 · A |
| 그라데이션 글자 | 한 단어 강조 | `background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent`. 한 글자 숫자는 `letter-spacing:0; padding:0 .06em; margin:0 -.06em`(음수 자간이면 오른쪽이 잘린다) | 낮 | 글자별 쪼개기(단어별까지만) · B·C |

**타이포**

| 기법 | 쓰는 순간 | 그리는 법 | 비용 | 같이 쓰면 안 되는 것 · 출처 |
|---|---|---|---|---|
| 초대형 제목 | 표지·마무리 | 7.4em · weight 800 · `letter-spacing: -.06em` · `line-height: 1.02`. 한 장에 단어 2~4개 | 0 | 두 줄 초과 · B |
| 잘린 거대 숫자 | 목차·순서·"올해의 숫자" | 19~22em, `position:absolute; bottom:-.32em`, 장 `overflow:hidden`, 등장은 `translateY(60%)→0` 1.3s | 0 | 글자 위에 겹치기 · B |
| 자간 넓힌 라벨 | 킥커·챕터 표시 | `.78em; letter-spacing: .5em; text-transform: uppercase`(한글은 .3em) | 0 | 본문 · A |
| 얇은 부제 | 표지 제목 위 한 줄 | weight 300 · `letter-spacing: .3em` · 1.55em | 0 | 밝은 바탕에서 300은 명암비 확인 · A |
| 한 단어 강조 | 결론 문장 | 문장 속 한 단어만 강조색 또는 그라데이션 글자 | 0 | 두 단어 이상 · A·B·C |

### 유리 규칙 — 전환 중 흐림이 꺼졌다 튀던 원인

시안 C에서 장을 넘길 때 0.6초 동안 유리 카드 뒤가 선명해졌다가 끝에 다시 흐려지며 튀었다. 원인은 **장(`.slide`)에 `opacity: 0→1` 전환을 건 것**이다. `opacity < 1`(그리고 `filter` `mask` `clip-path` `mix-blend-mode`)인 조상은 **backdrop root**가 되어, 그 안의 `backdrop-filter`는 조상 바깥(무대)을 못 보고 조상 안(투명한 장)만 흐린다 → 흐림이 없어졌다가 `opacity`가 1이 되는 순간 되돌아온다. 실측(260929, 줄무늬 무대를 깔고 전환 중간에 멈춰 캡처): 옛 시안은 유리 뒤 줄무늬가 선명, 새 메커니즘은 흐림 유지.

- 템플릿의 `ev-dissolve`는 그래서 **장은 transform만, 페이드는 자식**에게 건다. 헬퍼가 유리를 품은 조상을 건너뛰고 그 안쪽에 `.ev-fade`를 붙이므로 유리 요소는 **자기 opacity만** 바뀐다(자기 자신의 opacity는 괜찮다)
- 덱에서도 같은 규칙: 유리 요소의 **조상**에 opacity·filter·mask·clip-path·blend를 걸지 않는다 — 전환·등장 애니메이션·패럴랙스 래퍼 전부. 등장은 유리 요소 자신에게(`.c-card { animation: … }` OK) 또는 transform만으로
- 장 자체를 페이드하는 전환(밀기+후퇴의 `opacity:0`)은 유리 없는 덱에서만
- `transform`은 backdrop root가 아니다 — 패럴랙스(`.ev-par`)·줌·3D 회전은 유리와 같이 써도 된다(실측)

### 성능 규칙

- 장당 `backdrop-filter` 8개 이하, `blur()` 24px 이하, 유리끼리 겹치지 않게
- 무한 애니메이션은 무대에만. 장 안의 무한은 2개 이하(펄스·혜성·링 회전 중 택)
- `filter: blur()` 애니메이션은 글자 20자 이내(글자별 등장) — 문단에 쓰지 않는다
- `mix-blend-mode` 레이어는 무대에 1장 이하
- rAF 루프(입자·패럴랙스)는 합쳐서 2개 이하. 둘 다 켜면 `?fps=1`로 확인
- 실측(260929, MacBook M5 · Chrome · 1280×800 창): C(유리 10개 + 오로라 6층 + 패럴랙스) 평균 60fps·최저 55 / A(입자 110 + 메시 3 + 빛줄기 + 질감) 평균 60. 1920×1080 전체화면·다른 기기는 미실측 — 행사 당일 장비에서 `?fps=1`로 한 번 돌려 본다

### 이벤트 검증 (실무용 2종에 더해)

- **타이밍**: 각 장 첫 진입 연출이 3초 안에 끝나 **정지 상태**가 생긴다(녹화 컷 포인트) · `data-step` 클릭마다 **한 묶음만** 움직인다 — 헤드리스로 스텝별 캡처: 복사본에 `[data-step]{opacity:1!important}` 대신 `.visible`을 붙여 가며 찍거나, 브라우저에서 →키로 직접 본다
- **녹화 UI**: `?clean=1`(또는 H)로 진행바·카운터·네비·힌트·페이지 번호가 전부 사라지는지 캡처 1장
- **발표자 창**: `S`로 열어 미리보기가 보이는지(디졸브 덱은 클론이 `.ev-fade` 규칙에 걸리지 않게 템플릿이 처리한다 — 덱에서 `.slide` opacity를 건드렸으면 여기서 깨진다)
- **콘솔 0 · PDF 페이지 수 = 장수**(무대는 안 찍히므로 `@media print .slide.edu { background: … }`로 정지 배경을 준다 · `:has(.visible)`로 켜지는 것은 print에서 직접 켠다)
- **프레임**: `deck.html?fps=1`을 **활성 창**에서 열고 전 장을 넘기며 우상단 값을 본다(백그라운드 탭은 rAF가 멈춰 0이 찍힌다). 기준: 평균 55 이상·최저 45 이상. 콘솔 `[ev-fps]` 줄로 기록. 실측 못 했으면 산출물 보고에 "프레임 미실측"이라고 쓴다
- **reduced motion**: 시스템 설정을 켜고 한 번 넘겨 본다 — 연출이 0.01s로 줄고 내용은 전부 보여야 한다
- **헤드리스 캡처는 `?still=1`을 붙인다** — rAF 루프(입자·패럴랙스)가 돌면 가상 시간이 소진돼 등장 애니메이션이 끝나기 전에 찍힌다(260929 실측: 제목이 흐린 채 캡처됨). 명령:

```bash
"$C" --headless=new --hide-scrollbars --window-size=1280,720 --virtual-time-budget=5000 --screenshot=sN.png "file://$PWD/덱.html?still=1#slide-N"
"$C" --headless=new --no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf=덱.pdf "file://$PWD/덱.html?still=1"
```

### 예시 (`references/event_examples/`) — 보고 배우되 복사하지 않는다

같은 5장(표지·목차·6요소·4단계·마무리)을 세 연출로 만든 것. 현재 엔진(1.6.1 발표자 스텝) + 이벤트 템플릿으로 옮겼고 내용은 중립이다. 어느 장이 어떤 기법인지는 각 장 노트 첫 줄 "이 장의 연출".

| 파일 | 조합 | 배울 것 |
|---|---|---|
| `event_a_cinematic_dark.html` | 무대(메시+빛줄기+입자+질감+비네트) · 디졸브+줌 · 레터박스 · 글자별 흐림→선명 · 별자리 조립 · 빛의 궤적 | 어두운 무대에서 "빛"으로만 강조하는 법, 스텝과 선 그리기 연동 |
| `event_b_keynote_light.html` | 무대 없음 · 밀기+후퇴 · 단어별 밀어 올리기 · 잘린 거대 숫자·구체 · 격자선 자라기 | 흰 바탕에서 크기와 잘림만으로 대담해지는 법(연출 비용 거의 0) |
| `event_c_aurora_glass.html` | 오로라 무대 · 깊이에서 떠오르는 디졸브 · 패럴랙스 3층 · 유리 카드·구슬 · 3D 진입 · 케이블+타이핑 조립 | 유리 규칙(조상 opacity 금지)과 패럴랙스 층 나누기 |

### 이벤트 모드 함정

- 헬퍼는 `<body>` 스위치 클래스를 **로드 시 한 번** 읽는다 — 나중에 클래스를 붙여도 `.ev-fade`·패럴랙스는 안 켜진다
- `data-split` 안에 또 `data-split`을 넣지 않는다 · 쪼갠 뒤 `innerHTML`을 바꾸면 조각이 사라진다
- 무대 위 요소를 장 안에서 `position:absolute; inset:0` 래퍼로 감쌀 때 래퍼는 `pointer-events`를 막지 않는다(네비 버튼은 z-index 100이라 괜찮다) — 단 래퍼에 opacity 애니메이션을 걸면 안의 유리가 깨진다(유리 규칙)
- 엔진 UI(`#kbdHint` 등)를 톤에 맞춰 덮어쓰는 건 되지만 **숨기지는 않는다** — 녹화 때만 `H`
- 무대 `#ev-stage`는 `body.ev-stage` 없이는 장 뒤에 가려진다(장이 불투명) — 둘은 세트
- **디졸브 퇴장 때 진입 애니메이션 요소만 툭 사라짐** — `.is-active .x { animation … both }`처럼 진입을 `is-active`에만 걸면 장을 떠날 때 애니메이션이 즉시 제거돼 `.ev-fade` 페이드가 시작도 못 한다. 선택자를 `.is-active .x, .exit-left .x, .exit-right .x`로 쓰거나 진입 애니메이션을 안쪽 요소에 건다(1.7.0 리뷰 실측)
- **발표자 미리보기는 무대가 없다** — `ev-stage` 덱의 미리보기 배경은 템플릿이 `--tone-bg`로 채운다. 목차·힌트 등 엔진 UI 색이 다크 무대와 안 맞으면 덱 전용 스타일에서 `--bg` `--surface` `--text-*`를 덮어써도 된다(이벤트 모드에서만 허용)

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
  - 방향키는 관객 창의 `advance()`/`retreat()`를 그대로 실행 — **빌드 스텝(`data-step`)도 관객 창과 똑같이 하나씩** 공개된다. `Home`/`End`만 슬라이드 단위. `Esc`로 창 닫기
- 동기화 프로토콜: 발표자 창 화살표 → `{type:'advance'|'retreat'}` 발신 → 메인 창이 실행하고 슬라이드가 바뀌면 `{type:'goto', index}`로 답신. 발표자 창 최초 로드 시
  `{type:'request-state'}`로 메인 창의 현재 위치를 받아 온다. 메인 창 없이 발표자 창만 열렸으면 슬라이드 단위로 자체 이동
- 팝업 차단 시 허용 안내 alert 표시

---

## 슬라이드 HTML 구조 패턴 (교육 장)

```html
<section class="slide edu" id="slide-4" data-title="목차에 표시될 제목" data-chapter="1">
  <div class="cs-title"><small>1부 · 챕터명</small><h2>학습자 말투의 제목</h2></div>
  <!-- 이 장의 그림 — 덱 전용 스타일(cs-…)로 그린 시각 앵커 하나 -->
  <div class="cs-timeline">…</div>
  <div class="cs-band" data-step="1">하단 결론 한 문장</div>
  <aside class="notes">이 장의 그림: 타임라인 위 실루엣, 없는 건 점선+?<br>여는 멘트: "…"<br>강조: …<br>전환: "…"</aside>
</section>
```

- 엔진의 범용 클래스(`.slide__content` `.slide__title` `.cards` `.card` `.code-block`)는 교육 장에서 쓰지 않는다 — 그건 엔진 UI(발표자 창 등)와 옛 범용 덱용이다

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
  #progressBar, #slideCounter, .nav-btn, #kbdHint, #tocOverlay, #notesPanel, #presenterMode { display: none !important; }
}
```

---

## 필수 포함 요소 체크리스트

- [ ] `position: fixed; inset: 0` + **불투명 배경** 슬라이드 레이아웃 (이벤트 모드 `ev-stage`에서만 해제 — 무대가 대신 가린다)
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
- [ ] 톤 시안을 먼저 보여주고 골랐다(사용자가 톤을 줬으면 그 톤 + 대안 1개) · 레퍼런스 라이브러리가 있으면 2~3장을 직접 봤다
- [ ] 전 장 캡처에서 글을 가리고 봐도 메시지가 보인다
- [ ] 교육 규칙은 요청에 맞는 것만 — 챕터가 있으면 `data-chapter` 색 쌍, 챕터 끝엔 정리 장 검토
- [ ] `:root` `--tone-*`을 시안 값으로 채웠다(자리표시 회색 그대로 아님) · 검증용 예시 3장과 `ex-` CSS 전부 교체
- [ ] 각 장 노트 첫 줄에 "이 장의 그림:" 한 줄 · 하단 안전 영역(좌·우 하단 모서리, 중앙 페이지 번호) 침범 없음
- [ ] 사진은 원형 꽉 채움 또는 `.fade-up` — 사각 사진·이모지 큰 슬롯 없음
- [ ] 전 장 캡처 확인 · PDF 페이지 수 = 슬라이드 수(zlib 계수) · 콘솔 에러 0
- [ ] 빈칸 슬라이드가 있으면 정답 없는 배포용 PDF도 뽑을지 확인 — 필요하면 덱 전용 스타일에 `@media print`에서 정답을 숨기는 규칙 추가
- [ ] 파일명 `{주제}_슬라이드_{YYMMDD}.html`
- [ ] (이벤트 모드) 모드·분위기를 물었다(요청에 드러났으면 생략) · `template-event.html`에서 시작 · 장마다 "이 장의 연출" 한 줄, 장당 기법 1~2개, 같은 연출 3장 연속 없음 · 예시 3개 중 하나를 통째로 쓰지 않았다
- [ ] (이벤트 모드) 유리 조상에 opacity·filter·mask 없음 · 장당 유리 8개 이하 · `--ev-xfade` ≤ .6s · 헤드리스 캡처는 `?still=1` · `?clean=1` 캡처 · `?fps=1` 실측(못 했으면 "미실측" 명기) · 인쇄용 정지 배경

---

## 주의사항 (재발 버그 목록)

- `scale()` 기반 고정 캔버스 방식 사용 금지 — 반응형 깨짐, 텍스트 흐림 발생
- `getBoundingClientRect()` reflow 줄을 절대 생략하지 말 것 — 없으면 첫 전환이 순간이동
- `transitionend` 핸들러는 `e.target !== nextSlide || e.propertyName !== 'transform'` 체크 필수
  (자식 요소 이벤트 버블링 오발 방지) + **워치독 타이머 병행** (탭 숨김 시 이벤트 유실 → 덱 영구 잠김)
- 전환 정리 시 prev의 transition을 끄지 않으면 **유령 슬라이드**가 화면을 가로지른다
  (특히 슬라이드 배경이 반투명이면 그대로 노출)
- `.slide`에 불투명 `background` 누락 금지 — 뒤에서 정리되는 슬라이드가 비쳐 보임 (이벤트 모드 `body.ev-stage`만 예외 — 고정 무대가 뒤를 가린다)
- URL 해시는 `location.hash` 직접 대입 대신 `history.replaceState` 사용 — 히스토리 오염 + `hashchange` 루프 방지
- **발표자 창 화살표가 슬라이드 단위(`pmSet`)로 가면 빌드 스텝이 통째로 건너뛰어진다** — 관객 창의 `advance()`/`retreat()`를 메시지로 호출해야 한다(1.6.1, 260928. 한민님: "발표자 모드로 넘기면 순차 애니메이션이 생략된 채로 다음 장으로")
- 발표자 모드 단축키는 **S** — P를 쓰면 `Cmd+P` 인쇄와 충돌한 전례가 있다. 키 핸들러 첫 줄에서
  meta/ctrl/alt 조합을 반드시 무시할 것
- 발표자 미리보기 클론(`.pm-scale .slide`)에는 `color: var(--text-primary)` 필수 — 없으면 발표자 창의 흰 글자색을
  상속해 제목이 안 보인다
- 발표자 UI에서 덱을 숨길 때는 `body.is-presenter > .slide` (직계 자식 선택자) — 후손 선택자로 쓰면
  미리보기 클론까지 숨겨진다
- `@page { size }` 없이 인쇄하면 fixed 슬라이드가 겹쳐 **PDF가 1장만 나온다**
- (이벤트) **`.slide`에 opacity 전환 + 안에 `backdrop-filter`** → 전환 중 유리 흐림이 꺼졌다 튄다(backdrop root). 장은 transform만, 페이드는 자식(`ev-dissolve`)
- (이벤트) `.slide` transition을 .6s보다 길게 주면 엔진 워치독(650ms)이 먼저 정리해 나가는 장이 뚝 끊긴다
- (이벤트) rAF 루프가 도는 덱을 헤드리스로 찍으면 등장 애니메이션이 끝나기 전에 찍힌다 → `?still=1` · 백그라운드 탭에서는 rAF가 멈춰 fps가 0으로 찍힌다 → 활성 창에서 계측
- 엔진 UI 목록(`.slide__list`, 목차 오버레이)의 dot 정렬은 `align-items: center`(`flex-start` + `margin-top`은 폰트 크기 바뀌면 틀어짐). **덱 본문의 불릿은 flex를 쓰지 않는다**(위 "부품 사용 주의") — 두 규칙은 대상이 다르다
