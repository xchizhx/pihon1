a = int(input())
b = int(input())
c = int(input())
x = b ** 2 - (4 * a * c)

if x < 0:
    print("Корней нет")
else:
    print((x ** 0.5) - b / (2 * a))
    print(-b - (x ** 0.5) / (2 * a))
