s = input()
a, b, c = s.count('a'), s.count('b'), s.count('c')
n = max(a, b, c)

if len(s) == 1:
    print('YES')
elif len(s) == 2:
    if a == b == 0 or b == c == 0 or c == a == 0:
        print('NO')
    else:
        print('YES')
else:
    if n-a <= 1 and n-b <= 1 and n-c <= 1:
        print('YES')
    else:
        print('NO')