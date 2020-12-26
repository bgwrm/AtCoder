n = int(input())
b = [int(_) for _ in input().split()] + [0]
a = [0] * n
a[0] = b[0]

for i in range(n-1):
    a[i+1] = min(b[i], b[i+1])

a[len(a)-1] = b[len(b)-2]

print(sum(a))