---
name: prompt-optimization-minimize-negative-constraints
description: 'Do not', 'No'와 같은 부정 제약(Negative Constraint)을 줄이고 긍정적 묘사로 전환하여 AI의 창의성을 극대화하는 전략
keywords: prompt engineering, negative prompt, constraints, creativity, positive framing, stylistic freedom
---

## 📌 문제 (Problem) / 핵심 (Core)
프롬프트에 "Do not...", "Avoid...", "No..."와 같은 부정 제약 조건이 많아질수록, 생성된 이미지의 창의성이 떨어지고 결과물이 경직되거나 밋밋해지는 현상이 발생한다. 
예를 들어, `No gradients`, `No outlines`, `No 3D`, `No shadow` 등을 나열하면 AI는 스타일을 살리기보다 '하지 말라는 것을 피하는 데' 집중하여 가장 안전하고 재미없는(Safe but Boring) 결과를 내놓는다.

## 💡 원인 / 맥락 (Context)
생성형 AI 모델은 확률적으로 가장 적절한 이미지를 찾아가는 구조다. 긍정 명령(Positive Prompt)은 AI에게 '갈 방향'을 알려주어 탐색 공간을 넓혀주지만, 부정 명령(Negative Prompt)은 '가지 말아야 할 곳'에 벽을 세우는 행위다. 
벽이 너무 많으면 AI가 움직일 수 있는 공간(Latent Space)이 좁아져서, Memphis 스타일 특유의 '과장됨', '유기적 흐름', '역동성' 같은 우연한 예술적 요소들까지 차단된다.

## ✅ 해결책 / 지침 (Solution / Rule)
1.  **긍정 프레임 전환 (Positive Framing):** 부정적인 제약을 긍정적인 묘사로 바꾼다.
    * *Bad (Negative):* "No outlines" (선 그리지 마)
    * *Good (Positive):* "Shapes defined by solid color blocks" (형태는 단색 블록으로 정의됨)
    * *Bad (Negative):* "Avoid realistic proportions" (현실적 비율 피해서)
    * *Good (Positive):* "Abstract and stylized geometric forms" (추상적이고 양식화된 기하학적 형태)
2.  **핵심 제약만 남기기 (Essential Negatives Only):**
    * 스타일을 완전히 파괴하는 치명적인 요소(예: "3D render", "Photo-realistic")나 반복되는 오류(예: "Bad anatomy", "Text")를 막을 때만 제한적으로 부정 명령을 사용한다.
    * 스타일의 미묘한 뉘앙스(예: 곡선의 정도, 색감의 미세 조정)는 긍정 묘사로 유도한다.
3.  **스타일 키워드 신뢰하기:**
    * 일일이 제약 조건을 나열하는 대신, 해당 스타일을 잘 설명하는 대표 장르명(예: `Corporate Memphis`, `Flat Vector Art`)을 사용하면 AI가 알아서 불필요한 요소(3D, 실사 느낌 등)를 배제한다.
    