a, b, c, d, e, f = (int(_) for _ in input().split())
water, sugar = [], []
co = w1 = w2 = 0
for i in range(0, f+1, 100*a):
    for j in range(0, f-i+1, 100*b):
        water += [i+j]
for k in range(0, f+1, c):
    for l in range(0, f-k+1, d):
        sugar += [k+l]
w1 = water[-1]
for w in water:
    for s in sugar:
        if 0 < w+s <= f and 100*s <= w*e and s/(w+s) > co:
            co, w1, w2 = s/(w+s), w+s, s
print(w1, w2)