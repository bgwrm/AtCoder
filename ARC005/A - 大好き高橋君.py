n = int(input())
s = input().split()
ans = 0
for i in range(n):
    if i == n-1:
        s[i] = s[i][:-1]
    if s[i]=="TAKAHASHIKUN" or s[i]=="Takahashikun" or s[i]=="takahashikun":
        ans += 1
print(ans)