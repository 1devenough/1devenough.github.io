---
name: jekyll-kramdown-markdown-in-html-parsing
description: Jekyll의 Kramdown 파서가 HTML 블록(<div markdown="1">) 내부의 마크다운을 올바르게 렌더링하도록 하는 규칙
keywords: jekyll, kramdown, markdown, html, markdown="1", markdown in div, jekyll 탭 마크다운, kramdown 파싱, 들여쓰기, indentation, 빈 줄, blank line, code block
---

## 📌 문제 (Problem) / 핵심 (Core)
Jekyll(Kramdown) 환경에서 `div`와 같은 HTML 블록에 `markdown="1"` 속성을 부여했음에도 불구하고, 내부의 마크다운(`###`, `*` 등)이 올바르게 렌더링되지 않습니다.

* **증상 1:** 마크다운이 단순 텍스트나 HTML 코드로 노출됩니다.
* **증상 2:** 마크다운이 들여쓰기된 **코드 블록**으로 렌더링됩니다.
* **증상 3:** 닫는 태그(`</div>`)가 텍스트로 노출되거나, HTML 구조가 깨져 레이아웃이 망가집니다. (예: 숨겨져야 할 탭 콘텐츠가 모두 보임)

## 💡 원인 / 맥락 (Context)
Kramdown 파서는 `markdown="1"` 속성이 지정된 HTML 블록을 처리할 때 매우 엄격한 규칙을 따릅니다. 이 규칙을 하나라도 어기면 파서가 마크다운과 HTML을 구분하지 못하고 오류를 발생시킵니다.

1.  **코드 블록 증상 (증상 2):** `<div>` 내부의 마크다운 콘텐츠가 **들여쓰기(indentation)** 되어 있으면, Kramdown은 이 내용을 `markdown="1"` 속성보다 우선하여 '코드 블록'으로 강제 처리합니다.
2.  **레이아웃 깨짐 (증상 3):** 마크다운 콘텐츠(특히 리스트)가 닫는 `</div>` 태그와 **빈 줄 없이** 붙어있으면, Kramdown은 `</div>`를 HTML 태그가 아닌 마크다운 리스트의 일부 텍스트로 오인합니다. 그 결과 `div`가 닫히지 않아 전체 HTML 구조가 깨집니다.

## ✅ 해결책 / 지침 (Solution / Rule)
Kramdown이 HTML 내부의 마크다운을 올바르게 파싱하게 하려면, 다음 **세 가지 규칙을 모두** 지켜야 합니다.

1.  **`markdown="1"` 속성 사용:** 마크다운 파싱을 원하는 HTML 블록 태그에 `markdown="1"` 속성을 추가합니다.
2.  **들여쓰기 절대 금지:** `<div>` 내부의 마크다운 콘텐츠는 **절대 들여쓰기(indent)하면 안 됩니다.** 모든 `###`, `*`, 텍스트는 0번째 칸에서 시작해야 합니다.
3.  **콘텐츠 상/하단에 빈 줄 확보:** 마크다운 콘텐츠의 **시작(여는 태그 직후)과 끝(닫는 태그 직전)에 반드시 빈 줄(blank line)을 추가**하여 파서가 HTML과 마크다운 영역을 명확히 구분하도록 해야 합니다.

---

### 올바른 예시 (Good)

```html
<div class="tab-pane" markdown="1">

### 📖 1. 핵심 전략 분석
여기에 마크다운을 작성합니다.

* 글머리 기호도
* 들여쓰기 없이 작성합니다.

</div>
```

### 잘못된 예시 (Bad)

```html
<div class="tab-pane" markdown="1">

    ### 📖 1. 핵심 전략 분석
    
    * 들여쓰기가 되어 파싱 실패

</div>

<div class="tab-pane" markdown="1">
### 📖 1. 핵심 전략 분석
* ...
* 마지막 리스트
</div>
```
