s, p = (int(_) for _ in input().split())
for n in range(1,10**6+1):
    if n*(s-n) == p:
        print('Yes')
        exit()
print('No')