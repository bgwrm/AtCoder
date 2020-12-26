from decimal import Decimal
a, b = (Decimal(_) for _ in input().split())
print(int(a*b))