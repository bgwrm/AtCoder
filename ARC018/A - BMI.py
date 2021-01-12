from decimal import Decimal
h, b = (Decimal(_) for _ in input().split())
print(h*h*b/10000)