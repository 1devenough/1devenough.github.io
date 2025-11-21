---
name: prompt-layout-diagram-positioning
description: 추상적인 다이어그램 요청 시 요소들이 뭉치는 현상을 방지하고, 원하는 위치에 정확히 배치하는 좌표 전략
keywords: layout, positioning, diagram, clock face, spacing, composition
---

## 📌 문제 (Problem) / 핵심 (Core)
"다이아몬드 모양으로 배치해줘"라고 추상적으로 요청하면, AI는 다이아몬드 '형태'를 인식하지 못하고 캐릭터들을 중앙에 뭉쳐(Clustering) 놓거나 무작위로 배치한다.

## 💡 원인 / 맥락 (Context)
생성형 AI는 공간적 관계(Spatial Relationship)를 추상적인 단어(Diamond, Circle)보다 구체적인 **위치 지시어**나 **좌표 개념**으로 더 잘 이해한다.

## ✅ 해결책 / 지침 (Solution / Rule)
추상적인 도형 이름 대신 **'시계 방향(Clock Face)'** 또는 **'절대 위치(Absolute Position)'**를 사용하여 강제한다.

1.  **위치 매핑:**
    * `Top Center (12 o'clock)`
    * `Bottom Center (6 o'clock)`
    * `Far Left (9 o'clock)`
    * `Far Right (3 o'clock)`
2.  **간격 강제:**
    * `Widely spaced apart` (넓게 띄워라)
    * `Do not cluster` (뭉치지 마라)
3.  **흐름 연결:** 각 요소를 `Thick, curved arrows`로 연결하여 시선의 흐름(Cycle)을 만든다.
