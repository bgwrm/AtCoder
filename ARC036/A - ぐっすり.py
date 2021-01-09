n, k = (int(_) for _ in input().split())
t = [int(input()) for _ in range(n)]
s = sum(t[0:3])
if s < k:
    print(3)
    exit()
for i in range(3,n):
    s += t[i] - t[i-3]
    if s < k:
        print(i+1)
        exit()
print(-1)