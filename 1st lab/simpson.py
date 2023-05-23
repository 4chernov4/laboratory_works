def f(x):
    return x ** 2 + 2 * x + 1


a = int(input("Введите нижнюю границу: "))
b = int(input("Введите верхнюю границу: "))
n = int(input("Введите n: "))


def simpsonmethod(f, a, b, n):
    x = 0
    dx = (b - a) / n
    for i in range(n):
        x += dx/6 * (f(a) + 4 * f((a + b) / 2) + f(b))
    return x


print(simpsonmethod(f, a, b, n))
