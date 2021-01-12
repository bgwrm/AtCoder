n = int(input())
a = [int(_) for _ in input().split()]
print(sum(a[i]%2==1 for i in range(0,n,2)))