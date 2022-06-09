n = int(input())
a, b, c = sorted([int(_) for _ in input().split()])
ans = 9999
for i in range(n//c+1):
    p = i*c
    for j in range((n-p)//b+1):
        q = j*b
        if (n-p-q)%a == 0:
            ans = min(ans, i+j+(n-p-q)//a)
print(ans)