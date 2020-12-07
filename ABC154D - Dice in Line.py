n, k = (int(_) for _ in input().split())
p = [int(_) for _ in input().split()]
num = sum(p[:k])
max = num

for i in range(n-k):
    num = num - p[i] + p[i+k]
    if max < num:
        max = num

print((k+max)/2)