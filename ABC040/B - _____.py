n = int(input())
ans = 10**6
for i in range(1,int(n**0.5)+1):
    ans = min(ans,abs(i-n//i)+n-n//i*i)
print(ans)