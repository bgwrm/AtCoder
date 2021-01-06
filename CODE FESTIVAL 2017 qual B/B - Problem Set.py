n = int(input())
d = sorted([int(_) for _ in input().split()])
m = int(input())
t = sorted([int(_) for _ in input().split()])

num = 0
for i in d:
    if i == t[num]:
        num += 1
    if num >= m:
        print('YES')
        exit()
print('NO')