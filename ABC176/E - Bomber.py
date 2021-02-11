h, w, m = (int(_) for _ in input().split())
xy = [[int(_) for _ in input().split()] for i in range(m)]
ch, cw = [0]*h, [0]*w
for x, y in xy:
    ch[x-1] += 1
    cw[y-1] += 1
mh, mw = max(ch), max(cw)
c, p = 0, ch.count(mh)*cw.count(mw)
for x, y in xy:
    if ch[x-1] == mh and cw[y-1] == mw:
        c += 1
print(mh+mw-(c==p))