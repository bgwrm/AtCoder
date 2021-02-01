import math
n, h = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(n)]
a, b = [list(i) for i in zip(*ab)]
a_max = max(a)
b = sorted(b, reverse=True)
ans = i = 0
while h > 0:
    if i < n and b[i] > a_max:
        h -= b[i]
        i += 1
        ans += 1
    else:
        ans += math.ceil(h/a_max)
        break
print(ans)