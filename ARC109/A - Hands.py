a, b, x, y = (int(_) for _ in input().split())

if a == b:
    print(x)
if a < b:
    if 2*x >= y:
        print(x+y*(b-a))
    else:
        print(x+2*x*(b-a))
elif a > b:
    if 2*x >= y:
        print(x+y*(a-b-1))
    else:
        print(x+2*x*(a-b-1))