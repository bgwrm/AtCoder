a, b, c = (int(_) for _ in input().split())
print((a*(a+1)//2 * b*(b+1)//2 * c*(c+1)//2)%998244353)