# 아이콘 세트 (16×16 · 24×24)

Midnight Aurora는 아이콘을 거의 쓰지 않습니다. 정보 전달은 글자와 숫자가 하고, 아이콘은 **비교표의 지원 여부**와 **입력 바의 보조 기호**에만 씁니다. 스타일은 `midnight-aurora.css`의 `.ck`, `.nx`가 처리합니다.

## 비교표

| key | 용도 | 마크업 |
|---|---|---|
| check | 지원함 (sky 채움 원 + 검정 체크) | `<svg class="ck" viewBox="0 0 16 16"><circle cx="8" cy="8" r="8"/><path d="M4.8 8.2l2.1 2.1 4.3-4.4"/></svg>` |
| none | 지원 안 함 (짧은 회색 대시) | `<i class="nx"></i>` |

- 체크는 모든 열에서 같은 sky 색을 씁니다. 우리 열만 다른 색으로 칠하지 않고, 하이라이트 열(`.cmp .hl`)로 구분합니다.
- 빈 칸에 ×, 빨간 아이콘을 쓰지 않습니다. 대시나 빈칸으로 둡니다.

## 보조 선 아이콘 (필요할 때만, 24 그리드 · 1.6px · round · 채움 없음)

```html
<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7M9 7h8v8"/></svg>
```

| key | 용도 | path |
|---|---|---|
| arrow | 링크 · 다음 단계 | `<path d="M7 17L17 7M9 7h8v8"/>` |
| enter | 입력 바 끝(질문 실행) | `<path d="M20 5v7a3 3 0 0 1-3 3H5M9 11l-4 4 4 4"/>` |
| plus | 추가 · 확장 | `<path d="M12 5v14M5 12h14"/>` |
| dot | 상태 점 | `.tag .dot` 사용 (6px sky 원) |

선 아이콘은 `--sub` 또는 `--mute` 색으로 둡니다. 이모지 · 컬러 아이콘 · 아이콘 칩 배경은 쓰지 않습니다.
