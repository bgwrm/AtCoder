import math
nxt = [int(x) for x in input().split()]
print(math.ceil(nxt[0] / nxt[1]) * nxt[2])