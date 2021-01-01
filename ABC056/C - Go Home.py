x = int(input())
for i in range(1,10**9):
    if i*(1+i)//2 >= x:
        print(i)
        exit()