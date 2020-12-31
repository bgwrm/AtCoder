l, h = (int(_) for _ in input().split())
n = int(input())
a = [int(input()) for _ in range(n)]

for i in a:
    if l <= i and i <= h:
        print(0)
    elif i <= l:
        print(l-i)
    else:
        print(-1)