n, k, q = (int(_) for _ in input().split())
a = [int(input()) for _ in range(q)]
l = [0] * n
ans = 0

for i in a:
    l[i-1] += 1

for i in l:
    print('Yes' if k + i - q > 0 else 'No')