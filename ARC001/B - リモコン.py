a, b = (int(_) for _ in input().split())
d = abs(b-a)
l = [0,1,2,3,2,1,2,3,3,2]
print(abs(b-a)//10+l[d%10])