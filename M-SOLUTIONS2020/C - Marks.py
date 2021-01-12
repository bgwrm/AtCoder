n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
for i in range(n-k):
    if a[i] < a[k+i]:
        print('Yes')
    else:
        print('No')