n = int(input())
ng = [int(input()) for _ in range(3)]

if n in ng:
    print('NO')
    exit()

for i in range(100):
    if n-3 not in ng:
        n -= 3
    elif n-2 not in ng:
        n -= 2
    elif n-1 not in ng:
        n -= 1
    else:
        print('NO')
        exit()

if n <= 0:
    print('YES')
else:
    print('NO')