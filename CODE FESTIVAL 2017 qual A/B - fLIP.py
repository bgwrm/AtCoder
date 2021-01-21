n, m, k = (int(_) for _ in input().split())
for i in range(n+1):
    for j in range(m+1):
        if (n-i)*(m-j)+i*j == k:
            print('Yes')
            exit()
print('No')