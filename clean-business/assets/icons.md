# 아이콘 (2종만 사용)

이 디자인은 아이콘을 거의 쓰지 않습니다. 로고 별표와 원형 버튼 안의 화살표, 두 가지만 씁니다. 그 외 아이콘 칩, 컬러 아이콘, 이모지는 쓰지 않습니다.

| key | 용도 | 마크업 |
|---|---|---|
| mark | 로고 별표 (라이트 `--mark` 회색 · 다크 흰색) | `<span class="logo"><svg viewBox="0 0 24 24"><path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>LogoName</span>` |
| arrow | 원형 버튼 화살표 (기본 ↘) | `<span class="cbtn"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 8v9H8"/></svg></span>` |

화살표 방향은 클래스로 돌립니다. 기본은 ↘이고, `.ne`는 ↗, `.sw`는 ↙, `.nw`는 ↖입니다. 크기는 `.cbtn`(40px), `.lg`(56px), `.xl`(76px) 세 가지입니다.

- ↘ 표지·마무리 상단 바, 다음으로 넘어감
- ↗ 목차·대형 제목 옆, 외부 링크나 "자세히"
- ↙ 구분장 하단, 본문으로 들어감

실제 브랜드 로고가 있으면 별표 SVG 자리를 그 로고 SVG로 바꾸고, 높이는 20px, 색은 단색(`currentColor`)으로 맞춥니다.
