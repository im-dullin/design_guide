# Design Guide

실제 작업에서 잘 나온 문서 디자인을 **Claude Code 스킬** 형태의 디자인 가이드로 모아 둔 저장소입니다. 폴더 하나를 `~/.claude/skills/`에 복사하면, 어느 Claude Code에서도 같은 톤의 결과물이 나옵니다.

## Designs

<!-- GALLERY:START -->
<table>
<tr><td width="50%" valign="top"><a href="mono-panel-design/"><img src="mono-panel-design/preview/thumbnail.png" width="100%"></a><br><b><a href="mono-panel-design/">Mono Panel</a></b><br><sub>다크 패널 · 얇은 영문 디스플레이 · 페일 블루 단일 액센트의 에디토리얼 IR덱</sub></td></tr>
</table>

| 디자인 | 폴더 | 잘 맞는 문서 | 추가일 |
|---|---|---|---|
| [Mono Panel](mono-panel-design/) | `mono-panel-design` | 제안서 · 소개서 · 커리큘럼 · 보고서 | 2026-11-06 |
<!-- GALLERY:END -->

## 사용법

```bash
git clone https://github.com/im-dullin/design_guide.git
cp -R design_guide/<디자인 폴더> ~/.claude/skills/        # 모든 프로젝트에서 사용
# 또는 <project>/.claude/skills/ 에 복사하면 해당 프로젝트에서만 사용

pip install playwright pillow && python3 -m playwright install chromium   # PDF 렌더용 (한 번만)
```

Claude Code에 "`<디자인 폴더명>` 스킬로 ○○ 만들어줘"라고 요청합니다. 디자인별 상세 내용은 각 폴더의 README에 있습니다.

## 새 디자인 추가 규칙

디자인마다 폴더 하나를 만들고 아래 구성을 맞춥니다.

```
<design-slug>/
├── SKILL.md              필수 · frontmatter(name = 폴더명, description) + 규칙서
├── README.md             필수 · 미리보기 이미지 · 설치 · 사용법
├── design.json           필수 · 갤러리 메타 {name, slug, summary, formats, best_for, added}
├── assets/               CSS · 아이콘 등
├── templates/            시작용 템플릿
├── scripts/              렌더 스크립트
├── guide/                그 디자인으로 만든 '디자인 가이드 샘플' 문서 (html · pdf)
└── preview/
    ├── thumbnail.png     필수 · 800×450 · 루트 갤러리 썸네일
    └── guide/            가이드 샘플 장별 PNG (README 노출용)
```

폴더를 추가한 뒤 아래 명령으로 이 README의 갤러리를 다시 만들고 커밋합니다.

```bash
python3 scripts/update_gallery.py
```
