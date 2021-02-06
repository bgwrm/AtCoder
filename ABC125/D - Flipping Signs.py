n = int(input())
a = [int(_) for _ in input().split()]
abs_a, c = [], 0
for i in a:
    abs_a += [abs(i)]
    if i < 0:
        c += 1
print(sum(abs_a)-2*(c%2)*min(abs_a))