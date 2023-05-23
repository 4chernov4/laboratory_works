import math

x0 = float(input('Введите начальное приближение х0: '))


def f(x):
    return math.cos(x) - x ** 3


def df(x):
    return -math.sin(x) - 3 * (x ** 2)


def newtonmethod(func, dfunc, xmain, limitation=1e-9):
    x = xmain
    while abs(func(x)) >= limitation:
        if dfunc(x) == 0:
            break
        x = x - func(x) / dfunc(x)
    return x


print(newtonmethod(f, df, x0))