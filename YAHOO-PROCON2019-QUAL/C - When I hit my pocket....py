k, a, b = (int(_) for _ in input().split())

if a+1 >= b or a-1 >= k:
    print(k+1)
else:
    print(a+(k-a+1)//2*(b-a)+(k-a+1)%2)