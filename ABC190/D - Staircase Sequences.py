n = int(input())
ans, i = 0, 1
for i in range(1, 10**7):
    if (2*n-i*i+i) > 0 and (2*n-i*i+i)%(2*i) == 0:
        ans += 2
print(ans)