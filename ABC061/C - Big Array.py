n, k = (int(_) for _ in input().split())
ab = [[int(_) for _ in input().split()] for i in range(n)]
l = [0] * (10**5 + 1)

for i in range(n):
    l[ab[i][0]] += ab[i][1]

for i in range(len(l)):
    k -= l[i]
    if k <= 0:
        print(i)
        exit()