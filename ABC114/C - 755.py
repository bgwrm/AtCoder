import itertools
ans, n = 0, int(input())
for i in range(3, len(str(n))+1):
    for j in itertools.product(*['357'], repeat=i):
        if int(''.join(j)) <= n and len(set(j)) == 3:
            ans += 1
print(ans)