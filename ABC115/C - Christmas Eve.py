n, k = (int(_) for _ in input().split())
h = sorted([int(input()) for _ in range(n)])
l = [0] *(n-k+1)

for i in range(n-k+1):
    l[i] = h[i+k-1] - h[i]

print(min(l))