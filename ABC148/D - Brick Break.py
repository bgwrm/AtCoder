n = int(input())
s = [int(_) for _ in input().split()]
target = 1

for i in s:
    if i == target:
        target += 1

print(-1 if target == 1 else n - target + 1)