n, m = (int(_) for _ in input().split())
p = ['*'] * n

for i in range(m):
    s, c = (int(_) for _ in input().split())
    if p[s-1] == '*':
        p[s-1] = str(c)
    elif p[s-1] != str(c):
        print(-1)
        exit()

if p[0] == '0' and n > 1:
    print(-1)
    exit()
if p[0] == '*' and n > 1:
    p[0] = '1'
elif p[0] == '*' and n == 1:
    p[0] = '0'

print(''.join(p).replace('*', '0'))