---
#################################################################
# 1. LAYOUT & HEADER
#################################################################
layout: splash
hidden: true # 네비게이션 메뉴에 이미 '모든 글' 링크가 있으므로 이 페이지 자체는 숨김

# 페이지 제목 (splash 레이아웃의 Hero 영역에 표시됨)
title: "모든 글"

# 페이지 부제목 (splash 레이아웃의 Hero 영역에 표시됨)
excerpt: "1DevEnough의 모든 글을 시간순으로 확인하세요."

# Page Header
header:
  overlay_color: "transparent"
  title: "모든 글"
  excerpt: "1DevEnough의 모든 글을 시간순으로 확인하세요."
---

<div class="latest-posts-row" style="margin-top: 2em; margin-bottom: 2em;">
  
  <h2 class="archive__subtitle">전체 글 ({{ site.posts | size }})</h2>

  <div class="archive">
    
    {% for post in site.posts %}
      
      {% include archive-single.html type="list" %}
    
    {% endfor %}
  
  </div>
</div>
