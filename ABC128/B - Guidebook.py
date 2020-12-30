n = int(input())
l = []

for i in range(n):
    s, p = (input().split())
    l += [[s, -int(p), i+1]]

l = sorted(l)

for i in l:
    print(i[2])