#Вводим функцию
def f(x):
    return x ** 2 + 2 * x + 1

#Вводим границы, а так же количество разбиений
divn = int(input('Введите n: '))
ainput = int(input('Введите нижнюю границу:'))
binput = int(input('Введите верхнюю границу:'))


def trapeze(f, n, a, b):
    x = 0
    dx = (b - a) / n    #ширина
    for i in range(n):
        x += dx * (f(a + dx * i) + f(a + dx + dx * i)) / 2  #Формула метода трапеций
    return x


print(trapeze(f, divn, ainput, binput)) #Вывод
