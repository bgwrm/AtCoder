a, b, c = (int(_) for _ in input().split())
print('?' if a+b == a-b == c else '+' if a+b == c else '-' if a-b == c else '!')