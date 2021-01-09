n, m, a, b = (int(_) for _ in input().split())
for i in range(1,m+1):
    if n <= a:
        n += b
    c = int(input())
    n -= c
    if n < 0:
        print(i)
        exit()
print('complete')