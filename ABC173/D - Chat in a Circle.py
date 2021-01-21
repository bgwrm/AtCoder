n = int(input())
a = sorted([int(_) for _ in input().split()], reverse=True)
print(a[0]+2*sum(a[1:(n-2)//2+1])+n%2*a[(n-1)//2])