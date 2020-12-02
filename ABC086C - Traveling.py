import sys

N = int(input())
now = [0, 0, 0]

for i in range (N):
    next = [int(n) for n in input().split()]
    dt = next[0] - now[0]
    dx = abs(next[1] - now[1])
    dy = abs(next[2] - now[2])
    if dt < dx + dy or (dt + dx + dy) % 2 == 1:
        print('No')
        sys.exit()
    now = next

print('Yes')