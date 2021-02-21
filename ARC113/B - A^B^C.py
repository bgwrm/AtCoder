a, b, c = (int(_) for _ in input().split())
a %= 10
if b > 4:
    b = b%4+4
if c > 4:
    c = c%4+4
e = b**c
if a in [0, 1, 5, 6]:
    print(a)
elif a in[2, 3, 7, 8]:
    p = e%4
    if p == 0:
        print((a**4)%10)
    else:
        print((a**p)%10)
else:
    if e%2:
        print(a)
    else:
        print((a*a)%10)