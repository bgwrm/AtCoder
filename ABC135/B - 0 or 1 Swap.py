n = int(input())
p = [int(_) for _ in input().split()]
count = 0

for i in range(n):
    if p[i] != i + 1:
        count += 1

print('YES' if count <= 2 else 'NO')