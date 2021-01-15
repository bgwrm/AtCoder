n, t = (int(_) for _ in input().split())
ab = []
sa = sb = ans = 0
for i in range(n):
    a, b = (int(_) for _ in input().split())
    ab += [[a-b, a, b]]
    sa += a
    sb += b
if sa <= t:
    print(0)
elif sb > t:
    print(-1)
else:
    ab = sorted(ab, reverse=True)
    for abi, ai, bi in ab:
        sa -= abi
        ans += 1
        if sa <= t:
            print(ans)
            exit()