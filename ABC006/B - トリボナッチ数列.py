n = int(input())
a = [0,0,1]
for i in range(3,n):
    a += [(a[-3]+a[-2]+a[-1])%10007]
print(a[n-1])