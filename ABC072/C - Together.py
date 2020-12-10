n = int(input())
a = [int(_) for _ in input().split()]
l = [0] * (10**5 + 2)

for i in a:
    l[i-1] += 1
    l[i] += 1
    l[i+1] += 1

print(max(l))