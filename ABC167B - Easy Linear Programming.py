a, b, c, k = (int(_) for _ in input().split())

if a >= k:
    print(k)
elif b >= k:
    print(a)
else:
    print(2 * a + b - k)