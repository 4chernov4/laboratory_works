def f(x):
    return x ** 2 + 2 * x + 1


divn = int(input('Введите n: '))
ainput = int(input('Введите нижнюю границу:'))
binput = int(input('Введите верхнюю границу:'))


def rectangle(f, n, a, b):
    x = 0
    dx = (b - a) / n
    for i in range(n):
        x += dx * f(a + dx / 2 + i * dx)
    return x


print(rectangle(f, divn, ainput, binput))
