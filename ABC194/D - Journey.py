from decimal import Decimal
n = int(input())
c = 0
for i in range(1, n+1):
    c += Decimal(1/i)
print(n*c-1)