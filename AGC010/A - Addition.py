n = int(input())
a = [int(_) for _ in input().split()]
c = 0
for i in a:
    if i%2 == 1:
        c += 1
print('YES' if c%2 == 0 else 'NO')