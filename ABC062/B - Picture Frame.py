h, w = (int(_) for _ in input().split())
a = [input() for _ in range(h)]

print('#' * (w + 2))
for i in a:
    print('#' + i + '#')
print('#' * (w + 2))