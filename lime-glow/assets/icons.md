# 아이콘 세트 (24×24 선 아이콘 · 라임 글로우 칩용)

모든 아이콘은 `viewBox="0 0 24 24"` 기준이고, `fill:none`, `stroke:var(--lime)`, 굵기 1.6px, 끝·모서리 round로 통일합니다. 스타일은 `lime-glow.css`의 `.gico`가 처리합니다. 다크 장의 4열 원칙/기능 그리드에서만 씁니다.

```html
<div class="gico"><i><svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg></i></div>
```

| key | 용도 | path |
|---|---|---|
| shield | 보안·접근 권한 | `<path d="M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/>` |
| lock | 개인정보·암호화 | `<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v2"/>` |
| spark | AI·거버넌스 | `<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/>` |
| user | 사람 검토·담당자 | `<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>` |
| card | 결제·카드 | `<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h4"/>` |
| chart | 지표·성장 | `<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>` |
| flow | 연동·자동화 | `<circle cx="6" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.5 6H14a4 4 0 0 1 4 4v5.5"/>` |
| doc | 문서·신고 | `<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h4"/>` |
| bank | 금융기관 | `<path d="M3 10l9-6 9 6M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18"/>` |
| clock | 일정·실시간 | `<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>` |

로고 마크는 아이콘이 아니라 `.logo` 안의 원 두 개 SVG(외곽 r7 선 + 중심 r2.4 점)를 그대로 씁니다. 세트에 없는 아이콘은 같은 규칙(24 그리드, 선만, 1.6px, round)으로 그리고, 이모지·컬러 아이콘은 쓰지 않습니다.
