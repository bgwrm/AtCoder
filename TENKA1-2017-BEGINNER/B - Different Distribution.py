n = int(input())
xy = sorted([[int(_) for _ in input().split()] for i in range(n)],reverse=True)
print(xy[0][0]+xy[0][1])