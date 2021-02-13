t = int(input())
for _ in range(t):
    l, r = (int(_) for _ in input().split())
    if 2*l <= r and l != r or l == r == 0:
        n = r-2*l+1
        print(n*(n+1)//2)
    else:
        print(0)