n, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
c = sum(a) / (4 * m)
count = 0

for p in a:
    if p >= c:
        count += 1

print('Yes' if count >= m else 'No')