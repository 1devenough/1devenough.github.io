---
#################################################################
# 1. LAYOUT & HEADER
#################################################################
layout: splash
hidden: true

# 페이지 제목 (splash 레이아웃의 Hero 영역에 표시됨)
title: "디자인 허브"

# 페이지 부제목 (splash 레이아웃의 Hero 영역에 표시됨)
excerpt: "1인 개발자를 위한 실용적인 UI/UX 팁, 리소스, 워크플로우 큐레이션."

# Page Header
header:
  overlay_color: "transparent"
  # overlay_image: /assets/images/design-hero.jpg # (Optional)
  caption: # "Category"
  title: "디자인 허브"
  excerpt: "1인 개발자를 위한 실용적인 UI/UX 팁, 리소스, 워크플로우 큐레이션."

#################################################################
# 2. "START HERE" (Curated Picks)
# _includes/curated_row.html 이 데이터를 사용함
#################################################################
curated_title: "시작 가이드: 추천 워크플로우"
curated_picks:
  - title: "AI로 기획부터 디자인 시스템까지 A-to-Z 워크플로우"
    excerpt: "1인 개발자의 가장 큰 장벽인 '기획'과 '디자인'을 AI(Notion, Stitch)로 한 번에 해결하는 실용적인 워크플로우입니다."
    url: "/design/ai-workflow-prd-to-design/"

#################################################################
# 3. "TOPIC EXPLORER" (Sub-categories)
# _includes/feature_row.html 이 데이터를 사용함
#################################################################
feature_row:
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "AI 디자인"
    excerpt: "Stitch, Midjourney 등 AI를 활용한 디자인 자동화 팁."
    url: "/design/ai-design/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "UI/UX 원칙"
    excerpt: "1인 개발자가 바로 적용하는 실용적인 UI/UX 원칙과 팁."
    url: "/design/ui-ux-tips/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "디자인 리소스"
    excerpt: "무료 아이콘, 폰트, CSS 라이브러리 등 큐레이션."
    url: "/design/resources/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
---

{% include curated_row.html %}

<hr>

{% include feature_row %}

<hr>

<div class="latest-posts-row">
  <h2 class="archive__subtitle">최신 디자인 아티클</h2>

{% assign category_name = "design" %}

  <div class="archive">
    {% for post in site.categories[category_name] limit:3 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>

  <p style="text-align: right; margin-top: 1em;">
    <a href="{{ site.category_archive_path | default: '/categories/' | relative_url }}{{ category_name }}/" 
       class="btn btn--primary">
      모든 디자인 아티클 보기 &rarr;
    </a>
  </p>
</div>
