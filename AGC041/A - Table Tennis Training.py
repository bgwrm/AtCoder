n, a, b = (int(_) for _ in input().split())
print(min(a-1, n-b)+1+(b-a-1)//2 if abs(a-b)%2 == 1 else (b-a)//2)