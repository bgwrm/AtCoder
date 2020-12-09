n, a, b = (int(_) for _ in input().split())
s = input()

for i in range(n):
    if s[i] == 'a':
        if a > 0:
            print('Yes')
            a -= 1
        elif b > 0:
            print('Yes')
            b -= 1
        else:
            print('No')
    elif s[i] == 'b':
        if b > 0:
            print('Yes')
            b -= 1
        else:
            print('No')
    else:
        print('No')