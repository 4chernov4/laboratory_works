#Вводим функцию
def f(x):
    return x ** 2 + 2 * x + 1

#Вводим границы, а так же количество разбиений
divn = int(input('Введите n: '))
ainput = int(input('Введите нижнюю границу:'))
binput = int(input('Введите верхнюю границу:'))


def rectangle(f, n, a, b):
    x = 0
    dx = (b - a) / n    #ширина
    for i in range(n):
        x += dx * f(a + dx / 2 + i * dx)   #Формула метода прямоугольников
    return x


print(rectangle(f, divn, ainput, binput))   #Вывод
