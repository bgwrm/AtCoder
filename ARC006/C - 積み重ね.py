n = int(input())
w = [int(input()) for _ in range(n)]
l = []
for i in w:
    for j in range(len(l)):
        if i <= l[j]:
            l[j] = i
            l = sorted(l)
            break
    else:
        l += [i]
print(len(l))