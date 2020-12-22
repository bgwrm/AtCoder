n = int(input())
x = [int(_) for _ in input().split()]
sorted_x = sorted(x)
num1 = sorted_x[n//2-1]
num2 = sorted_x[n//2]

for i in x:
    print(num1 if i > num1 else num2)