"""Electric Blue 코일 오브젝트 생성기 — 유광 블루 3D 코일을 순수 SVG로 그린다.

원리: 휘어진 나선(helix)을 반 바퀴씩 잘라(뒤쪽 호 → 앞쪽 호 순서) 깊이 순으로 그리고,
각 호를 '굵은 어두운 선 → 가늘고 밝은 선' 여러 겹으로 겹쳐 튜브의 광택을 만든다.
밝은 겹일수록 왼쪽 위로 조금씩 밀어 하이라이트가 한쪽에 맺히게 한다.
필터·이미지·blur 없음 → PDF에서도 화면과 똑같이 인쇄된다.

사용: python3 coil.py [turns] [id] [spin] > coil.svg
  turns : 감긴 횟수 (기본 11)
  id    : 클래스 접두사 (한 HTML에 서로 다른 코일 2개를 넣을 때만 바꾼다, 기본 c)
  spin  : 화면상 회전 각도(도, 기본 0). 꼬리가 패널 밖으로 빠지게 할 때 쓴다. 광택은 항상 왼쪽 위
출력된 <svg>를 HTML에 그대로 붙이고, 크기는 감싸는 div의 width로만 조절한다.
"""
import math
import sys

turns = int(sys.argv[1]) if len(sys.argv) > 1 else 11
gid = sys.argv[2] if len(sys.argv) > 2 else "c"
spin = math.radians(float(sys.argv[3])) if len(sys.argv) > 3 else 0.0   # 화면 회전(도). 광택 방향은 유지

A, R, r = 300.0, 66.0, 40.0           # 중심 호 반지름 · 나선 반지름 · 튜브 반지름
th0, th1 = math.radians(-74), math.radians(80)
per_turn = 80
steps = turns * per_turn
tilt_x, tilt_y = math.radians(62), math.radians(-20)


def rot(x, y, z):
    y, z = y * math.cos(tilt_x) - z * math.sin(tilt_x), y * math.sin(tilt_x) + z * math.cos(tilt_x)
    x, z = x * math.cos(tilt_y) + z * math.sin(tilt_y), -x * math.sin(tilt_y) + z * math.cos(tilt_y)
    return x, y, z


def point(u):
    th = th0 + (th1 - th0) * u
    ph = 2 * math.pi * turns * u
    nx, ny = math.cos(th), math.sin(th)
    x, y, z = rot(A * nx + R * math.cos(ph) * nx, A * ny + R * math.cos(ph) * ny, R * math.sin(ph))
    _, _, zc = rot(A * nx, A * ny, 0)  # 같은 위치의 중심축 깊이
    s = 1100 / (1100 - z)              # 약한 원근
    x, y = x * s, y * s
    x, y = x * math.cos(spin) - y * math.sin(spin), x * math.sin(spin) + y * math.cos(spin)
    return x, y, z, z - zc


pts = [point(i / steps) for i in range(steps + 1)]

# 중심축보다 앞(+)/뒤(-)로 잘라 뒤쪽 호를 먼저, 앞쪽 호를 나중에 그린다
segs, cur = [], [pts[0]]
for a, b in zip(pts, pts[1:]):
    cur.append(b)
    if (a[3] >= 0) != (b[3] >= 0):
        segs.append(cur)
        cur = [b]
if len(cur) > 1:
    segs.append(cur)
segs.sort(key=lambda s: (sum(p[3] for p in s) > 0, sum(p[2] for p in s) / len(s)))

# 겹(layer): 굵은 어두운 선 → 가는 밝은 선. 밝을수록 왼쪽 위로 이동
ramp = [(0, (4, 12, 92)), (.18, (10, 30, 175)), (.42, (31, 77, 255)), (.66, (82, 120, 255)),
        (.84, (160, 186, 255)), (1, (240, 245, 255))]


def col(t):
    for (t0, c0), (t1, c1) in zip(ramp, ramp[1:]):
        if t <= t1:
            k = (t - t0) / (t1 - t0)
            return "#%02x%02x%02x" % tuple(round(a + (b - a) * k) for a, b in zip(c0, c1))
    return "#f0f5ff"


N = 28
layers = []
for i in range(N):
    t = i / (N - 1)
    w = 2.0 - 1.9 * (t ** 0.8)
    layers.append((w, col(t), 0.46 * (t ** 1.1)))
css = "".join(
    f".{gid}{i}{{fill:none;stroke:{c};stroke-width:{w * r:.1f};stroke-linecap:round;stroke-linejoin:round}}"
    for i, (w, c, _) in enumerate(layers)
)

xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
pad = r * 1.15
vb = f"{min(xs) - pad:.0f} {min(ys) - pad:.0f} {max(xs) - min(xs) + 2 * pad:.0f} {max(ys) - min(ys) + 2 * pad:.0f}"

defs, out = [], []
for n, s in enumerate(segs):
    d = "M" + "L".join(f"{x:.0f} {y:.0f}" for x, y, _, _ in s)
    defs.append(f'<path id="{gid}p{n}" d="{d}"/>')
    for i, (_, _, off) in enumerate(layers):
        dx, dy = -off * r * 0.55, -off * r
        pos = f' x="{dx:.1f}" y="{dy:.1f}"' if off else ""
        out.append(f'<use href="#{gid}p{n}" class="{gid}{i}"{pos}/>')
print(f'<svg class="coil" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><style>{css}</style>'
      f'<defs>{"".join(defs)}</defs>{"".join(out)}</svg>')
