a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a >= 1 and b >= 3 and c >= 2 and d >= 1:
    cheese = b // 3
    pork = c // 2
    z = min(cheese, pork, a, d)
    print(z)
else:
    print(0)