x, y = (int(_) for _ in input().split())
k = int(input())
print(x+k if y>=k else x+2*y-k)