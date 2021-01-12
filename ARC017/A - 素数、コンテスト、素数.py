n = int(input())
if n%2 == 0:
    print('NO')
    exit()
for i in range(3, n, 2):
    if n%i == 0:
        print('NO')
        exit()
print('YES')