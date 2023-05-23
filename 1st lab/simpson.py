#Вводим функцию
def f(x):
    return x ** 2 + 2 * x + 1

#Вводим границы, а так же количество разбиений
a = int(input("Введите нижнюю границу: "))
b = int(input("Введите верхнюю границу: "))
n = int(input("Введите количество разбиений: "))


def simpsonmethod(f, a, b, n):
    x = 0
    dx = (b - a) / n    #ширина
    for i in range(n):
        x += dx/6 * (f(a) + 4 * f((a + b) / 2) + f(b))  #Формула метода Симпсона
    return x


print(simpsonmethod(f, a, b, n))    #Вывод
