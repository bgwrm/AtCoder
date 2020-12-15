a, b = (int(_) for _ in input().split())

for i in range(1,1251):
    if (i*0.08)//1 == a and (i*0.1)//1 == b:
        print(i)
        exit()
print(-1)