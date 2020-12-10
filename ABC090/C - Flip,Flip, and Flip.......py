n, m = (int(_) for _ in input().split())

if n == 1 and m == 1:
    print(1)
elif n == 1 or m == 1:
    print(n * m - 2)
elif n == 2 or m == 2:
    print(0)
else:
    print(n * m - 2 * n - 2 * m + 4)