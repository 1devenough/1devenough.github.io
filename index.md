---
layout: splash
hidden: true
title: "1인 개발 워크플로우를 위한 핵심 도구와 정보"

header:
  overlay_color: "transparent" # 배경 오버레이를 투명하게 설정
  #overlay_filter: "0.5"
  #overlay_image: /assets/images/index/splash_background.jpg
  caption: # "1인 개발자를 위한 모든 것"
  cta:
    label: "Get Started"
    url: "/archive/"

excerpt: "코딩, 디자인, 마케팅의 실용적인 팁과 리소스를 탐색하세요."
  
feature_row:
  - image_path: /assets/images/common/lightbulb-solid-full.svg
    title: "인사이트"
    excerpt: "사례 연구, 비즈니스 전략, 마인드셋 등 1인 개발의 'Why'와 'What'을 다룹니다."
    url: "/insights/"
    btn_label: "더 알아보기"  
  - image_path: /assets/images/common/code-solid-full.svg
    title: "코딩"
    excerpt: "개발 팁, 프레임워크, 유용한 정보들을 아카이빙합니다."
    url: "/coding/"
    btn_label: "더 알아보기"
    disabled: false
  - image_path: /assets/images/common/palette-solid-full.svg
    title: "디자인"
    excerpt: "1인 개발자를 위한 UI/UX 디자인 팁과 리소스 모음입니다."
    url: "/design/"
    btn_label: "더 알아보기"
    disabled: false
  - image_path: /assets/images/common/chart-simple-solid-full.svg
    title: "마케팅"
    excerpt: "내 앱을 알리고 사용자를 모으는 방법, 마케팅 전략입니다."
    url: "/marketing/"
    btn_label: "더 알아보기"
    disabled: true
---

{% include feature_row %}

<hr>

<div class="latest-posts-row" style="margin-bottom: 2em;">
  <h2 class="archive__subtitle" style="margin-top: 2em;">최신 글</h2>

  <div class="archive">
    {% for post in site.posts limit:5 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>

  <p style="text-align: right; margin-top: 1em;">
    <a href="/archive/" class="btn btn--primary">
      모든 글 보러가기 &rarr;
    </a>
  </p>
</div>
