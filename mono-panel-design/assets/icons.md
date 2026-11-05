# 아이콘 세트 (24×24 선 아이콘)

모든 아이콘은 `viewBox="0 0 24 24"` 기준이고, `fill:none`, `stroke:currentColor`, 굵기 1.6px, 끝·모서리 round로 통일합니다. 스타일은 `mono.css`의 `.ico`가 처리합니다. 사용법:

```html
<div class="ico"><svg viewBox="0 0 24 24"><path d="M7 17L17 7M9 7h8v8"/></svg></div>
```

| key | 용도 | path |
|---|---|---|
| arrow | 타일 우하단 CTA(기본) | `<path d="M7 17L17 7M9 7h8v8"/>` |
| code | 개발·웹 | `<path d="M8 9l-4 3 4 3M16 9l4 3-4 3M13 6l-2 12"/>` |
| slide | 발표·문서 | `<rect x="3" y="5" width="18" height="13" rx="2"/><path d="M7 14l3-3 3 2 4-4"/>` |
| loop | 반복·자동화 | `<path d="M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3M18 3v4h-4M6 21v-4h4"/>` |
| rocket | 출시·성장 | `<path d="M5 15c-1 2-1 4-1 4s2 0 4-1M9 15l-3-3c2-5 6-8 12-8 0 6-3 10-8 12l-1-1zM14 10h.01"/>` |
| table | 데이터·엑셀 | `<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/>` |
| doc | 보고서 | `<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>` |
| chart | 지표 | `<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>` |
| shop | 매장·커머스 | `<path d="M4 10l2-6h12l2 6M4 10v10h16V10M4 10h16M10 20v-5h4v5"/>` |
| edu | 교육 | `<path d="M3 9l9-5 9 5-9 5-9-5zM7 11v5c3 2 7 2 10 0v-5"/>` |
| user | 사람·대상 | `<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>` |
| pc | 장비·실습 | `<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>` |
| clock | 시간·일정 | `<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>` |

세트에 없는 아이콘이 필요하면 같은 규칙(24 그리드, 선만 사용, 1.6px, round, 채움 없음)으로 직접 그립니다. 이모지나 컬러 아이콘은 쓰지 않습니다.
