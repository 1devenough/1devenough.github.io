---
name: prompt-color-brand-palette-control
description: 브랜드 컬러를 사용하면서도 이미지가 단조로운 듀오톤(Duotone)이 되거나 너무 쨍해지는 것을 방지하는 색상 전략
keywords: color palette, muted tone, pastel, brand color, saturation, low contrast
---

## 📌 문제 (Problem) / 핵심 (Core)
브랜드 컬러(예: Mint, Coral)를 프롬프트에 입력하면 AI가 피부, 머리카락, 사물까지 모든 요소를 해당 색으로 칠해버려 듀오톤(Duotone) 필터를 낀 것처럼 보인다. 반대로 다양성(Diversity)을 허용하면 브랜드 톤앤매너가 깨지고 색이 산만해진다.

## 💡 원인 / 맥락 (Context)
AI에게 색상 이름은 매우 강력한 토큰이다. "Mint and Coral palette"라고 하면 이를 '제약(Constraint)'으로 인식하여 다른 색 사용을 억제한다. 또한 `Bright`, `Vivid` 등의 수식어는 1DevEnough가 추구하는 '차분한 신뢰감(Zappy Style)'을 해친다.

## ✅ 해결책 / 지침 (Solution / Rule)
1.  **역할 분담 (Role Assignment):** 색상별 용도를 명확히 제한한다.
    * **브랜드 컬러 (Mint/Coral):** `Accent colors`, `Background shapes`, `Robots`, `Arrows`에만 사용.
    * **고유 색상 (Specifics):** 주인공의 `Yellow Hoodie`, `Dark Pants`, `Light Skin Tone`은 별도로 지정하여 브랜드 컬러의 침범을 막는다.
2.  **톤 보정 (Tone-on-Tone):** `Bright` 대신 **`Muted`, `Pastel`, `Soft`, `Matte`** 키워드를 사용하여 채도를 낮춘다.
3.  **배경색 지정:** 배경은 `Off-white`나 `Slightly brightened Mint (V>30)`를 사용하여 시인성을 확보한다.
