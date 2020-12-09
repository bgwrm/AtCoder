nab = [int(i) for i in input().split()]
ans = 0

for i in range(nab[0] + 1):
    num = 0
    for j in range(len(str(i))):
        num += int(str(i)[j])
    if num >= nab[1] and num <= nab[2]:
        ans += i

print(ans)