n = int(input())
ans = 0

for num in range(105, n+1, 2):
    l1, l2 = [], []
    i = 1
    while i*i <= num:
        if num%i == 0:
            l1 += [i]
            if num//i != i:
                l2 += [num//i]
        i += 1
    if len(l1)+len(l2) == 8:
        ans += 1

print(ans)