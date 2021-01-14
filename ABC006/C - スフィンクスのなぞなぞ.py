n, m = (int(_) for _ in input().split())
if n*4 < m or n*2 > m:
    print(-1, -1, -1)
else:
    b = m%2
    c = (m-2*n)//2
    a = n-b-c
    print(a, b, c)