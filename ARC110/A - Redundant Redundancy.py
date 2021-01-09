import math
n = int(input())
num = 1
for i in range(2,n+1):
    num = (num*i)//math.gcd(num,i)
print(num+1)