n = int(input())
l = [2, 1] + [0] * (n-1)
for i in range(2, n+1):
    l[i] = l[i-1] + l[i-2]
print(l[n])