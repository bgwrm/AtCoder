a, b, c, d = (int(_) for _ in input().split())

while(True):
    c = c - b
    if c <= 0:
        print('Yes')
        exit()
    a = a - d
    if a <= 0:
        print('No')
        exit()