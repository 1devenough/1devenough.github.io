---
#################################################################
# 1. LAYOUT & HEADER
#################################################################
layout: splash
hidden: true

# 페이지 제목 (splash 레이아웃의 Hero 영역에 표시됨)
title: "인사이트 허브"

# 페이지 부제목 (splash 레이아웃의 Hero 영역에 표시됨)
excerpt: "1인 개발의 'Why/What': 비즈니스 전략, 사례 연구, 마인드셋 큐레이션."

# Page Header
header:
  overlay_color: "transparent"
  # overlay_image: /assets/images/insights-hero.jpg # (Optional)
  caption: # "Category"
  title: "인사이트 허브"
  excerpt: "1인 개발의 'Why/What': 비즈니스 전략, 사례 연구, 마인드셋 큐레이션."
  
#################################################################
# 2. "START HERE" (Curated Picks)
# _includes/curated_row.html 이 데이터를 사용함
#################################################################
curated_title: "시작 가이드: 추천 인사이트"
curated_picks:
  - title: "'알라미' 사례 연구 분석"
    excerpt: "성공적인 1인 개발 앱 '알라미'의 핵심 전략을 분석합니다."
    url: "/insights/alarmy-case-study/"
  - title: "AI로 기획부터 디자인 시스템까지 A-to-Z 워크플로우"
    excerpt: "1인 개발자의 가장 큰 장벽인 '기획'과 '디자인'을 AI(Notion, Stitch)로 한 번에 해결하는 실용적인 워크플로우입니다."
    url: "/design/ai-workflow-prd-to-design/"    

#################################################################
# 3. "TOPIC EXPLORER" (Sub-categories)
# _includes/feature_row.html 이 데이터를 사용함
#################################################################
feature_row:
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "사례 연구"
    excerpt: "성공 및 실패 사례 분석."
    url: "/insights/case-studies/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "비즈니스・전략"
    excerpt: "수익화, 법률, 마케팅 전략."
    url: "/insights/business/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
  - image_path: /assets/images/index/chart-simple-solid-full.svg # Placeholder
    title: "마인드셋"
    excerpt: "지속가능성, 동기부여."
    url: "/insights/mindset/" # (Future page)
    btn_label: "더 알아보기"
    disabled: true
---

{% include curated_row.html %}

<hr>

{% include feature_row %}

<hr>

<div class="latest-posts-row">
  <h2 class="archive__subtitle">최신 인사이트</h2>

{% assign category_name = "insights" %}

  <div class="archive">
    {% for post in site.categories[category_name] limit:3 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>

  <p style="text-align: right; margin-top: 1em;">
    <a href="{{ site.category_archive_path | default: '/categories/' | relative_url }}{{ category_name }}/" 
       class="btn btn--primary">
      모든 인사이트 보기 &rarr;
    </a>
  </p>
</div>
