---
#################################################################
# 1. LAYOUT & HEADER
#################################################################
layout: splash
hidden: true # Hides from header navigation, if desired

# Page Header
header:
  overlay_color: "transparent"
  # overlay_image: /assets/images/coding-hero.jpg # (Optional)
  caption: # "Category"
  title: "Coding Hub"
  excerpt: "Practical tips, frameworks, and curated resources for 1-person-development."
  
#################################################################
# 2. "START HERE" (Curated Picks)
# Data is consumed by _includes/curated_row.html
#################################################################
curated_title: "Start Here: Recommended Guides"
curated_picks:
  - title: "1인 개발 기술 스택 선택 가이드"
    excerpt: "어떤 기술로 시작해야 할지 막막한 분들을 위한 첫 가이드입니다."
    url: "/coding/tech-stack-guide/"
  - title: "Firebase로 10분 만에 백엔드 구축하기"
    excerpt: "서버 없이 앱을 만드는 가장 빠른 방법을 소개합니다."
    url: "/coding/firebase-basics/"
  - title: "TBD: Post 3 Title"
    excerpt: "TBD: Post 3 Excerpt"
    url: "#"

#################################################################
# 3. "TOPIC EXPLORER" (Sub-categories)
# Data is consumed by _includes/feature_row.html
#################################################################
feature_row:
  - image_path: /assets/images/index/code-solid-full.svg # Placeholder
    title: "Frameworks"
    excerpt: "React, Svelte, Flutter, etc."
    url: "/coding/frameworks/" # (Future page)
    btn_label: "Learn More"
  - image_path: /assets/images/index/code-solid-full.svg # Placeholder
    title: "Backend & Infra"
    excerpt: "Firebase, Supabase, Vercel."
    url: "/coding/backend/" # (Future page)
    btn_label: "Learn More"
  - image_path: /assets/images/index/code-solid-full.svg # Placeholder
    title: "Dev Tools"
    excerpt: "VS Code, Git, CI/CD tips."
    url: "/coding/tools/" # (Future page)
    btn_label: "Learn More"
---

{% include curated_row.html %}

<hr>

{% include feature_row %}

<hr>

<div class="latest-posts-row">
  <h2 class="archive__subtitle">Latest Coding Posts</h2>

{% assign category_name = "coding" %}

  <div class="archive">
    {% for post in site.categories[category_name] limit:3 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>

  <p style="text-align: right; margin-top: 1em;">
    <a href="{{ site.category_archive_path | default: '/categories/' | relative_url }}{{ category_name }}/" 
       class="btn btn--primary">
      All Coding Posts &rarr;
    </a>
  </p>
</div>
