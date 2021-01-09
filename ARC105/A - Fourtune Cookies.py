c = [int(_) for _ in input().split()]
for i in range(2**4):
    ate = 0
    for j in range(4):
        if (i>>j)&1:
            ate += c[j]
    if sum(c) - ate == ate:
        print('Yes')
        exit()
print('No')