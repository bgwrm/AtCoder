xa, ya, xb, yb, xc, yc = (int(_) for _ in input().split())
print(abs((xb-xa)*(yc-ya)-(yb-ya)*(xc-xa))/2)