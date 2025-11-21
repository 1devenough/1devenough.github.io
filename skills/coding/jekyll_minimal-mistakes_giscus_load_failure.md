---
name: jekyll-minimal-mistakes-giscus-hybrid-fix
description: Minimal Mistakes 테마에서 Giscus 설정이 모두 올바름(200 OK)에도 불구하고 댓글 창이 로드되지 않는 '고스트 버그'를 커스텀 `_includes/comments.html` 파일로 해결하는 방법
keywords: jekyll, giscus, minimal mistakes, comments, 200 OK, empty iframe, load failure, ghost bug, _config.yml, _includes/comments.html, realcoding.blog
---

## 📌 문제 (Problem) / 핵심 (Core)
Jekyll Minimal Mistakes 테마에서 Giscus 댓글을 연동할 때, 아래 조건을 모두 만족했음에도 불구하고 "COMMENTS" 섹션 아래에 Giscus 댓글 창이 로드되지 않고 빈 화면만 표시됩니다.

1.  `_config.yml`에 `comments: provider: giscus` 및 `repo`, `repo_id` 등 모든 Giscus 설정이 올바르게 기재되어 있습니다.
2.  GitHub 저장소에 Giscus 앱 설치 및 Discussions 기능 활성화 등 모든 백엔드 설정을 완료했습니다.
3.  포스트(`*.md`)의 YAML Front Matter에 `comments: true`가 설정되어 있습니다.
4.  브라우저 개발자 도구 Network 탭에서 Giscus 요청이 `Status Code: 200 OK`로 성공합니다.

## 💡 원인 / 맥락 (Context)
이 '고스트 버그'는 테마가 `_config.yml`을 읽어 Giscus 스크립트 태그를 *자동으로 생성*하는 내부 로직에서 알 수 없는 이유로 **조용히 실패(fail silently)**하기 때문에 발생합니다.

`layout: single`은 `comments: true` 플래그와 `_config.yml`의 `provider: giscus`를 보고 **테마의 내장 댓글 로직**을 실행하려 하지만, 이 로직이 실패하면서 Giscus가 로드되지 않습니다.

## ✅ 해결책 / 지침 (Solution / Rule)
테마의 내장 로직을 우회하는 **'하이브리드' 방식**을 사용합니다. `_config.yml` 설정은 유지하되, 테마의 기본 `comments.html` 파일을 **우리가 만든 커스텀 파일로 덮어쓰기(override)**하여 Giscus 스크립트를 수동으로 삽입합니다.

1.  **`_config.yml` 유지:** `comments:` 블록(`provider: giscus` 및 모든 `repo` 정보 포함)을 `_config.yml`에 **그대로 유지합니다**. 이 설정이 있어야 `layout: single`이 댓글 로드를 시도합니다.
2.  **포스트 `comments: true` 유지:** 댓글을 표시할 포스트(`*.md`)에 `comments: true` 플래그를 **반드시 유지합니다**.
3.  **`_includes/comments.html` 커스텀 생성:**
    `_includes` 폴더에 `comments.html` 파일을 **직접 생성**합니다. (Minimal Mistakes 테마의 기본 파일을 덮어쓰게 됩니다.)
4.  **Giscus 스크립트 하드코딩:** 생성한 `_includes/comments.html` 파일에 `_config.yml`의 값을 참조하여 Giscus 스크립트 태그 전체를 다음과 같이 직접 붙여넣습니다:

    ```html
    <div class="comments-section" style="margin-top: 2em;">
      <script src="[https://giscus.app/client.js](https://giscus.app/client.js)"
              
              data-repo="[Your-User]/[Your-Repo]"
              data-repo-id="[Your-Repo-ID]"
              data-category="[Your-Category-Name]"
              data-category-id="[Your-Category-ID]"
              
              data-mapping="pathname"
              data-strict="0"
              data-reactions-enabled="1"
              data-emit-metadata="0"
              data-input-position="bottom"
              data-theme="preferred_color_scheme"
              data-lang="ko"
              crossorigin="anonymous"
              async>
      </script>
    </div>
    ```
5.  **`.md` 파일에 직접 include comments 기재하지 않는다:** 포스트 본문(`*.md`)에는 `{% include comments.html %}` 태그를 ** 추가하지 않습니다**. `layout: single`이 `comments: true` 플래그를 보고 자동으로 이 파일을 삽입해 줍니다.
