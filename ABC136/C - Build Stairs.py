n = int(input())
h = [int(_) for _ in input().split()]
h_max = h[0]

for i in range(1, n):
    if h_max - 1 > h[i]:
            print('No')
            exit()
    else:
        h_max = max(h_max, h[i])

print('Yes')