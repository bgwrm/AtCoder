c = [input().split() for i in range(4)]
for i in range(3, -1, -1):
    print(*c[i][::-1])