a, b, k = (int(_) for _ in input().split())

if a >= k:
    print(a-k, b)
elif b >= k-a:
    print(0, b-k+a)
else:
    print(0, 0)