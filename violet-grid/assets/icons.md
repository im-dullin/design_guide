# 아이콘 세트 (24×24 흰 선 아이콘)

모든 아이콘은 `viewBox="0 0 24 24"`, `fill:none`, `stroke:currentColor`, 굵기 1.5px, 끝·모서리 round로 통일합니다. 크기·선 굵기는 `violet-grid.css`의 `.ic`(30px)가 처리합니다. 기본 사용처는 **블랙 페이지 위 아이콘 그리드**(`.icg`, 6열)이고, 아이콘 아래에 `.cap` 라벨을 붙입니다. 칩 배경이나 원형 테두리로 감싸지 않습니다.

```html
<div class="icg">
  <div><svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/></svg><span class="cap">퍼포먼스 광고</span></div>
</div>
```

| key | 용도 | path |
|---|---|---|
| flag | 깃발·목표 | `<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>` |
| target | 타깃팅 | `<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/>` |
| chart | 지표 | `<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>` |
| trend | 성장·상승 | `<path d="M3 17l6-6 4 4 8-8M15 7h6v6"/>` |
| bell | 푸시·알림 | `<path d="M6 16v-5a6 6 0 0 1 12 0v5l2 2H4l2-2zM10 21h4"/>` |
| user | 사람 | `<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>` |
| users | 팀·오디언스 | `<circle cx="9" cy="9" r="3.5"/><path d="M2.5 20c.8-3.5 3.3-5 6.5-5s5.7 1.5 6.5 5M16 5.5a3.5 3.5 0 0 1 0 7M18 15c2 .6 3.2 2.2 3.5 5"/>` |
| phone | 앱·모바일 | `<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.5h2"/>` |
| play | 영상 소재 | `<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9.5v5l4.5-2.5z"/>` |
| shield | 보안·검수 | `<path d="M12 3l7 3v6c0 4-3 7.5-7 9-4-1.5-7-5-7-9V6z"/>` |
| clock | 일정 | `<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>` |
| globe | 글로벌 | `<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9s-1 6.5-3.5 9c-2.5-2.5-3.5-5.5-3.5-9S9.5 5.5 12 3z"/>` |
| cart | 커머스 | `<path d="M3 4h2.5l2 11h11l2-8H6.5"/><circle cx="9" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>` |
| chat | 메시지·CRM | `<path d="M4 5h16v11H9l-5 4z"/>` |
| code | 개발·SDK | `<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>` |
| grid | 대시보드 | `<rect x="4" y="4" width="6.5" height="6.5"/><rect x="13.5" y="4" width="6.5" height="6.5"/><rect x="4" y="13.5" width="6.5" height="6.5"/><rect x="13.5" y="13.5" width="6.5" height="6.5"/>` |
| search | 리서치·ASO | `<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>` |
| mail | 이메일 | `<rect x="3" y="5" width="18" height="14"/><path d="M3 6l9 7 9-7"/>` |
| coin | 예산·매출 | `<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .8 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6.5V8M12 16v1.5"/>` |
| edu | 교육 | `<path d="M3 9l9-5 9 5-9 5-9-5zM7 11v5c3 2 7 2 10 0v-5"/>` |
| heart | 헬스케어 | `<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>` |
| game | 게임 | `<rect x="2.5" y="7" width="19" height="10" rx="5"/><path d="M7 10.5v3M5.5 12h3M15.5 11h.01M17.5 13h.01"/>` |
| card | 핀테크·결제 | `<rect x="3" y="5.5" width="18" height="13" rx="1.5"/><path d="M3 10h18M7 15h3"/>` |
| arrow | CTA·다음 | `<path d="M7 17L17 7M9 7h8v8"/>` |

세트에 없는 아이콘이 필요하면 같은 규칙(24 그리드, 선만, 1.5px, round, 채움 없음)으로 직접 그립니다. 이모지, 컬러 아이콘, 3D 아이콘은 쓰지 않습니다.
