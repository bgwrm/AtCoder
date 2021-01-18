n = int(input())
a = sorted([int(_) for _ in input().split()])
if a.count(0) == n or (a.count(0) == n//3 and len(set(a)) == 2):
    print('Yes')
    exit()
if len(set(a)) == 3:
    x, y, z = list(set(a))
    if x^y^z == 0 and a.count(x) == a.count(y) == a.count(z):
        print('Yes')
        exit()
print('No')