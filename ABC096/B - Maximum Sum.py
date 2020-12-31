x = sorted([int(_) for _ in input().split()])
k = int(input())

for i in range(k):
    x[2] *= 2

print(sum(x))