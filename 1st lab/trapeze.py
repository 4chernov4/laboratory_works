def f(x):
    return x ** 2 + 2 * x + 1


divn = int(input('Введите n: '))
ainput = int(input('Введите нижнюю границу:'))
binput = int(input('Введите верхнюю границу:'))


def trapeze(f, n, a, b):
    x = 0
    dx = (b - a) / n
    for i in range(n):
        x += dx * (f(a + dx * i) + f(a + dx + dx * i)) / 2
    return x


print(trapeze(f, divn, ainput, binput))
