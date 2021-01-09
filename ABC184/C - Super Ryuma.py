a, b = (int(_) for _ in input().split())
c, d = (int(_) for _ in input().split())

if a == c and b == d:
    print(0)
elif a+b==c+d or a-b==c-d or abs(a-c)+abs(b-d)<=3:
    print(1)
elif abs(a+b+c+d)%2==0 or abs(a-c)+abs(b-d)<=6 or abs(a+b-c-d)<=3 or abs(a-b-c+d)<=3:
    print(2)
else:
    print(3)