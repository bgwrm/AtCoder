n, d, k = (int(_) for _ in input().split())
lr = [[int(_) for _ in input().split()] for i in range(d)]
st = [[int(_) for _ in input().split()] for i in range(k)]
for s, t in st:
    d = 1
    if s < t:
        for l, r in lr:
            if l <= s:
                s = max(r, s)
                if s >= t:
                    print(d)
                    break
            d += 1
    else:
        for l, r in lr:
            if s <= r:
                s = min(l, s)
                if s <= t:
                    print(d)
                    break
            d += 1