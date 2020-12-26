a, b, c = (int(_) for _ in input().split())

for i in range(b+1):
    if i * a % b == c:
        print('YES')
        exit()
print('NO')