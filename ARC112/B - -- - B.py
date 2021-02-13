b, c = (int(_) for _ in input().split())
if b <= 0:
    print(c+1+min(-2*b-1,c-2))
else:
    print(max(c-2,0)+min(2*b+1,c+1))