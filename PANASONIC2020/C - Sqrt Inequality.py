from decimal import Decimal
a, b, c = (int(_) for _ in input().split())
print('Yes' if Decimal(a).sqrt()+Decimal(b).sqrt()<Decimal(c).sqrt() else 'No')