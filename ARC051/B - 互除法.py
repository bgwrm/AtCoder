k, l= int(input()), [1, 1]
for _ in range(k-1):
    l += [l[-2]+l[-1]]
print(*l[-2:])